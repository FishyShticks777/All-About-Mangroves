from flask import Flask, abort, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tbbbthdufdf78d8789bb123polz'

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/sources')
def sources():
    return render_template("bibliography.html")


if __name__ == '__main__':
    app.run(debug=True)