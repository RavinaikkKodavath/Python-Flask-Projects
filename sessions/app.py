# Flask Session –
# Flask-Session is an extension for Flask that supports Server-side Session to your application.
# The Session is the time between the client logs in to the server and logs out of the server.
# The data that is required to be saved in the Session is stored in a temporary directory on the server.
# The data in the Session is stored on the top of cookies and signed by the server cryptographically.
# Each client will have their own session where their own data will be stored in their session.
# Uses of Session
# Remember each user when they log in
# Store User-specific website settings (theme)
# Store E-Commerce site user items in the cart
from flask import *

app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def home():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['response'] = 'session#1'
    return res;


@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response'];
        return render_template('getsession.html', name=s)


if __name__ == '__main__':
    app.run(debug=True)