import pymysql


def testconnect():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
    cursor = connection.cursor()
    return connection, cursor


class MarksheetModel:
    def add(self, data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection, cursor = testconnect()
        sql = "insert into marksheet values(%s,%s,%s,%s,%s,%s) "
        data = (id, roll_no, name, physics, chemistry, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Inserted Successfully!")

    def update(self, data):
        id = data['id']
        name = data['name']
        connection, cursor = testconnect()
        sql = "update marksheet set name=%s where id=%s"
        data = (name, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Updated Successfully!")

    def delete(self, data):
        id = data['id']
        connection, cursor = testconnect()
        sql = "delete from marksheet where id=%s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Record Deleted Successfully!")

    def read(self):
        connection, cursor = testconnect()
        sql = "select * from marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def getbyid(self, data):
        id = data['id']
        connection, cursor = testconnect()
        sql = "select * from marksheet where id=%s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], data[4], '\t', data[5])
        connection.commit()
        connection.close()

    def search(self, data):
        id=data.get('id',0)
        roll_no = data.get('roll_no', 0)
        name = data.get('name', '')
        # physics=data.get('physics',0)
        # chemistry=data.get('chemistry',0)
        # maths=data.get('maths',0)
        pagesize = data.get('pagesize', 0)
        pageNo = data.get('pageNo', 1)
        connection, cursor = testconnect()
        sql = "select * from marksheet where 1=1"
        if id != 0:
            sql+= " and id = " +str(id)
        if name != '':
            sql += " and name ='" + name + "'"
        if roll_no != 0:
            sql += " and roll_no=" + str(roll_no)
        if (pagesize > 0):
            pageNo = (pageNo - 1) * pagesize
            sql += " limit " + str(pageNo) + ", " + str(pagesize)
        print("sql=>", sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], data[4], '\t', data[5])
        connection.commit()
        connection.close()



