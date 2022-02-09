from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is the main page with html word from it like: <h1>Hello Word</h1>"

@app.route('/<name>/')
def user(name):
    return f"Hello { name }"

@app.route('/admin/')
def admin():
    return redirect(url_for('user', name='Mokwyzebeurga'))

if __name__ == "__main__":
    app.run(debug=True)