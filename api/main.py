from flask import Flask, render_template, request,redirect, url_for, session, Blueprint
import pymongo
from db import database
from pymongo.server_api import ServerApi

app = Flask(__name__) 

import admin


app.secret_key = '##@$sGwJCyEn4DVw46fm736hymzkHztDZVNK0c7Mhywd'
myclient = pymongo.MongoClient("mongodb+srv://speace:sp1234@silentpeace.d2wm9xi.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = myclient["silentpeace"]
col = db["Members"]
app.register_blueprint(admin.admin, url_prefix='/admin')


@app.route("/")
@app.route("/silent_peace")
def home():
    return render_template("home.html")



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST" and "username"  in request.form and "passwd" in request.form:
        username = request.form["username"]
        passwd = request.form["passwd"]
        user = database.login( username,passwd)
        if user[1]  == True:
            session['loggedin'] = True
            session['username'] = request.form["username"]
            return render_template("home.html", msg = user[0])

        elif user[1] == False:
            return render_template("login.html", msg = user[0])
        pass
    elif request.method == "GET":
        return render_template('login.html')



@app.route("/register", methods=["GET","POST"])
def signup():
    if request.method == 'POST' and 'name' in request.form and 'username' in request.form and "email" in request.form and "num" in request.form and "passwd" in request.form :
        name = request.form['name']
        username = request.form["username"]
        email = request.form.get('email')
        number = request.form.get('num')
        password = request.form.get('passwd')
        response = database.register(name, username, password, email, number)
        if response[1] == True:
          return render_template("home.html", msg = response[0])
        elif response[1] == False:
          return render_template("register.html", msg = response[0])
    else: 
      return render_template("register.html" )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")