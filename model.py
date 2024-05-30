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
            print(f"[ Koneksi ke Database Gagal! Error: {ex} ]")

    def close(self):
        if self.conn is not None and self.cur is not None:
            try:
                self.cur.close()
                self.conn.close()
            except OperationalError as ex:
                print(f"Gagal Menutup Koneksi! Error: {ex}")
        else:
            print("[ Tidak ada koneksi yang ditutup! ]")
    
    def version(self):
        try:
            self.connect()
            self.cur.execute("SELECT version();")
            version = self.cur.fetchone()
            print(f"Versi PostgreSQL: {version[0]}")

        except OperationalError as ex:
            print(f"[ Error: {ex} ]")
        finally:
            self.close()
    
    def create_data(self):
        pass

    def read_data(self):
        pass

    def update_data(self):
        pass

    def delete_column(self):
        pass