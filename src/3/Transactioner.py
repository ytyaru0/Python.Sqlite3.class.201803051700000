from threading import Thread, Lock
import functools
import dataset
from Singleton import Singleton

class Transactioner(metaclass=Singleton):
    def __init__(self, db_url, *dataset_args, **dataset_kwargs):
        self.__db_url = db_url
        self.__dataset_args = dataset_args
        self.__dataset_kwargs = dataset_kwargs
        self.__target_class = None
        self.__lock = Lock()

    def transact(self):
        print('self:', self)
        def transact(target_class):
            print('target_class:', target_class)
            def transact(func):
                print('func:', func)
                import functools
                @functools.wraps(func)
                def wrapper(*args, **kwargs):
                    print('args:', args)
                    print('kwargs:', kwargs)
                    print('db_url:', self.__db_url)
                    print('dataset_args:', self.__dataset_args)
                    print('dataset_kwargs:', self.__dataset_kwargs)
                    with self.__lock:
                        with dataset.connect(self.__db_url, self.__dataset_args, self.__dataset_kwargs) as db:
                            db.begin()
                            res = func(self.__target_class, db, *args, **kwargs)
                            db.commit()
                            return res
                return wrapper
            return transact
        return transact

    @property
    def target_class(self): return self.__target_class
    @target_class.setter
    def target_class(self, v):
        self.__target_class = v

    """
    def transact(self):
        def _transact(func):
            import functools
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('self:', self)
                print('func:', func)
                print('args:', args)
                print('kwargs:', kwargs)
                print('db_url:', self.__db_url)
                print('dataset_args:', self.__dataset_args)
                print('dataset_kwargs:', self.__dataset_kwargs)
                with self.__lock:
                    with dataset.connect(self.__db_url, self.__dataset_args, self.__dataset_kwargs) as db:
                        db.begin()
                        res = func(db, *args, **kwargs)
                        db.commit()
                        return res
            return wrapper
        return _transact
    """

    """
    def transact(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            #print(self)
            #print(func)
            print(args)
            print(kwargs)
            print('db_url:', self.__db_url)
            print('dataset_args:', self.__dataset_args)
            print('dataset_kwargs:', self.__dataset_kwargs)
            with self.__lock:
                with dataset.connect(self.__db_url, self.__dataset_args, self.__dataset_kwargs) as db:
                    db.begin()
                    res = func(cls, db, *args, **kwargs)
                    db.commit()
                    return res
        return wrapper
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
