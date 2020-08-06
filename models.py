from api import app
from flask_sqlalchemy import SQLAlchemy

# init a db
db = SQLAlchemy(app)

# widget model
class Widget(db.Model):
  __tablename__='widgets'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  wodgets = db.Column(db.Integer)
  quantity = db.Column(db.Integer)

  def as_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'wodgets': self.wodgets,
      'quantity': self.quantity
    }

  def __repr__(self):
    return f'👾 Widget\nid: {self.id}\nname: {self.name}\nwodgets: {self.wodgets}\nquantity:{self.quantity}'


