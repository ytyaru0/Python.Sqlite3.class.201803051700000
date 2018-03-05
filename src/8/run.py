from db.Service import Service
if __name__ == '__main__':
    # CREATE TABLE
    Service().Main.Initialize()
    # INSERT, DELETE
    id1 = Service().Main.Add('http://1', 'memo1')
    id2 = Service().Main.Add('http://2', 'memo2')
    id3 = Service().Main.Add('http://3', 'memo3')
    Service().Main.Remove(id2)
    # SELECT
    for record in Service().Main.Gets():
        print(record)
