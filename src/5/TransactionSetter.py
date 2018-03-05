import inspect
import types
from Transactioner import Transactioner

class TransactionSetter:
    def Set(self, target_class):
        attrs = {}
        # target_classの自作公開メソッドをすべて取得
        for method_info in inspect.getmembers(target_class, inspect.ismethod):
            method_name = method_info[0]
            method = method_info[1]
            if not isinstance(method, types.MethodType): continue
            if method_name.startswith('_'): continue
            print(method_name, type(method_name))
            t = Transactioner()
            t.TransactionMethod = method
            t.DbUrl = target_class.DbUrl
            t.DbKwargs = target_class.DbKwargs
            attrs[method_name] = t.Transact
        accesserType = type(target_class.__class__.__name__ + 'Accesser', (object,), attrs)
        return accesserType()

