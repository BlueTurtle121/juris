from flask import Flask
app = Flask(__name__)

@app.route('/')
def start():
    return '<h1>Placeholder 1</h1>'

if __name__ == '__main__':
    app.run(debug=True)