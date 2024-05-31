import model

host = 'localhost'
port = '5432'
username = 'postgres'
password = 'ouji'
dbname = 'nortwind'

db = model.model(host=host,port=port,username=username,password=password,dbname=dbname)
table = db.get_tablename(table="employees")
tables = db.getall_tablename()


# values = ['Semester 6']
# db.create_data(table='semester',values=values)

db.read_data(select="order_id,first_name,company_name,order_date",table="orders",join="employees,customers")