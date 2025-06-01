import requests
import json
import pandas as pd


class Extract():
    def __init__(self, url):
        self.url = url
        
    def extract_api(self):
        request = requests.get(self.url).json().get('value')
        return request
    
    def request_into_dataframe(self, request):
        df = pd.DataFrame(request)
        
        return df
    
    def save_dataframe_into_csv(self, df, name):
        df.to_parquet(f'D:\\Projetos\\Python\\Data_Engineering\\dolar-pipeline\\data\\{name}.parquet', index=False)