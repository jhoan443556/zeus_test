from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def index():
    return 'hola mundo'

@app.route('/')
def home():
    return render_template('layout.html')

app.run(debug = True, port=5000)
