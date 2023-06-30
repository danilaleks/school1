from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/derived')
def derived():
    return render_template('derived.html')

if __name__ == '__main__':
    app.run()
