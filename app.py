import secrets
from flask_wtf import FlaskForm
from wtforms import TextField ,PasswordField , SubmitField
from wtforms.validators import  DataRequired ,EqualTo, Length ,Email
from flask import Flask , url_for, render_template , redirect

app=Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = "12sd34fgt1scv"

class registerform(FlaskForm):
    user_name = TextField("Username",validators=[DataRequired(),Length(min=3,max=20)])
    email = TextField("email",validators=[DataRequired() ,Email()])
    password = PasswordField("Password",validators=[DataRequired(),Length(min=5,max=10)])
    confirm = PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Register')


class Login(FlaskForm):

    email = TextField("email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=1, max=4)])
    submit = SubmitField('Login')

@app.route('/')
@app.route('/home')
def hoo():
    return render_template('hom.html')


@app.route('/register',methods=['GET', 'POST'])
def index():
    formm = registerform()
    if formm.validate_on_submit():
        return redirect(url_for('hoo'))

    return render_template('reg.html',form=formm)
@app.route('/login',methods=['GET', 'POST'])
def signin():
    form1 = Login()

    if form1.validate_on_submit():
        return redirect(url_for('hoo'))

    return render_template('login.html' , form= form1)


if __name__ == "__main__":
    app.run(debug=True)


