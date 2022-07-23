from requests import session
from flask import *

app = Flask(__name__)
app.secret_key = "abc"  

@app.route('/')
def index():
    res= make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4> ")
    session['s1']="Session#1"
    return res

@app.route("/get")
def getSessiondata():
    if "s1" in session:
        result = session['s1']
        res= render_template("session.html",name=result)
        return res
    
if __name__ == '__main__':
    app.run(debug=True,port = 8081)