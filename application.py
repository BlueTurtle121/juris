from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os 



@app.route('/')
def index():
    return render_template('index.html')

# # Other routes
# @app.errorhandler(404)
# def pagenotfound(e):
#     return render_template('404.html'), 404

# @app.errorhandler(401)
# def forbidden(e):
#     return render_template('401.html'), 401

# @app.errorhandler(500)
# def servererror(e):
#     return render_template('500.html'), 500


app = Flask(__name__)
app.secret_key='yeehawdingdangdiddly'
app.run(debug=True)