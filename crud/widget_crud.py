# import from db for CRUD
from models import Widget, db
from flask import jsonify, redirect

# CRUD

def create_widget(name, wodgets, quantity):
  # TODO break if bad type
  wodgets = int(wodgets)
  quantity = int(quantity)
  widget = Widget(name=name, wodgets=wodgets, quantity=quantity)
  db.session.add(widget)
  db.session.commit()
  return widget

def get_all_widgets():
  all_widgets = Widget.query.all()
  if all_widgets:
    all_widgets = [widget.as_dict() for widget in all_widgets]
    return jsonify(all_widgets)
  else: return jsonify({ 'message': 'no widgets in db' })

def get_widget(id):
  widget = Widget.query.get(id)
  if widget: return jsonify(widget.as_dict())
  else: return jsonify({ 'message': f'no widget found at id {id}' })

def update_widget(id, name, wodgets, quantity):
  widget = Widget.query.get(id)
  if widget:
    widget.name = name or widget.name
    widget.wodgets = wodgets or widget.name
    widget.quantity = quantity or widget.quantity
    db.session.commit()
    return jsonify(widget.as_dict()) 
  else: return jsonify({ 'message': f'no widget found at id {id}' })

def destroy_widget(id):
  widget = Widget.query.get(id)
  if widget:
    db.session.delete(widget)
    db.session.commit()
    return redirect('/widgets')
  else: return jsonify({ 'message': f'no widget found at id {id}' })