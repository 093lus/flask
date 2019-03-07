from wtforms import Form, IntegerField, StringField, validators

class UserForm(Form):
    name = StringField('name', [validators.Length(min=2, max=25)])
    age = IntegerField('age',[validators.Required()])
    occupation = StringField('occupation', [validators.Length(min=2, max=35)])
