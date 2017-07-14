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
@db_session
def agregarLista():
   todo_lists.nuevo(request.form.get('titulo'))
   return render_template("index.html",  lists=todo_lists.todas())

@app.route('/todo/borrar', methods=['POST'])
@db_session
def borrarLista():
    todo_lists.borrar(request.form.get('titulo'))
    return render_template("index.html",  lists=todo_lists.todas())

@app.route('/todo/<id>')
@db_session
def showTodos(id):
    return render_template("todos.html", todos=todo_lists.todosLosTodosDeLaLista(id))
