from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField("Id no of Puppy to Remove : ")
    submit = SubmitField('Remove Puppy')


class AddOwner(FlaskForm):

    name = StringField("Name of owner: ")
    id = IntegerField("Id of puppy: ")
    submit = SubmitField("Add Owner")
