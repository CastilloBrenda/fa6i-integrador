from pony.orm import *
from src import db
from datetime import *

class Todo(db.Entity):
    id = PrimaryKey(int, auto=True)
    descripcion = Optional(str)
    vencimiento = Optional(datetime, 6)
    terminado = Required(bool, default=False)
    lista = Required('TodoList')

class TodoService():
    def nuevo(self, descripcion, vencimiento):
        return Todo(descripcion=descripcion, vencimiento=vencimiento)
    def marcarHecho(self, id):
        pass
    def todos(self):
        return select(e for e in Todo)

todos = TodoService()
