import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
cursor = connection.cursor()
sql = "select * from marksheet"
cursor.execute(sql)
result = cursor.fetchall()
for data in result:
    print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', data[4], '\t', data[5])
connection.commit()
connection.close()
