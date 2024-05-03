from flask import *

app = Flask(__name__)
app.secret_key = "ravi" #The Session data is stored on top of cookies and the server signs them cryptographically. For this encryption, a Flask application needs a defined SECRET_KEY.


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/success', methods=["POST","GET"])
def success():
    if request.method == "POST":
        session['email'] = request.form['email'] #here we are setting the session with email variable
    return render_template('success.html')


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)  #here we are deleting the session with email variable
        return render_template('logout.html');
    else:
        return '<p>user already logged out</p>'


@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        return '<p>Please login first</p>'


if __name__ == '__main__':
    app.run(debug=True)