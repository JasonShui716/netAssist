from flask import Flask, request, render_template,g,redirect,url_for,session
from ftpls import ftpls
import os
app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        session.permanent=True
        session['host'] = request.form['host']
        session['user'] = request.form['user']
        session['password'] = request.form['password']
        session['currdir'] = '|'
        return redirect(url_for("cd",dirname='|'))

@app.route('/dir/<path:dirname>/')
def cd(dirname):
    if session['currdir']=='':
        session['prevdir'] = '|'
    elif session['currdir'][0]=='/':
        session['prevdir'] = session['currdir'].replace(session['currdir'][0],'')
    else:
        pass
    session['currdir'] = dirname.replace('|','')
    print(dirname)
    return ftpls(session['host'],session['user'],session['password'],session['currdir'])

@app.route('/back')
def back():
    return redirect(url_for("cd", dirname=session['prevdir']))

if __name__ == '__main__':
    app.run()
