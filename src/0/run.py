from Transactioner import Transactioner


class TestDbInitializer:
    #def __init__(self):
    #    self.__t = Transactioner('sqlite:///../res/test.db')
    #    self.__t.Execute()
    #@t.Execute
    #@transact('sqlite:///../res/test.db')
    def initialize(self, db, *args, **kwargs):
        print('TestDbInitializer.initialize()')
        print(self)
        print(db)
        print(args)
        print(kwargs)
        db.query('select 1')
        print(dir(db))
        print(db.tables)

        if 0 == len(db.tables): db.query("create table MyDb (Id integer, Name text);")
        db.query("select * from MyDb;")

        _id = db.query('select count(*) as count from MyDb').next()['count']
        print(_id)
        db.query("insert into MyDb (Id,Name) values ({},'{}')".format(_id, 'Run'))

        print(db['MyDb'].find())


initer = TestDbInitializer()

t = Transactioner('sqlite:///../res/test.db')
t.Execute(initer)

#TestDbInitializer().initialize()

"""
@t.Execute
#@transact('sqlite:///../res/test.db')
def initialize_db(db):
    db.query('select 1')
    print(db.tables)

    if 0 == len(db.tables): db.query("create table MyDb (Id integer, Name text);")
    db.query("select * from MyDb;")

    _id = db.query('select count(*) as count from MyDb').next()['count']
    print(_id)
    db.query("insert into MyDb (Id,Name) values ({},'{}')".format(_id, 'Run'))

    print(db['MyDb'].find())

# 実行！　引数db不要！
initialize_db()
"""

