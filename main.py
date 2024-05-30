import model

host = 'localhost'
port = '5432'
username = 'postgres'
password = 'ouji'
dbname = 'matkul'

db = model.model(host=host,port=port,username=username,password=password,dbname=dbname)
table = db.get_tablename(table="employees")
tables = db.getall_tablename()


values = ['Semester 6']
db.create_data(table='semester',values=values)