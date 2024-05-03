from flask import *

app = Flask(__name__)


# Flask class provides the redirect() function which redirects the user to some specified URL with the specified status code.

# An HTTP status code is a response from the server to the request of the browser.
# When we visit a website, a request is sent to the server, and the server then responds to the browser's request with a three-digit code: the HTTP status code.
# This status code also represents the error.

# The syntax to use the redirect() function is given below.
# Flask.redirect(<location>,<status-code>, <response> )
# 1	location	It is the URL where the response will be redirected.
# 2	status code	It is the status code that is sent to the browser's header along with the response from the server.
# 3	response	It is the instance of the response that is used in the project for future requirements.


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/validate', methods = ["POST"])
def validate():
    if request.method == 'POST' and request.form['pass'] == 'jtp':
        return redirect(url_for("success"))
    else:
        abort(401)

# The abort() function is used to handle the cases where the errors are involved in the requests from the client side, such as bad requests, unauthorized access and many more.
# However, the error code is to be mentioned due to which the error occurred.
# The syntax to use the abort() function is given below.
# Flask.abort(code)


@app.route('/success')
def success():
    return "logged in successfully"


if __name__ == '__main__':
    app.run(debug=True)