import model

host = 'localhost'
port = '5432'
username = 'postgres'
password = 'ouji'
dbname = 'nortwind'

db = model.model(host=host,port=port,username=username,password=password,dbname=dbname)
db.version()