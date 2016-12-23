from pony.orm import *
from src import db


class TodoList(db.Entity):
    id = PrimaryKey(int, auto=True)
    titulo = Optional(str)
    todos = Optional('Todo')

class TodoListService():
    def nuevo(self, titulo, todos = []):
        return TodoList(titulo=titulo, todos=todos)
    def marcarTodasComoTerminadas(self):
        pass
    def todas(self):
        return select(e for e in TodoList)
    def todosLosTodosDeLaLista(self, id):
        return TodoList[id].todos

todo_lists = TodoListService()
