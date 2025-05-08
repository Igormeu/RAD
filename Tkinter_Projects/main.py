import tkinter as tk
from tkinter import ttk
import classes
class PrincipalBD():
    def __init__(self, win):
       self.objbd = classes.AppBd()
       self.janela = win

       self.treeProdutos = ttk.Treeview(self.janela,
                                        columns=("Código do produto",
                                           "Nome", 
                                           "Preco"))
       self.treeProdutos.heading("Código do produto", text= "Id: ")
       self.treeProdutos.heading("Nome", text="Nome: ")
       self.treeProdutos.heading("Preco", text="Preco: ")
       self.exibirProdutos()
       self.treeProdutos.pack() 

       self.nome = tk.Label(self.janela, text="Nome: ")
       self.nome.pack()
       self.entrynome = tk.Entry(self.janela)
       self.entrynome.pack()
       self.preco = tk.Label(self.janela,
                             text="Preco")
       self.preco.pack()
       self.entrypreco = tk.Entry(self.janela)
       self.entrypreco.pack()

       self.button = tk.Button(self.janela, text="Adicionar item", command=self.cadastrarProduto)

       self.button.pack()
       
       self.button_update = tk.Button(self.janela, text="Atualizar item", command=self.atualizarProdutos)

       self.button_update.pack()
       
       self.button_delete = tk.Button(self.janela, text="Excluir item", command=self.excluirProdutos)

       self.button_delete.pack()
    
    def exibirProdutos (self):
       try:
          for item in self.treeProdutos.get_children():
            self.treeProdutos.delete(item)
            # or self.treeProdutos.delete(* self.treeProdutos.get_children())
          products = self.objbd.selectAllDate()
          for product in products:
            self.treeProdutos.insert("", tk.END, values=product) 
       except:
          print("Não deu para exibir")
    def cadastrarProduto(self):
      try: 
         name = self.entrynome.get()
         price = float(self.entrypreco.get())
         self.objbd.insertDate(name, price)

         self.entrynome.delete(0,tk.END)
         self.entrypreco.delete(0,tk.END)
         self.exibirProdutos()
         print ("Item cadastrado com sucesso !")
      except Exception as e:
         print ("Erro ao cadastrar o item")
    def atualizarProdutos (self):
       try:
         selectedItem = self.treeProdutos.selection()
         print(selectedItem)
         item = self.treeProdutos.item(selectedItem)
         print(item)
         valores = item ['values']
         print(valores) 
         id = valores[0]
         print(id)
         name = self.entrynome.get()
         print(name)
         price = self.entrypreco.get()
         print (price)
         
         name = valores[1] if len(name) == 0 else name
         price = float(valores[2]) if price == "" else float(price)     
             
         self.objbd.updateDate(id=id, name=name, price=price)

         self.entrynome.delete(0,tk.END)
         self.entrypreco.delete(0,tk.END)
         
         self.exibirProdutos()
         
       except Exception as e:
          print(e)
    def excluirProdutos (self):
       try:
         selectedItem = self.treeProdutos.selection()
         item = self.treeProdutos.item(selectedItem)
         valores = item ['values']
         id = valores[0]
             
         self.objbd.deleteDate(id)
         
         self.exibirProdutos()
         
       except Exception as e:
          print(e)
janela = tk.Tk() #criar a janela principal
product_app = PrincipalBD(janela)
#janela.title("Bem vindo ao sistema de cadastro!!")
janela.geometry("900x700")
janela.mainloop() 
#apresentar janela, ate que o usuario feche
