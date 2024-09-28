from django.db import connection


class Userservice:

    def pknext(self):
        pk = 0
        with connection.cursor() as cursor:
            sql = "select max(id) from ors_user"
            cursor.execute(sql)
            result = cursor.fetchall()
        connection.close()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        return pk + 1

    def add(self, data):

        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        Dob = data['Dob']
        address = data['address']

        sql = "insert into ors_user values((%s), (%s), (%s), (%s), (%s), (%s), (%s))"
        data = [Userservice.pknext(self), first_name, last_name, login_id, password, Dob, address]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        Dob = data['Dob']
        address = data['address']
        id = data['id']
        sql = "update ors_user set first_name = (%s), last_name = (%s), login_id = (%s), password = (%s), Dob = (%s), address = (%s) where id = (%s)"
        data = [first_name, last_name, login_id, password, Dob, address, id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        sql = "delete from ors_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def auth(self, login_id, password):
        sql = "select * from ors_user where login_id = (%s) and password = (%s)"
        data = [login_id, password]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "Dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def get(self, id):
        sql = "select * from ors_user where id = (%s)"
        data = [id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "Dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def findByLogin(self, login_id):
        sql = "select * from ors_user where login_id = (%s)"
        data = [login_id]
        cursor = connection.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "Dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res

    def search(self, param):
        first_name = param.get("first_name", "")
        pageno = param.get("pageno", 0)
        pagesize = param.get("pagesize", 0)
        sql = "select * from ors_user where 1=1"
        if first_name != "":
            sql += " and first_name like '" + first_name + "%%' "
        if (pagesize > 0):
            pageno = (pageno - 1) * pagesize
            sql += " limit " + str(pageno) + ", " + str(pagesize)
        print('sql => ', sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        columnName = ("id", "first_name", "last_name", "login_id", "password", "Dob", "address")
        res = []
        for x in result:
            print({columnName[i]: x[i] for i, _ in enumerate(x)})
            res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
        return res
