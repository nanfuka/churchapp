from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask import Flask, render_template, flash, request, jsonify, json
from wtforms import StringField, PasswordField
import psycopg2
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, render_template, request, url_for
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

app.config['SECRET_KEY'] = 'thisismysecretkey'


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

new_list = []
def my_fhun(temp_list):
    
    for ele in temp_list:
        if type(ele) == list:
            my_fhun(ele)
        else:

            new_list.append(ele)

@app.route('/', methods = ['GET', 'POST'])
def home():
    
    return render_template('home.html')

@app.route('/seark', methods = ['GET'])
def als():
    conn = psycopg2.connect(host='localhost', user='postgres', password= 'test', database= 'olives')
    cur = conn.cursor()
    cur.execute("SELECT username FROM trials")
    results = cur.fetchall()
    newlist =([list(l) for l in results])
	
    return newlist

@app.route('/search', methods = ['GET', 'POST'])
def search():
    
    return render_template('/ht/forrm.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    
    return render_template('/ht/login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    
    return render_template('/ht/registration.html')

@app.route('/r', methods = ['GET', 'POST'])
def registeri():
    
    return render_template('/ht/pikk.html')

@app.route('/userdash', methods = ['GET', 'POST'])
def userdash():
    
    return render_template('/ht/userdash.html')
@app.route('/retrieve')
def retrieve():
    conn = psycopg2.connect(host='localhost', user='postgres', password= 'test', database= 'olives')
    cur = conn.cursor()
    cur.execute("SELECT * FROM trials")
    data = cur.fetchall()
    return render_template('/ht/retrieved.html', data=data)



@app.route('/swee', methods = ['GET'])
def my_fun():
    my_fhun(als())

    print (new_list)
    return render_template('/ht/forrm.html', data =new_list )

@app.route('/allusernamesss', methods = ['GET', 'POST'])
def alllusernamess():
    
    form = LoginForm()
    conn = psycopg2.connect(host='localhost', user='postgres', password= 'test', database= 'olives')
    cur = conn.cursor()
  
    cur.execute("SELECT * FROM trials WHERE username =%s",(form.username.data,))
    dat = cur.fetchall()
    newlist =([list(l) for l in dat])
    return newlist

@app.route('/allusernamess', methods = ['GET', 'POST'])
def alllusernames():
    my_fhun(alllusernamess())

    print (new_list)
    return render_template('/ht/forrm.html', dat =new_list )
    
@app.route('/form', methods = ['GET', 'POST'])
def form():
    
    form = LoginForm()

    if form.validate_on_submit():
        conn = psycopg2.connect(host='localhost', user='postgres', password= 'test', database= 'olives')
        cur = conn.cursor()
        datas = "INSERT INTO trials(username, password) VALUES(%s,%s)"
        dukes= (form.username.data, form.password.data)
        cur.execute(datas,dukes)
        print("data inserted")
        conn.commit()

        conn.close()
        
    return render_template('/ht/form.html', form = form)
@app.route('/indexa', methods =['GET', 'POST'])
def show_index():
    form = LoginForm()
    
    conn = psycopg2.connect(host='localhost', user='postgres', password= 'test', database= 'olives')
    cur = conn.cursor()
    cur.execute("SELECT password FROM trials WHERE username =%s",(form.username.data,))
    conn.commit()
    pic = cur.fetchone()
    r =(''.join(pic))
    print(pic)
    
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], r)
    return render_template("/ht/forrm.html", user_image = full_filename)





 


if __name__ == '__main__':
    app.run(debug=True)