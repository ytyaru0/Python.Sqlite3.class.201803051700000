#from abc import ABCMeta, abstract
from Transactioner import Transactioner

class MyDbTransactionerMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['T'] = Transactioner('sqlite:///mydb.db')
        return type.__new__(cls, name, bases, attrs)
    def __init__(cls, name, bases, attrs):
        cls.T.target_class = cls

