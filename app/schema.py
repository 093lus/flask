from app import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'age', 'occupation', 'counter')

user_schema = UserSchema()
users_schema = UserSchema(many=True)