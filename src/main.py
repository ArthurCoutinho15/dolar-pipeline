from datetime import datetime
import logging
import os
from dotenv import load_dotenv

from extract import Extract
from s3_ingestion import BucketLoader
from mysql_ingestion import MysqlLoader

load_dotenv()

def create_extractor(url):
    return Extract(url)

def s3_connection(aws_access_key_id, aws_secret_access_key, region_name):
    return BucketLoader(aws_access_key_id, aws_secret_access_key, region_name)

def mysql_connection(host_name, user, pw):
    return MysqlLoader(host_name, user, pw)
    


if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO)
    
    data = datetime.now().strftime("%m-%d-%Y") 
    horario = datetime.now().strftime("%H")
    file_name = f"dolar_{data}_{horario}"
    
    
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2024'&@dataFinalCotacao='05-15-2025'&$top=500&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
    
    
    extractor = create_extractor(url)
    logging.info(f'Extraindo dados {data}')
    
    # Extração da api e tratamentos
    response = extractor.extract_api()
    dataframe = extractor.request_into_dataframe(response)
    
    dataframe_final = extractor.tratativas_dataframe(dataframe)
    extractor.save_dataframe_into_csv(df=dataframe_final, name="final")
    parquet = extractor.save_dataframe_into_parquet(df=dataframe_final, name=file_name)
    
    # Configuração e persistência no s3
    bucket_loader = s3_connection(
        aws_access_key_id = str(os.getenv('aws_access_key_id')),
        aws_secret_access_key= str(os.getenv('aws_secret_access_key')),
        region_name= str(os.getenv('region_name'))
    
    )
    
    s3 = bucket_loader.s3_connection()
    
    bucket_loader.s3_upload_files(s3, parquet, str(os.getenv('bucket_name')),'staging/dolar.parquet' )
    
    # Carga para mysql
    mysql_loader = mysql_connection(
        host_name=str(os.getenv('HOST')),
        user=str(os.getenv('USER')),
        pw = str(os.getenv('PASS'))
    )
    
    connection = mysql_loader.connect_mysql()
    cursor = mysql_loader.create_cursor(connection)
    mysql_loader.load_data(
        connection=connection, 
        cursor=cursor,
        db_name=str(os.getenv('DB_NAME')),
        tb_name=str(os.getenv('DB_TABLE')),
        df=dataframe_final
    )