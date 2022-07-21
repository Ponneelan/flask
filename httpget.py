from distutils.log import debug
from flask import *

app= Flask(__name__)

@app.route("/login",methods=["GET"])
def login():
    username= request.args  .get('user')
    password= request.args.get('pass')
    if username == "vasanth" and password == "hello":
        return "Welcome "+ username
    else :
        return "Wrong"
    
if __name__ == "__main__":
    app.run(debug=True,port=8080)