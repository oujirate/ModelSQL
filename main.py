import model

host = 'localhost'
port = '5432'
username = 'postgres'
password = 'ouji'
dbname = 'nortwind'

db = model.sqlmodel(host=host,port=port,username=username,password=password,dbname=dbname)
# tables = db.getall_tablename()


# values = ['Semester 6']
# db.create_data(table='semester',values=values)

# db.read_data(select="order_id,first_name,order_date,company_name",table="orders",join="employees,customers")

print(db.getall_tablename())
# print(db.auth_columntable(table="employees",column="   birth_date   ")

# db.read_data()
# db.update_data(table="semester",idcolumn="5",values=["Semester 55"])