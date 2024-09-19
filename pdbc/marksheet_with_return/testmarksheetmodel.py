from MarksheetModel import MarksheetModel

model = MarksheetModel()


def testadd():
    param = {'roll_no': 108, 'name': 'divya', 'physics': 82, 'chemistry': 66, 'maths': 75}
    model = MarksheetModel()
    model.add(param)


def tesupdate():
    param = {'name': 'divyanshi', 'id': 8}
    model.update(param)


def testdelete():
    model.delete(8)


def testgetbyid():
    list = model.getbyid(8)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'], '\t', data['maths'])

def testgetbyroll():
    list = model.getbyid(7)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'], '\t', data['maths'])

def testread():
    list=model.read()
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],'\t', data['maths'])


def testsearch():
    param={'pagesize':3}
    list=model.search(param)
    print(list)
    for data in list:
        print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],'\t', data['maths'])


# testadd()
# tesupdate()
# testdelete()
# testgetbyid()
# testgetbyroll()
# testread()
testsearch()