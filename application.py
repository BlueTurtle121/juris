from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os 

app = Flask(__name__)
app.secret_key='yeehawdingdangdiddly'
app.register_error_handler(404, pagenotfound)
db.init_app(app)
app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

# Other routes
@app.errorhandler(404)
def pagenotfound(e):
    return render_template('404.html'), 404

@app.errorhandler(401)
def forbidden(e):
    return render_template('401.html'), 401

@app.errorhandler(500)
def servererror(e):
    return render_template('500.html'), 500