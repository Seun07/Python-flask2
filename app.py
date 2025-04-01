from flask import Flask,jsonify,render_template
import os
import socket
app=Flask(__name__)

#find the hostname and machine ip


def findhostname():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

@app.route("/")
def home():
    
    return("You are highly welcome")

@app.route("/score")
def calculate():
    a=40
    b=50
    result=a+b
    return render_template('show.html',finalscore=result)

@app.route("/details")
def hostme():
    myhost,myip=findhostname()
    return render_template('index.html',host=myhost,IP=myip)
    

def home():
    email="check4obi@yahoo.com"
    mobile="2347036483444"
    return "These are the company contact details" + email + "," + mobile

@app.route("/calculate")

def calculate():
    a = 56
    b = 34
    sum = a + b
    return "This is the sum total:" + str(sum)
    
if __name__ == '__main__':
    app.run(debug=True, port=5002,host="0.0.0.0")
