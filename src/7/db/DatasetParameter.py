class DatasetParameter:
    def __init__(self, db_url, **dataset_kwargs):
        self.db_url = db_url
        self.dataset_kwargs = dataset_kwargs
    @property
    def DbUrl(self): return self.db_url
    @property
    def DbKwargs(self): return self.dataset_kwargs
