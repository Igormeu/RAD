import tkinter as tk
from tkinter import ttk 
import sqlite3 as bd
from classes import AppBd 

db = AppBd()
db.openConection()
db.createTable()
db.insertDate("maça",1.67)
db.insertDate("Tomate",2.25)
db.updateDate(id=1,name="batata", price=5.30)
db.deleteDate(id=1)

Dados = db.selectAllDate()

print(Dados)

db.closeConection()

