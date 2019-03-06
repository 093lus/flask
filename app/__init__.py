import os, sys


from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)


def init_db():
    users = [
        {
            "name": "Kamil",
            "age": 42,
            "occupation": "Network Engineer"
        },
        {
            "name": "Jakub",
            "age": 32,
            "occupation": "Doctor"
        },
        {
            "name": "Michal",
            "age": 22,
            "occupation": "Web Developer"
        }
    ]
    from app.models import User
    db.drop_all()
    db.create_all()
    db.session.query(User).delete()
    for u in users:
        user = User(name=u["name"],age=u["age"], occupation=u["occupation"])
        db.session.add(user)
    db.session.commit()


api = Api(app)
from app.resources import UserResource, UserResourceByName

api.add_resource(UserResource, "/user")
api.add_resource(UserResourceByName, "/user/<name>")
init_db()
app.run(host="127.0.0.1", port=8000)