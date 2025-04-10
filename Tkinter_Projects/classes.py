import sqlite3 as sq

class AppBd():
    def __init__(self):
        self.openConection()
        self.createTable()

    def openConection(self):
        try:
            self.conection = sq.connect("product.db")
            self.conection.execute("PRAGMA foreign_keys=ON")
            self.cursor = self.conection.cursor()
        except sq.Error as e:
            print("Falha ao se conectar ao BD", e)
            self.conection = None

    def createTable(self):
        createQuery = '''CREATE TABLE IF NOT EXISTS product (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            price REAL NOT NULL
                          );'''
        try:
            self.cursor.execute(createQuery)
            print("A criação da tabela product ocorreu com sucesso")
        except sq.Error as e:
            print("Falha ao criar a tabela product no BD", e)
        finally:
            if self.conection:
                self.conection.commit()

    def insertDate(self, name, price):
        insertionQuery = '''INSERT INTO product (name, price) VALUES (?, ?)'''
        try:
            self.cursor.execute(insertionQuery, (name, price))
            print("Linha inserida com sucesso na tabela product")
        except sq.Error as e:
            print("Falha ao inserir um item na tabela product do database", e)
        finally:
            if self.conection:
                self.conection.commit()

    def selectAllDate(self):
        selectQuery = '''SELECT * FROM product'''
        productList = []
        try:
            self.cursor.execute(selectQuery)
            productList = self.cursor.fetchall()
            print("Listagem de produtos coletada com sucesso")
        except sq.Error as e:
            print("Falha ao buscar os itens da tabela product", e)
        return productList

    def updateDate(self, id, name, price):
        updateQuery = '''UPDATE product SET name = ?, price = ? WHERE id = ?'''
        try:
            self.cursor.execute(updateQuery, (name, price, id))
            print(f"Linha de id {id} foi atualizada com sucesso")
        except sq.Error as e:
            print(f"Falha ao modificar o registro de id {id}", e)
        finally:
            if self.conection:
                self.conection.commit()

    def deleteDate(self, id):
        deleteQuery = '''DELETE FROM product WHERE id = ?'''
        try:
            self.cursor.execute(deleteQuery, (id,))
            print(f"Linha de id {id} deletada com sucesso")
        except sq.Error as e:
            print(f"Falha ao deletar o item de id {id} na tabela product do BD", e)
        finally:
            if self.conection:
                self.conection.commit()

    def closeConection(self):
        try:
            self.cursor.close()
            self.conection.close()
            print("Conexão fechada com sucesso")
        except sq.Error as e:
            print(f"Não há nenhuma conexão para ser fechada. Error: {e}")
