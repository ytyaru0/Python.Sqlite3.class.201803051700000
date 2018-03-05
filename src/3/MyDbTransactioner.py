from MyDbTransactionerMeta import MyDbTransactionerMeta
#from Transactioner import Transactioner

class MyDbTransactioner(metaclass=MyDbTransactionerMeta):
    #T = Transactioner('sqlite:///mydb.db')
    
    @T.transact()
    def CreateTable(self, db, table_name, **name_types):
        columns = ', '.join(k+' '+v for k,v in name_types.items())
        sql = f'create table {table_name} ({columns});'
        Log().debug(sql)
        db.query(sql)

    @T.transact()
    #@transact
    def Insert(self, db, table_name, **kv):
        columns = ','.join([k for k in kv.keys()])
        values = ','.join(cls.__GetInsertValues(kv.values()))
        sql = f'insert into {table_name} ({columns}) values ({values});'
        Log().debug(sql)
        db.query(sql)

    def __GetInsertValues(self, values):
        values = []
        for v in values:
            if isinstance(v, int): values.append(str(v))
            else: values.append(f"'{v}'")
        return values
    """
    @classmethod
    def __GetInsertValues(cls, values):
        values = []
        for v in values:
            if isinstance(v, int): values.append(str(v))
            else: values.append(f"'{v}'")
        return values
    """
    """
    def Execute(self, runner, *args, **kwargs):
        with self.__lock:
            with dataset.connect(self.__db_url, self.__dataset_args, self.__dataset_kwargs) as db:
                print(self.__db_url)
                print(self.__dataset_args)
                print(self.__dataset_kwargs)
                print(runner)
                #print(func)
                db.begin()
                res = runner.initialize(db, *args, **kwargs)
                #res = self.func(db, *args, **kwargs)
                db.commit()
                return res
    """

"""
def transact(db_url):
    def transact(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('db_url:', db_url)
            print('args:', args)
            print('kwargs:', kwargs)
            with dataset.connect(db_url) as db:
                db.begin()
                res = func(db, *args, **kwargs)
                db.commit()
                return res
        return wrapper
    return transact
"""
"""
def transact(some_func):
    import functools
    @functools.wraps(some_func)
    def wrapper(*args,**kwargs):
        con.begin()
        res = some_func(*args, **kwargs)
        con.commit()
        return res
    return wrapper
"""

"""
def connect(func):
#def connect(transact):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('args:', args)
        print('kwargs:', kwargs)
        with dataset.connect(args[0]) as db:
            return transact(*args, **kwargs)
            #return func(db, **kwargs)
    return wrapper
    
def transact(some_func):
    import functools
    @functools.wraps(some_func)
    def wrapper(*args,**kwargs):
        con.begin()
        res = some_func(*args, **kwargs)
        con.commit()
        return res
    return wrapper
"""
