from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    files = db.relationship('UserFiles', backref='user', lazy=True)
class UserFiles(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_name = db.Column(db.String, nullable=False)
    file_path =db .Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def serialize(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'file_name':self.file_name,
            'file_path':self.file_path,
            'date':self.date
        }

