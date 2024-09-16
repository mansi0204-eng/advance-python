import pymysql


def testInsert1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(5, 105, 'ppp', 13, 48, 38)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert2():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (6, 106, 'kkk', 78, 67, 56)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert3(id, roll_no, name, physics, chemistry, maths):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, roll_no, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


def testInsert4(data):
    id = data['id']
    roll_no = data['roll_no']
    name = data['name']
    physics = data['physics']
    chemistry = data['chemistry']
    maths = data['maths']
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
    cursor = connection.cursor()
    sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s)"
    data = (id, roll_no, name, physics, chemistry, maths)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print('data inserted successfully')


# testInsert1()
# testInsert2()
# testInsert3(7, 107, 'ttt', 89, 77, 67)

params = {'id':5,'roll_no':105,'name':'nikhil','physics':86,'chemistry':89,'maths':92}

testInsert4(params)
