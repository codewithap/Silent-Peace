from flask import Flask, render_template 
app = Flask(__name__) 

@app.route("/")
@app.route("/silent_peace")
def home():
    return render_template("home.html")
    

@app.route('/login')
def login():
  return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)