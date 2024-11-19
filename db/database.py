#archivo: database.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Descripción del Programa: Programa que permite la gestión de productos en una base de datos SQLite
#Descripción de la Clase: Esta clase se encarga de la conexión a la base de datos y de realizar las operaciones de insert, update, delete y select.
import sys
import mariadb
import env
class Database:
    def connect(self):
        
        # with sqlite3.connect('data/database.db') as conn:
        #     self.conn = conn
        #     return conn

        try:
            connection = mariadb.connect(
            user = env.DBUSER,
            password = env.DBPASS,
            host = env.DBHOST,
            port = env.DBPORT,
            database = env.DBPORT)
            
            # Get Cursor
            cursor = connection.cursor()
            print("Connected to MariaDB Platform")
            self.conn = connection
            self.cursor = cursor

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        
    def close(self):
        self.conn.close()


    def select(self, query: str, params: list):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def insert(self, query: str, params: list):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.lastrowid
    
    def update(self, query: str, params: list):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.rowcount
    
    def delete(self, query: str, params: list):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor.rowcount
    
    def createTableIfNotExists(self):
        self.conn.cursor().execute('''
            create table if not exists products (
                code int primary key auto_increment not null,
                description text,
                price float
            )
        ''')
        self.conn.commit()