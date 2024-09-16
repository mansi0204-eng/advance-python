
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
cursor = connection.cursor()
sql = "update marksheet set name = 'aaa' where id = 1"
cursor.execute(sql)
connection.commit()
connection.close()
print('data updated successfully')