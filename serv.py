from flask import Flask, request, render_template
from ftp import ftp_test
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        host = request.form['host']
        user = request.form['user']
        password = request.form['password']
        return ftp_test(host,user,password)


if __name__ == '__main__':
    app.run()
