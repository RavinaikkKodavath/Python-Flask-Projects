from flask import Flask,render_template
# Flask constructor takes the name of current module (__name__) as argument.
# A Flask application is started by calling the run() method

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)