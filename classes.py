from asyncio import open_connection
import sqlite3 as sq
class AppBd ():
    def openConection (self):
        try:
            self.conection = sq.connect("product.db")
            self.conection.execute("PRAGMA foreign_keys=ON")
            self.cursor = self.conection.cursor()
        except sq.Error as e:
            print("Falha ao se connectar ao bd", e)
    def createTable(self):
        createQuery = '''CREATE TABLE IF NOT EXIST product (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL NOT NULL);'''

        try:
            self.cursor.execute(createQuery)
            print("A criação da tabela product ocorreu com sucesso")
        except sq.Error as e:
            print("Falha ao criar a tabela product ao bd", e)
        finally:
            if self.conection:
                self.conection.commit()
                
    def insertDate (self, name, price):
        insertionQuery = '''INSERT INTO products (name, price) VALUES (?,?)'''
        try:   
            self.cursor.execute(insertionQuery,(name,price))
            print("Linha inserida com sucesso na tabela products")
        except sq.Error as e:
            print("Falha ao unserir um item na tabela products do bd", e)
        finally:
            if self.conection:
                self.conection.commit()