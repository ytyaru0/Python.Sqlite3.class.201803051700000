from threading import Thread, Lock
import functools
import dataset
from Singleton import Singleton

# http://momijiame.tumblr.com/post/38226755506/python-%E3%81%AE-threadinglock-%E3%82%92%E8%A9%A6%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B

class Transactioner(metaclass=Singleton):
#class Transactioner:
    def __init__(self, db_url, *dataset_args, **dataset_kwargs):
        self.__db_url = db_url
        self.__dataset_args = dataset_args
        self.__dataset_kwargs = dataset_kwargs
        self.__lock = Lock()

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
