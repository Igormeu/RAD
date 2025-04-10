import tkinter as tk
from tkinter import ttk 
import sqlite3 as bd
import classes as cls



#Integrar a janela aos modeulos criados
class aplication():
    def __init__(self, master=None):
        self.modulo = cls.AppBd()
        self.window = master
        self.treeProduct = ttk.Treeview(self.window, columns=("Código", "Nome", "Preço"))
        self.treeProduct.heading('Código',text="ID")
        self.treeProduct.heading('Nome',text="Nome")
        self.treeProduct.heading('Preço',text="Preço")
        self.treeProduct.pack()
        self.labelName = tk.Label(self.window, text="Nome: ")
        self.labelName.pack()
        self.entryName = tk.Entry(self.window)
        self.entryName.pack()
        self.labelPrice = tk.Label(self.window, text="Preço: ")
        self.labelPrice.pack()
        self.entryPrice = tk.Entry(self.window)
        self.entryPrice.pack()

    def registerProduct (self):
        name = self.entryName.get()
        price = self.entryPrice.get()
        try:
            price = float(price)
        except:
            price = 0
        
        self.modulo.insertDate(name,price)
        
        
#criar janela princiopal
window = tk.Tk()

root = aplication(window)

#Customizar janela principal
window.title("Janela principal")
window.geometry("1200x900")
window.mainloop()



#db = AppBd()
#b.insertDate("maça",1.67)
#db.insertDate("Tomate",2.25)
#db.updateDate(id=1,name="batata", price=5.30)
#db.deleteDate(id=1)

#Dados = db.selectAllDate()

#db.closeConection()

