from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    name = db.Column(db.String(80), nullable=False)
    occupation = db.Column(db.String(120), nullable=False)
    counter = db.Column(db.Integer, default=0)

    @property
    def serialize(self):
        """Return object data in serializeable format"""
        return {
            'id': self.id,
            'age': self.age,
            'name': self.name,
            'occupation': self.occupation,
            'counter': self.counter
        }

    def __repr__(self):
        return '<User %r>' % self.name