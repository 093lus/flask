from flask import jsonify, request
from flask_restful import Resource, Api

from app import app, db
from app.models import User
from app.schema import users_schema
from flask_restful import reqparse

parser = reqparse.RequestParser()


class UserResource(Resource):

    def get(self):
        users = User.query.order_by(User.age).all()
        result = users_schema.dump(users)
        return jsonify(result.data)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('age', type=int)
        parser.add_argument('occupation', type=str)
        args = parser.parse_args()
        user = User(name=args.get("name", ''), age=args.get("age", ''), occupation=args.get("occupation", ''))
        db.session.add(user)
        db.session.commit()
        return 'ok'

    def delete(self):
        parser.add_argument('age', type=int)
        args = parser.parse_args()
        try:
            age = args["age"]
        except KeyError as e:
            return 'Pleas pass age', 400
        User.query.filter(User.age > age).delete()
        db.session.commit()
        return 'ok'


class UserResourceByName(Resource):
    def get(self, name):
        db.session.query(User).filter_by(name=name).update({'counter': User.counter + 1})
        db.session.commit()
        return 'ok'
