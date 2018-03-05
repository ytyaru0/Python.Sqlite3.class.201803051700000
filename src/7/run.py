from db.Accesser import Accesser
if __name__ == '__main__':
    table_name = 'MyTable'
    nt = {'Id': 'integer', 'Name': 'text'}
    Accesser().MyDb.CreateTable(table_name, **nt)
    nv = {'Id': 0, 'Name': 'A'}
    Accesser().MyDb.Insert(table_name, **nv)

