from datetime import datetime
import logging

from extract import Extract

def create_extractor(url):
    return Extract(url)


if __name__ == '__main__':
    
    logging.basicConfig(level=logging.INFO)
    
    data = datetime.now().strftime("%m-%d-%Y") 
    horario = datetime.now().strftime("%H-%M")
    file_name = f"dolar_{data}_{horario}"
    
    
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='01-01-2024'&@dataFinalCotacao='05-15-2025'&$top=500&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"
    
    
    extractor = create_extractor(url)
    logging.info(f'Extraindo dados {data}')
    
    response = extractor.extract_api()
    dataframe = extractor.request_into_dataframe(response)
    extractor.save_dataframe_into_csv(df=dataframe, name=file_name)
    ##extractor.save_dataframe_into_parquet(df=dataframe, name=file_name)
    
    dataframe_final = extractor.tratativas_dataframe(dataframe)
    extractor.save_dataframe_into_csv(df=dataframe_final, name="final")
    