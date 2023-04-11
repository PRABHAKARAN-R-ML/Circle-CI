from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class carModel(db.Model):
    __tablename__ = "table"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    color = db.Column(db.String())
    price = db.Column(db.Integer())
 
    def __init__(self,id,name,color,price):
        self.id = id
        self.name = name
        self.color = color
        self.price = price
 
    def __repr__(self):
        return f"{self.name}:{self.color}"
