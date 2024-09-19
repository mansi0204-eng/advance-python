import datetime

from Usermodel import Usermodel

model = Usermodel()


def testadd():
    param1 = {'first_name': 'yash', 'last_name': 'sharma', 'login_id': '103yash', 'password': 'y5685',
             'dob': datetime.date(2003, 7, 12),
             'address': 'barwani'}
    param2 = {'first_name': 'nikhil', 'last_name': 'kumawat', 'login_id': '104yash', 'password': 'n565s85',
             'dob': datetime.date(2006, 9, 27),
             'address': 'nisarpur'}
    model.add(param1)
    model.add(param2)


def testupdate():
    param = {'password': '66mak', 'id': 1}
    model.update(param)

def testdelete():
    model.delete(1)

def testgetbyid():
    g=model.getbyid(1)
    print(g)
    for data in g:
        print(data['id'],'\t',data['first_name'],'\t',data['last_name'],'\t',data['login_id'],'\t',data['password'],'\t',data['dob'],'\t',data['address'],'\t')

def testgetbylogin_id():
    g=model.getbylogin('102mohit')
    print(g)
    for data in g:
        print(data['id'],'\t',data['first_name'],'\t',data['last_name'],'\t',data['login_id'],'\t',data['password'],'\t',data['dob'],'\t',data['address'],'\t')

def testsearch():
    param={'pagesize':2}
    list=model.search(param)
    for data in list:
        print(data['id'],'\t',data['first_name'],'\t',data['last_name'],'\t',data['login_id'],'\t',data['password'],'\t',data['dob'],'\t',data['address'],'\t')

def testread():
    list=model.read()
    for data in list:
        print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t',
              data['password'], '\t', data['dob'], '\t', data['address'], '\t')


testadd()
# testupdate()
# testdelete()
# testgetbyid()
# testgetbylogin_id()
# testsearch()
# testread()