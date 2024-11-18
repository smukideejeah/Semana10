#archivo: items.py
#Grupo: 1
#Autores: Elmer Montoya, Elvis Aguilar, Rafael Argüello, Joseph Avilez
#Fecha de Modificación: 18/11/2024
#Versión de Python: 3.12
#IDE Usada: Visual Studio Code
#Ejecución: python main.py
#Descripción del Programa: Programa que permite la gestión de productos en una base de datos SQLite
#Descripción de la Clase: Esta clase se encarga de gestionar los productos en la base de datos
from db.database import Database
from dict.Item import Item
class Items:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def findById(self, code: int) -> Item | None:
        dat = self.db.select('select code, description, price from products where code = ?', [code])
        return Item(int(dat[0][0]), str(dat[0][1]), float(dat[0][2])) if len(dat) > 0 else None

    def findAll(self) -> list[Item]:
        data = self.db.select('select code, description, price from products', [])
        items = list[Item]()
        for item in data:
            items.append(Item(int(item[0]), str(item[1]), float(item[2])))
        return items

    def create(self, item: Item) -> int:
        return self.db.insert('insert into products (description, price) values (?,?)', [item.description, item.price])

    def update(self, item) -> int:
        return self.db.update('update products set description = ?, price = ? where code = ?', [item.description, item.price, item.code])

    def delete(self, id) -> int:
        return self.db.delete('delete from products where code = ?', [id])