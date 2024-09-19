import pymysql


class Usermodel:
    def nextpk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select max(id) from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = Usermodel.nextpk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "insert into user values(%s,%s,%s,%s,%s,%s,%s)"
        data = (id, first_name, last_name, login_id, password, dob, address)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data inserted Successfully")

    def update(self, data):
        password = data['password']
        id = data['id']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "update user set password =%s where id =%s"
        data = (password, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Updated Successfully!")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "delete from user where id=%s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("Data Deleted Successfully!")

    def getbyid(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from user where id =%s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        ColumnName = ('id', 'first_name', 'last_name', 'login_id', 'password', 'dob', 'address')
        res = []
        for x in result:
            res.append({ColumnName[i]: x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res

    def getbylogin(self, login_id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from user where login_id =%s"
        data = (login_id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        ColumnName = ('id', 'first_name', 'last_name', 'login_id', 'password', 'dob', 'address')
        res = []
        for x in result:
            res.append({ColumnName[i]: x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res

    def search(self,data):
        id=data.get('id',0)
        login_id=data.get('login_id','')
        pageno=data.get('pageno',1)
        pagesize=data.get('pagesize',0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from user where 1=1"
        if id !=0:
            sql+= " and id ="+str(id)
        if login_id != '':
            sql+= " and login_id='"+login_id+"'"
        if pagesize>0:
            pageno=(pageno-1)*pagesize
            sql+= " limit " +str(pageno)+ ", " +str(pagesize)
        print("sql=>",sql)
        cursor.execute(sql)
        result=cursor.fetchall()
        ColumnName = ('id', 'first_name', 'last_name', 'login_id', 'password', 'dob', 'address')
        res=[]
        for x in result:
            res.append({ColumnName[i]:x[i] for i , _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res


    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from user"
        cursor.execute(sql)
        result=cursor.fetchall()
        ColumnName = ('id', 'first_name', 'last_name', 'login_id', 'password', 'dob', 'address')
        res = []
        for x in result:
            res.append({ColumnName[i]: x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res


