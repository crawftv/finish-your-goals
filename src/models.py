from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.String, primary_key=True, unique=True)
    name =DB.Column(DB.String(30),nullable=False)
