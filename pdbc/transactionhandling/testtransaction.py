import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')

try:

    cursor = connection.cursor()
    sql1 = "insert into marksheet values(9,109,'shreyansh',59,16,56)"
    sql2 = "insert into marksheet values(9,110,'ansh',59,16,56)"
    sql3 = "insert into marksheet values(11,111,'shreyansh',59,16,56)"
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    connection.commit()
    connection.close()
    print("data inserted successfully")
except Exception as e:
    connection.rollback()
    print('exception: ', e)
