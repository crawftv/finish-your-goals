from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.String, primary_key=True, unique=True)
    name =DB.Column(DB.String(30),nullable=False)
    tasks = DB.relationship("Task",backref='user',lazy=True)

class Task(DB.Model):
    id = DB.Column(DB.Integer,primary_key=True,unique=True)
    name = DB.Column(DB.String(50), nullable = False)
    monday = DB.Column(DB.Boolean,default=False)
    tuesday = DB.Column(DB.Boolean,default=False)
    wednesday = DB.Column(DB.Boolean,default=False)
    thursday = DB.Column(DB.Boolean,default=False)
    friday = DB.Column(DB.Boolean,default=False)
    saturday = DB.Column(DB.Boolean,default=False)
    sunday = DB.Column(DB.Boolean,default=False)
    start_time = DB.Column(DB.BigInteger,nullable=False)
    end_time = DB.Column(DB.BigInteger,nullable=False)
    interval = DB.Column(DB.Integer,nullable=False)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'),nullable=False) 


