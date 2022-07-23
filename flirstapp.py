from distutils.log import debug
from flask import Flask,jsonify


app = Flask(__name__)
@app.route('/index/<int:age>')
def home(age):
    return jsonify({'age':age})

if __name__== '__main__':
    app.run(debug=True)
