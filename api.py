from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from crud.widget_crud import *

test_print_1(123)
test_print_2(213542345)

# import models when they are created

# initialize flask app
app = Flask(__name__)

# config app wtih db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql'

# ROUTES

# test route
@app.route('/')
def home():
  return jsonify({ 'message': 'Hello, World!' })

# GET : READ all widgets/POST : CREATE new widget
@app.route('/widgets', methods=['GET', 'POST'])
def all_widgets():
    if request.method == 'GET': 
      return jsonify({ 'message': 'READ all widgets' })
    if request.method == 'POST': 
      return jsonify({ 'message': 'CREATE new widget' })

#GET : READ one widget/PUT : UPDATE one widget 
@app.route('/widget/<id>', methods=['GET', 'POST', 'DELETE'])
def detail_widget(id):
    if request.method == 'GET': 
      return jsonify({ 'message': f'READ one widget at id {id}' })
    if request.method == 'POST': 
      return jsonify({ 'message': f'UPDATE one widget at id {id}' })
    if request.method == 'DELETE': 
      return jsonify({ 'message': f'DELETE one widget at id {id}' })



    