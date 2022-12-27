from transformers import pipeline
from crypt import methods
from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#Create a flask instance
app=Flask(__name__)
app.config['SECRET_KEY'] = "My super secrete key"

 #create a form class
class NameForm(FlaskForm):
    name=StringField("Type your input here",validators=[DataRequired()])
    submit=SubmitField("Submit")


@app.route("/review", methods=['GET', 'POST'])
def review():
    name=None
    text=None
    form=NameForm()
    #validate form
    name=form.name.data
    form.name.data=''
    text=str(name)
    classifier = pipeline('sentiment-analysis', model="/Users/srivatsa/Desktop/Srivatsa@Study/Artificial_Intelligence/model")
    source = classifier(text)
    return render_template('name.html',data=source,name=name,form=form)

