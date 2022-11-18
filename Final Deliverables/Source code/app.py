from flask import Flask,request,redirect 
from flask import render_template
app = Flask(__name__,template_folder='templates')


@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/')
def bot():
    return render_template('chatbot.html')
if __name__ == "__main__":
    app.run(debug=True)
