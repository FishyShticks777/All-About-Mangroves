from flask import Flask, abort, render_template, redirect, url_for, flash, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tbbbthdufdf78d8789bb123polz'

@app.route('/')
def index():    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)