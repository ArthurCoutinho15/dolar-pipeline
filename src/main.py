from extract import Extract

def create_extractor(url):
    return Extract(url)


if __name__ == '__main__':
    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1\
    /odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao='05-30-2025'&%24format=json"
    
    
    extractor = create_extractor(url)
    request = extractor.extract_api()
    dataframe = extractor.request_into_dataframe(request)
    extractor.save_dataframe_into_csv(df=dataframe, name='dolar_1')
    