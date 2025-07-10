from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    no_hp = db.Column(db.String(100), nullable=False)
