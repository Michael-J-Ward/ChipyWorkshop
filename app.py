from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask import Flask, render_template

from api import get_meetup_members

class MyForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/meetup')
def meetup():
    # somehow we will get an event id from the form
    members = list(get_meetup_members('235484841'))
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)