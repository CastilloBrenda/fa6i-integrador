from flask import render_template, request, redirect, url_for
from pony.orm import *
from src import app

from src.models.todo_list import *

@app.route('/')
@app.route('/todo/agregar', methods=['GET'])
@app.route('/todo/borrar', methods=['GET'])
@db_session
def home():
    return render_template("index.html",  lists=todo_lists.todas())

@app.route('/todo/agregar', methods=['POST'])
def agregarLista():
    return "TODO"

@app.route('/todo/<id>')
@db_session
def showTodos(id):
    return render_template("todos.html", todos=todo_list.todosLosTodosDeLaLista(id))
