from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('index.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      res = request.form  
      return render_template("results.html",result = res)  
   
if __name__ == '__main__':  
   app.run(debug = True) 