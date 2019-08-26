from flask import Flask, render_template, session, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateField, RadioField,
                        SelectField, TextField,TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

class InfoForm(FlaskForm):
    breed = StringField('What is your breed?', validators=[DataRequired()])
    nutered = BooleanField('Have you been nutered?')
    mood = RadioField('Please Choose your mood...',
                        choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food = SelectField('Select your choice',
                                choices=[('chicken', 'Chicken'), ('fish', 'Fish'), ('mutton', 'Mutton')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['nutered'] = form.nutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        session['submit'] = form.submit.data
    
        return redirect(url_for('thankyou')

    return render_template('index.html', form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)



