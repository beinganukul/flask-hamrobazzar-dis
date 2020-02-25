from flask import Flask,url_for,request,render_template
from markupsafe import escape
#from flask_bootstrap import Bootstrap


app = Flask(__name__)
#Bootstrap(app)

@app.route('/single')
@app.route('/single/<name>')
@app.route('/single/<name>/<item_name>')
@app.route('/single/<name>/<item_name>/<contacts>')
@app.route('/single/<name>/<item_name>/<contacts>/<item_detail>')
@app.route('/single/<name>/<item_name>/<contacts>/<item_detail>/<price>')
def single(name=None,item_name=None,contacts=None,item_detail=None,price=None):
    return render_template('single.html',name=name,item_name=item_name,contacts=contacts,item_detail=item_detail,price=price)

@app.route('/all')
def all():
    return render_template('all.html')
@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login'
    else:
        return 'show_the_login_form'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
   # print(url_for('index'))
    print(url_for('login'))
    print(url_for('login',next = '/'))
    print(url_for('profile',username = 'JOnh Doe'))

    





