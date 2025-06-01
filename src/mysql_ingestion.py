import pymysql
import logging

class MysqlLoader():
    def __init__(self, host_name, user, pw):
        self._host_name = host_name
        self._user = user
        self._pw = pw
    
    def connect_mysql(self):
        try:
            connection = pymysql.connect(
                host= self._host_name,
                user = self._user,
                password = self._pw
            )
            logging.info('Sucesso ao conetar com MySQL!')
            print('Sucesso ao conetar com MySQL!')
            return connection
        except Exception as e:
            logging.info(f'Erro ao conectar com MySQL: {e}')
    
    def create_cursor(self, connection):
        cursor = connection.cursor()
        return cursor
    
    def load_data(self, connection, cursor, db_name, tb_name, df):
        list = [tuple(row) for i, row in df.iterrows()]
        sql = f'INSERT INTO {db_name}.{tb_name} VALUES (%s,%s,%s,%s,%s)'
        
        cursor.executemany(sql, list)
        logging.info(f'\n {cursor.rowcount} dados foram inseridos na tabela {tb_name}')
        connection.commit()