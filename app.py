from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect

from api import get_meetup_members

import pprint 

class MeetupForm(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    form = MeetupForm()
    if form.validate_on_submit():
        event_id = str(form.id.data)
        return redirect('/meetup/' + event_id)
    return render_template('index.html', form=form) 

@app.route('/meetup/<event_id>')
def meetup(event_id):
    # somehow we    will get an event id from the form
    members = get_meetup_members(event_id)
    return render_template('test.html', members=members)

if __name__ == '__main__':
    app.run(debug=True)