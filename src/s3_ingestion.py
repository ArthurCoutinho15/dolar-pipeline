import boto3
import logging

class BucketLoader():
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key
        self._region_name = region_name
    
    def s3_connection(self):
        try:
            boto3.setup_default_session(
                aws_access_key_id = self._aws_access_key_id,
                aws_secret_access_key = self._aws_secret_access_key,
                region_name = self._region_name
            )
            
            s3 = boto3.client('s3')
            logging.info('Sucesso na conexão com s3')
            return s3
        except Exception as e:
            logging.info(f'Erro ao fazer conexão com s3: {e}')
    
    def s3_upload_files(self, s3, file_path, bucket_name, s3_key):
        try:
            with open(file_path, "rb") as data:
                s3.put_object(
                    Bucket=bucket_name,
                    Key=s3_key,
                    Body=data
                )
            logging.info('Sucesso ao carregar arquivo para s3')
        except Exception as e:
            logging.info(f'Erro ao carregar arquivos para o s3: {e}')