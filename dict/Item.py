#archivo: Item.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Descripción del Programa: Programa que permite la gestión de productos en una base de datos SQLite
#Descripción de la Clase: Esta clase se encarga de describir un producto
class Item:
    def __init__(self, code: int, description: str, price: float):
        self.code = code
        self.description = description
        self.price = price