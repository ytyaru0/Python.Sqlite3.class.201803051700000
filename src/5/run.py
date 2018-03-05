from TransactionSetter import TransactionSetter
from MyDbTransactioner import MyDbTransactioner
if __name__ == '__main__':
    mydb = MyDbTransactioner()
    s = TransactionSetter()
    accesser = s.Set(mydb)
    print(dir(accesser))

    table_name = 'MyTable'
    nt = {'Id': 'integer', 'Name': 'text'}
    accesser.CreateTable(table_name, **nt)
    nv = {'Id': 0, 'Name': 'A'}
    accesser.Insert(table_name, **nv)

