from MyDbTransactioner import MyDbTransactioner

#mydb = MyDbTransactioner('sqlite:///mydb.db')
mydb = MyDbTransactioner()
table_name = 'MyTable'
nt = {'Id':'integer','Name':'text'}
mydb.CreateTable(table_name, **nt)
nv = {'Id':0,'Name':'A'}
mydb.Insert(table_name, **nv)

