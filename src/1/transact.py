import functools
import dataset

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
