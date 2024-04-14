from 测试1.config import project_config as conf
import pymysql
class MySQLUtil:
    def __init__(self,
                 host = conf.metadata_host,
                 port = conf.metadata_port,
                 user = conf.metadata_user,
                 password = conf.metadata_password):
        self.conn = pymysql.Connection(
            host= host,
            port = port,
            user = user,
            password = password,
        )
    def execute(self,sql):
        cursor = self.conn.cursor()
        print(cursor.execute(sql))
        cursor.close()
