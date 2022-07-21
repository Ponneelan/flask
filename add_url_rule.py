from distutils.log import debug
from flask import Flask

app= Flask(__name__)
def home():
    return "home"
def welcome():
    return 'welcome'

app.add_url_rule('/home',"home",home)
app.add_url_rule('/',"welcome",welcome)


if __name__== "__main__":
    app.run(debug=True,port=8081)