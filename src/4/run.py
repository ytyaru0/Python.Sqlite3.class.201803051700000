from Transactioner import Transactioner

if __name__ == '__main__':
    def CreateTable(db, table_name, **name_types):
        if table_name in db.tables: DropTable(db, table_name)
        columns = ', '.join(k+' '+v for k,v in name_types.items())
        sql = f'create table {table_name} ({columns});'
        print(sql)
        db.query(sql)
    def DropTable(db, table_name):
        sql = f'drop table {table_name};'
        print(sql)
        db.query(sql)
    def Insert(db, table_name, **kv):
        columns = ','.join([k for k in kv.keys()])
        values = ','.join(GetInsertValues(kv.values()))
        sql = f'insert into {table_name} ({columns}) values ({values});'
        print(sql)
        db.query(sql)
    def GetInsertValues(values):
        vals = []
        for v in values:
            if isinstance(v, int): vals.append(str(v))
            else: vals.append(f"'{v}'")
        return vals

    t = Transactioner()
    t.DbUrl = 'sqlite:///test.db'

    t.TransactionMethod = CreateTable
    nt = {'Id': 'integer', 'Name': 'text'}
    t.Transact('MyTable', **nt)

    t.TransactionMethod = Insert
    nv = {'Id': 0, 'Name': 'A'}
    t.Transact('MyTable', **nv)
