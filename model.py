import psycopg2 as pg
from psycopg2 import OperationalError

class model:
    def __init__(self,host,port,username,password,dbname):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.dbname = dbname
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            connection_string = f"""host='{self.host}' port={self.port} user='{self.username}' 
            password='{self.password}' dbname='{self.dbname}'"""
            self.conn = pg.connect(connection_string)
            self.cur = self.conn.cursor()

        except OperationalError as ex:
            print(f"Connection Failed! Error: {ex}")

    def close(self):
        if self.conn is not None and self.cur is not None:
            try:
                self.cur.close()
                self.conn.close()
            except OperationalError as ex:
                print(f"Close Failed! Error: {ex}")
        else:
            print("Message: Connection Not Found!")
    
    def version(self):
        try:
            self.connect()
            self.cur.execute("SELECT version();")
            version = self.cur.fetchone()
            print(f"Versi PostgreSQL: {version[0]}")

        except OperationalError as ex:
            print(f"Error: {ex}")
        finally:
            self.close()

    def get_columndata(self,table,idenable=0):
        try:
            self.connect()
            column_data = []
            query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}' ORDER BY ordinal_position"
            self.cur.execute(query)
            column = self.cur.fetchall()
            if idenable == 1:
                for i in column:
                    column_data.extend(i)
            else:
                for i in column[1:]:
                    column_data.extend(i)
            return column_data
        
        except OperationalError as ex:
            print(f"Error: {ex}")

        finally:
            self.close()
    
    def getall_tablename(self):
        try:
            self.connect()
            table_name = []
            query = f"SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name"
            self.cur.execute(query)
            table = self.cur.fetchall()
            for i in table:
                table_name.extend(i)
            return table_name
        except OperationalError as ex:
            print(f"Error: {ex}")
        finally:
            self.close()

    def get_tablename(self,table):
        table_name = None
        tables = self.getall_tablename()
        for i in tables:
            if i == table:
                table_name = i
        return table_name

    def create_data(self,table,values):
        try:
            column = self.get_columndata(table=table)
            self.connect()
            query = f"INSERT INTO {table} ({','.join(column)}) VALUES ({','.join(['%s'] * len(values))})"
            self.cur.execute(query,values)
            self.conn.commit()
        except OperationalError as ex:
            print(f"Error: {ex}")
        finally:
            self.close()

    def read_data(self,select='*',table=None,join=None,where=None,groupby=None,having=None,orderby=None):
        query = ""
        if table:
            column = self.get_columndata(table=table)
            self.connect()
            if join:
                list_join = join.strip().split(",")
                if select != "*":
                    query = f"SELECT "
                    list_select = select.strip().split(",")
                    tables = [table]
                    if len(list_join) > 0:
                        for i in list_join:
                            tables.append(i)
                    else:
                        tables.append(join)

                    count = 1
                    for i in list_select:
                        list_format = [i]
                        for j in tables:
                            list_format.append(j)

                        str_table = ",".join("%s" for table in tables)

                        query_find = f"SELECT table_name FROM information_schema.columns WHERE column_name = %s AND table_name in ({str_table})"
                        self.cur.execute(query_find,tuple(list_format))
                        table = self.cur.fetchone()
                        if count == len(list_select):
                            query += f"{table[0]}.{i}"
                        else:
                            query += f"{table[0]}.{i}, "
                            count += 1
                
                    print(query)
                    exit()
                else:
                    query += f"SELECT * FROM {table} "
            if where:
                pass



            

    def update_data(self):
        pass

    def delete_data(self):
        pass
