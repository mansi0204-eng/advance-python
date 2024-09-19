import pymysql


class MarksheetModel:
    def nextPK(self):
        PK = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select max(id) from marksheet"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                PK = data[0]
        connection.commit()
        connection.close()
        return PK + 1

    def add(self,data):
        id=MarksheetModel.nextPK(self)
        roll_no=data['roll_no']
        name=data['name']
        physics=data['physics']
        chemistry=data['chemistry']
        maths=data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql="insert into marksheet values(%s,%s,%s,%s,%s,%s)"
        data=(id,roll_no,name,physics,chemistry,maths)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("Data Inserted Successfully!")


    def update(self,data):
        id=data['id']
        # roll_no=data['roll_no']
        name=data['name']
        # physics=data['physics']
        # chemistry=data['chemistry']
        # maths=data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql="update marksheet set name=%s where id =%s"
        data=(name,id)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("Data Updated Successfully!")

    def delete(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql="delete from marksheet where id=%s "
        data=(id)
        cursor.execute(sql,data)
        connection.commit()
        connection.close()
        print("Data Deleted Successfully!")

    def getbyid(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql="select * from marksheet where id =%s"
        data=(id)
        cursor.execute(sql,data)
        result=cursor.fetchall()
        columnname=('id','roll_no','name','physics','chemistry','maths')
        res=[]
        for x in result:
            print({columnname[i]:x[i] for i, _ in  enumerate(x)})
            res.append({columnname[i]:x[i] for i , _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res


    def getbyroll(self,roll_no):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from marksheet where roll_no=%s"
        data=(roll_no)
        cursor.execute(sql,data)
        result=cursor.fetchall()
        columname=('id','roll_no','name','physics','chemistry','maths')
        res=[]
        for x in result:
            print({columname[i]:x[i] for i, _ in enumerate(x)})
            res.append({columname[i]:x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res

    def read(self):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from marksheet "
        cursor.execute(sql)
        result=cursor.fetchall()
        columname=('id','roll_no','name','physics','chemistry','maths')
        res=[]
        for x in result:
            # print({columname[i]: x[i] for i, _ in enumerate(x)})
            res.append({columname[i]: x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res

    def search(self,data):
        id=data.get('id',0)
        roll_no=data.get('roll_no',0)
        name=data.get('name','')
        pageno=data.get('pageno',1)
        pagesize=data.get('pagesize',0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='python')
        cursor = connection.cursor()
        sql = "select * from marksheet where 1=1"
        if name != '':
            sql+=" and name='"+name+"'"
        if id!= 0:
            sql+=" and id=" +str(id)
        if (pagesize>0):
            pageno=(pageno-1)*pagesize
            sql+= " limit "+str(pageno)+ ", " +str(pagesize)
        print("sql=.>",sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        columname = ('id', 'roll_no', 'name', 'physics', 'chemistry', 'maths')
        res = []
        for x in result:
            # print({columname[i]: x[i] for i, _ in enumerate(x)})
            res.append({columname[i]: x[i] for i, _ in enumerate(x)})
        connection.commit()
        connection.close()
        return res


