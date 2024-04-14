import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='root',
    database = 'db_itheima')
cursor = conn.cursor()
sql = "select * from product"
count = cursor.execute(sql)
print(count)
for i in range(count):
    result = cursor.fetchone()
    print(result)
