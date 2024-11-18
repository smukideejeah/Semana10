#archivo: main.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Descripción del Programa: Programa que permite la gestión de productos en una base de datos SQLite
#Descripción del archivo: Este archivo es el punto de entrada del programa, se encarga de crear la instancia de la clase MainForm, de la clase Items y de crear la tabla en la base de datos
from UI.mainForm import MainForm
from db.items import Items

items = Items()

items.db.createTableIfNotExists()

form = MainForm(items)

