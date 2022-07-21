from flask import *  
app = Flask(__name__) 

@app.route("/redir")
def redir():
    return "wrong"
    
      
@app.route('/log',methods = ['POST'])  
def login():  
    uname=request.form['user']  
    passwrd=request.form['pass']  
    if uname=="vasanth" and passwrd=="hello":  
        return render_template('message.html',name=uname)
    else:
        
        return redirect(url_for("/redir"))
       
if __name__ == '__main__':  
    app.run(debug = True,port=8081)  