class MainService:
    def __init__(self):
        # https://dataset.readthedocs.io/en/latest/api.html#connecting
        self.__dataset_kwargs = {'Urls':{'url': 'sqlite:///Urls.db'}, 'Memos':{'url': 'sqlite:///Memos.db'}}
    @property
    def DatasetArgs(self): return self.__dataset_kwargs
    def Initialize(self, dbs):
        for name in ['Urls', 'Memos']:
            if name in dbs[name].tables:
                dbs[name].query(f'DROP TABLE {name};')
        dbs['Urls'].query('CREATE TABLE Urls (Id integer PRIMARY KEY, Name text);')
        dbs['Memos'].query('CREATE TABLE Memos (Id integer PRIMARY KEY, UrlId NOT NULL, Memo text);')
    def Gets(self, dbs):
        dbs['Urls'].query('attach "{}" as _U;'.format(self.__GetDbPath(self.__dataset_kwargs['Urls']['url'])))
        dbs['Urls'].query('attach "{}" as _M;'.format(self.__GetDbPath(self.__dataset_kwargs['Memos']['url'])) )
        return dbs['Urls'].query('SELECT u.Id, u.Url, m.Memo FROM main.Urls u INNER JOIN _M.Memos m ON u.Id = m.UrlId;')
    def Add(self, dbs, url, memo):
        _id = dbs['Urls']['Urls'].insert({'Url': url})
        dbs['Memos']['Memos'].insert({'UrlId': _id, 'Memo': memo})
        return _id
    def Remove(self, dbs, id):
        dbs['Memos']['Memos'].delete(UrlId=id)
        dbs['Urls']['Urls'].delete(Id=id)

    def __GetDbPath(self, db_url): return db_url.replace('sqlite:///', '')
    """
    def __GetAlias(self, path):
        if not isinstance(path, pathlib.PurePath):
            path = pathlib.PurePath(path)
        return '_' + path.name[0]
    """

