import dataset
import types

class Transactioner:
    def __init__(self):
        self.__transaction = None
        self.__dataset_kwargs = None

    def Transact(self, *args, **kwargs):
        dbs = {}
        for key in self.__dataset_kwargs:
            dbs[key] = dataset.connect(**self.__dataset_kwargs[key])
            dbs[key].begin()
        res = self.__transaction(dbs, *args, **kwargs)
        for key in self.__dataset_kwargs:
            dbs[key].commit()
        for key in self.__dataset_kwargs:
            dbs[key].engine.dispose()
            del dbs[key]
        return res

    @property
    def TransactionMethod(self): return self.__transaction
    @TransactionMethod.setter
    def TransactionMethod(self, v):
        if v is None: return
        if isinstance(v, types.MethodType): self.__transaction = v
        else: raise Exception('メソッドを指定してください。第一引数は{"name": dataset.Database, ...}です。（他の引数は任意）')

    @property
    def DatasetArgs(self): return self.__dataset_kwargs
    @DatasetArgs.setter
    def DatasetArgs(self, v):
        if v is None: return
        if isinstance(v, dict): self.__dataset_kwargs = v
        else: raise Exception('dictを指定してください。dataset.connect()のキーワード引数になります。')

