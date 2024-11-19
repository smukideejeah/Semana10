#archivo: mainForm.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Descripción del Programa: Programa que permite la gestión de productos en una base de datos SQLite
#Descripción de la Clase: Esta clase se encarga de desplegar la interfaz gráfica de usuario
from tkinter import END, StringVar, Tk, messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Button, Entry, Frame, Label, LabelFrame, Notebook
from dict.Item import Item
from db.items import Items

class MainForm:
    def __init__(self, items: Items):
        self.items = items
        self.main = Tk()
        self.main.resizable(False, False)
        self.codeData = StringVar()
        self.descriptionData = StringVar()
        self.priceData = StringVar()
        self.main.title("Gestor de Artículos")
        self.book = Notebook(self.main)
        self.book.bind("<<NotebookTabChanged>>", self.sheetSelected)
        self.addItemsTab()
        self.getByCodeTab()
        self.getAllItemsTab()
        self.deleteItemTab()
        self.updateItemTab()
        self.book.grid(row=0, column=0, padx=10, pady=10)
        self.main.mainloop()

    def sheetSelected(self, event):
        self.descriptionData.set("")
        self.priceData.set("")
        self.codeData.set("")
        self.scrolledText.delete("1.0", END)


    def addItemsTab(self):
        self.sheet1 = Frame(self.book)
        
        self.book.add(self.sheet1, text="Nuevo Artículo")
        self.frameSheet1 = LabelFrame(self.sheet1, text="Datos del Artículo")
        self.frameSheet1.grid(row=0, column=0, padx=5, pady=10)
        self.labelSheet1 = Label(self.frameSheet1, text="Nombre del Artículo")
        self.labelSheet1.grid(row=0, column=0, padx=4, pady=4)
        
        self.entryDescription = Entry(self.frameSheet1, textvariable=self.descriptionData)
        self.entryDescription.grid(row=0, column=1, padx=4, pady=4)
        self.labelSheet2 = Label(self.frameSheet1, text="Precio del Artículo")
        self.labelSheet2.grid(row=1, column=0, padx=4, pady=4)
        
        self.entryPrice = Entry(self.frameSheet1, textvariable=self.priceData)
        self.entryPrice.grid(row=1, column=1, padx=4, pady=4)
        self.buttonSheet1 = Button(self.frameSheet1, text="Guardar Artículo", command=self.addItems)
        self.buttonSheet1.grid(row=2, column=1, padx=4, pady=4)

    def addItems(self):
        description = self.descriptionData.get()
        price = self.priceData.get()
        item = Item(0, description, float(price))
        lastId = self.items.create(item);
        self.descriptionData.set("")
        self.priceData.set("") 
        messagebox.showinfo("Información", "Artículo guardado con éxito. ID: " + str(lastId))

    def getByCodeTab(self):
        self.sheet2 = Frame(self.book)
        self.book.add(self.sheet2, text="Buscar Artículo por Código")
        self.frameSheet2 = LabelFrame(self.sheet2, text="Datos del Artículo")
        self.frameSheet2.grid(row=0, column=0, padx=5, pady=10)
        self.labelSheet1 = Label(self.frameSheet2, text="Código del Artículo:")
        self.labelSheet1.grid(row=0, column=0, padx=4, pady=4)
        
        self.entryCode = Entry(self.frameSheet2, textvariable=self.codeData)
        self.entryCode.grid(row=0, column=1, padx=4, pady=4)
        self.labelSheet2 = Label(self.frameSheet2, text="Nombre del Artículo:")
        self.labelSheet2.grid(row=1, column=0, padx=4, pady=4)
        self.entryDescription = Entry(self.frameSheet2, state="readonly", textvariable=self.descriptionData)
        self.entryDescription.grid(row=1, column=1, padx=4, pady=4)
        self.labelSheet3 = Label(self.frameSheet2, text="Precio del Artículo:")
        self.labelSheet3.grid(row=2, column=0, padx=4, pady=4)
        self.entryPrice = Entry(self.frameSheet2, textvariable=self.priceData , state="readonly")
        self.entryPrice.grid(row=2, column=1, padx=4, pady=4)
        self.buttonSheet2 = Button(self.frameSheet2, text="Buscar Artículo", command=self.getByCode)
        self.buttonSheet2.grid(row=3, column=1, padx=4, pady=4)

    def getByCode(self):
        code = self.codeData.get()
        item = self.items.findById(int(code))
        if item is not None:
            self.descriptionData.set(item.description)
            self.priceData.set(item.price)
        else:
            self.descriptionData.set("")
            self.priceData.set("")
            messagebox.showerror("Error", "Artículo no encontrado")

    def getAllItemsTab(self):
        self.sheet3 = Frame(self.book)
        self.book.add(self.sheet3, text="Listado de Artículos")
        self.frameSheet3 = LabelFrame(self.sheet3, text="Artículos")
        self.frameSheet3.grid(row=0, column=0, padx=5, pady=10)
        self.buttonSheet3 = Button(self.frameSheet3, text="Listar Artículos", command=self.getAllItems)
        self.buttonSheet3.grid(row=0, column=0, padx=4, pady=4)
        self.scrolledText = ScrolledText(self.frameSheet3, width=50, height=10)
        self.scrolledText.grid(row=1, column=0, padx=10, pady=10)

    def getAllItems(self):
        items = self.items.findAll()
        self.scrolledText.delete("1.0", END)
        for item in items:
            self.scrolledText.insert(END, f"Código: {item.code} - Nombre: {item.description} - Precio: {item.price}\n")

    def deleteItemTab(self):
        self.sheet4 = Frame(self.book)
        self.book.add(self.sheet4, text="Eliminar Artículo")
        self.frameSheet4 = LabelFrame(self.sheet4, text="Datos del Artículo")
        self.frameSheet4.grid(row=0, column=0, padx=5, pady=10)
        self.labelSheet1 = Label(self.frameSheet4, text="Código del Artículo:")
        self.labelSheet1.grid(row=0, column=0, padx=4, pady=4)
        self.entryCodeDelete = Entry(self.frameSheet4, textvariable=self.codeData)
        self.entryCodeDelete.grid(row=0, column=1, padx=4, pady=4)
        self.buttonSheet4 = Button(self.frameSheet4, text="Eliminar Artículo", command=self.deleteItem)
        self.buttonSheet4.grid(row=1, column=1, padx=4, pady=4)

    def deleteItem(self):
        code = self.codeData.get()
        rows = self.items.delete(int(code))
        if rows > 0:
            self.codeData.set("")
            messagebox.showinfo("Información", "Artículo eliminado con éxito")
        else:
            messagebox.showerror("Error", "Artículo no encontrado")

    def updateItemTab(self):
        self.sheet5 = Frame(self.book)
        self.book.add(self.sheet5, text="Actualizar Artículo")
        self.frameSheet5 = LabelFrame(self.sheet5, text="Datos del Artículo")
        self.frameSheet5.grid(row=0, column=0, padx=5, pady=10)
        self.labelSheet1 = Label(self.frameSheet5, text="Código del Artículo:")
        self.labelSheet1.grid(row=0, column=0, padx=4, pady=4)
        self.entryCode = Entry(self.frameSheet5, textvariable=self.codeData)
        self.entryCode.grid(row=0, column=1, padx=4, pady=4)
        self.labelSheet2 = Label(self.frameSheet5, text="Nombre del Artículo:")
        self.labelSheet2.grid(row=1, column=0, padx=4, pady=4)
        self.entryDescription = Entry(self.frameSheet5, textvariable=self.descriptionData)
        self.entryDescription.grid(row=1, column=1, padx=4, pady=4)
        self.labelSheet3 = Label(self.frameSheet5, text="Precio del Artículo:")
        self.labelSheet3.grid(row=2, column=0, padx=4, pady=4)
        self.entryPrice = Entry(self.frameSheet5, textvariable=self.priceData)
        self.entryPrice.grid(row=2, column=1, padx=4, pady=4)

        self.buttonSheet5 = Button(self.frameSheet5, text="Consutar", command=self.getByCode)
        self.buttonSheet5.grid(row=3, column=0, padx=4, pady=4)
        self.buttonSheet6 = Button(self.frameSheet5, text="Actualizar Artículo", command=self.updateItem)
        self.buttonSheet6.grid(row=3, column=1, padx=4, pady=4)

    def updateItem(self):
        code = self.codeData.get()
        description = self.descriptionData.get()
        price = self.priceData.get()
        item = Item(int(code), description, float(price))
        rows = self.items.update(item)
        if rows > 0:
            self.codeData.set("")
            self.descriptionData.set("")
            self.priceData.set("")
            messagebox.showinfo("Información", "Artículo actualizado con éxito")
        else:
            messagebox.showinfo("Información", "Artículo no encontrado")