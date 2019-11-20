from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)


# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'kaasboer'

user = {"jur": "pass"}


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        if user.get(username) == password:
            session['loggedin'] = True
            session['username'] = username
            return 'Logged in successfully!'
        else:
            msg = 'Wrong username or password.'
    return render_template('index.html', msg=msg)

@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

app.run()