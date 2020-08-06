from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from crud.widget_crud import *

# initialize flask app
app = Flask(__name__)

# config app wtih db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask_widgets'

# import CRUD functions after db is set up
from crud.widget_crud import *

# ROUTES

# test route
@app.route('/')
def home():
  return jsonify({ 'message': 'Hello, World!' })

# GET : READ all widgets/POST : CREATE new widget
@app.route('/widgets', methods=['GET', 'POST'])
def all_widgets():
    if request.method == 'GET': 
      return get_all_widgets()
    if request.method == 'POST': 
      create_widget(request.form['name'], request.form['wodgets'], request.form['quantity'])
      return redirect('/widgets')

#GET : READ one widget/PUT : UPDATE one widget /DELETE : DESTROY one widget
@app.route('/widget/<id>', methods=['GET', 'PUT', 'DELETE'])
def detail_widget(id):
    if request.method == 'GET': 
      return get_widget(id)
    if request.method == 'PUT': 
      return update_widget(id, request.form['name'], request.form['wodgets'], request.form['quantity'])
    if request.method == 'DELETE': 
      return destroy_widget(id)
