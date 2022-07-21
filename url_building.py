from distutils.log import debug
from flask import *


app=Flask(__name__)

@app.route("/home")
def home():
    return "home"
@app.route("/library")
def library():
    return "library"
@app.route("/dept")
def dept():
    return "dept"
@app.route("/about")
def about():
    return "about"
def hi():
    return "hi"
app.add_url_rule("/hello","hi",hi)
@app.route("/<path>")
def index(path):
    if path=="home":
        return redirect(url_for("home"))
    elif path=="dept":
        return redirect(url_for("dept"))
    elif path=="lib":
        return redirect (url_for("library"))
    elif path=="hai":
        pass
    else:
        return redirect(url_for("about"))
    
    
if __name__=="__main__":
    app.run(debug=True,port=8080)