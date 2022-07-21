from distutils.log import debug
from flask import *
app = Flask(__name__)

@app.route('/cookie')
def cookie():
    res = make_response("welcome")
    res.set_cookie("hi","hello")
    return res

if __name__ == "__main__":
    app.run(debug=True,port=5000)