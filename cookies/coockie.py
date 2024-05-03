from flask import  Flask,render_template,request,make_response
app = Flask(__name__)

# Technically, cookies track user activity to save user information in the browser as key-value pairs, which can then be accessed
# whenever necessary by the developers to make a website easier to use. These enhances the personal user experience on a particular website
# by remembering your logins, your preferences and much more.

# Using set_cookie( ) method to set the key-value pairs below.
# Response.set_cookie(key, value = '', max_age = None, expires = None, path = '/', domain = None,secure = None, httponly = False)
# key – Name of the cookie to be set.
# value – Value of the cookie to be set.
# max_age – should be a few seconds, None (default) if the cookie should last as long as the client’s browser session.
# expires – should be a datetime object or UNIX timestamp.
# domain – To set a cross-domain cookie.
# path – limits the cookie to given path, (default) it will span the whole domain.
@app.route('/setcookie')
def setcookie():
    # Initializing response object
    resp = make_response('Setting the cookie')
    resp.set_cookie('GFG', 'HERE this is ravi')
    return resp


# getting cookie from the previous set_cookie code
@app.route('/getcookie')
def getcookie():
    GFG = request.cookies.get('GFG')
    return 'GFG is a '+ GFG

if __name__ == '__main__':
   app.run(debug = True)   # app.run(host, port, debug, options)
