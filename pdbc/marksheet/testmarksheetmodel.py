from MarksheetModel import MarksheetModel


def testadd():
    param = {'id': 8, 'roll_no': 108, 'name': 'gautam', 'physics': 65, 'chemistry': 45, 'maths': 30}
    m = MarksheetModel()
    m.add(param)


def testupdate():
    param = {'name':'goutam','id':8}
    m = MarksheetModel()
    m.update(param)

def testdelete():
    param={'id':8}
    m = MarksheetModel()
    m.delete(param)

def testgetbyid():
    param={'id':6}
    m=MarksheetModel()
    m.getbyid(param)

def testsearch():
    param={'pagesize':3,'pageNo':2}
    m = MarksheetModel()
    m.search(param)


# testadd()
# testupdate()
# testdelete()
# testgetbyid()
testsearch()