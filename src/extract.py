import requests
import json
import pandas as pd
import logging
from datetime import datetime


class Extract():
    def __init__(self, url):
        self.url = url
        
    def extract_api(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json().get('value')
            if data:
                return data
        except Exception as e:
            logging.info(f'Erro ao extrair dados: {e}')
            return []
    
    def request_into_dataframe(self, response):
        df = pd.DataFrame(response)
        df['data_extracao'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        return df
    
    def save_dataframe_into_csv(self, df, name):
        path = f'D:\\Projetos\\Python\\Data_Engineering\\dolar-pipeline\\data\\{name}.csv'
        df.to_csv(path, index=False)
        
    
    def save_dataframe_into_parquet(self, df, name):
        path = f'D:\\Projetos\\Python\\Data_Engineering\\dolar-pipeline\\data\\{name}.parquet'
        df.to_parquet(path, index=False)
        return path
        
    def tratativas_dataframe(self, df):
        df['dataHoraCotacao'] = pd.to_datetime(df['dataHoraCotacao'])
        df['data'] = df['dataHoraCotacao'].dt.date
        
        datas = pd.date_range(start='2024-01-01', end='2025-05-15', freq='D')
        df_datas = pd.DataFrame(datas, columns=['data'])
        
        df['data'] = pd.to_datetime(df['data'])         
        df_datas['data'] = pd.to_datetime(df_datas['data'])
        
        df_merged = pd.merge(df_datas, df[['data', 'cotacaoCompra', 'cotacaoVenda', 'dataHoraCotacao', 'data_extracao']], on='data', how='left')
        df_merged.sort_values('data', inplace=True)  
        df_merged.fillna(method='bfill', inplace=True) 
        df_merged.fillna(method='ffill', inplace=True)
        
        return df_merged