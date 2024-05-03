from flask import Flask,render_template
app = Flask(__name__)

# #normal way to render templates
# @app.route('/')
# def index(user):
#    return render_template('hello.html')



#normal way to render templates with parameter passsing

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name = user)


if __name__ == '__main__':
   app.run(debug = True)