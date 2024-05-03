from flask import Flask  #Importing flask module in the project is mandatory. An object of Flask class is our WSGI application.

app = Flask(__name__)  #Flask constructor takes the name of current module (__name__) as argument.

# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# app.route(rule, options)

@app.route('/') #
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run(debug = True)   # app.run(host, port, debug, options)

# Debug mode
# A Flask application is started by calling the run() method. However, while the application is under development, it should be restarted manually for each change in the code. To avoid this inconvenience, enable debug support. The server will then reload itself if the code changes. It will also provide a useful debugger to track the errors if any, in the application.
# The Debug mode is enabled by setting the debug property of the application object to True before running or passing the debug parameter to the run() method.

# app.debug = True
# app.run()
# app.run(debug = True)