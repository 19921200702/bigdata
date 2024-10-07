import pymysql
conn = pymysql.Connection(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database='db_itheima'
)
cursor = conn.cursor()
result = cursor.execute("select * from product")

for i in range(result):
    result = cursor.fetchall()
    print(result)