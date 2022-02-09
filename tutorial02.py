from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('index.html', name=name, r=234, content=[1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == "__main__":
    app.run(debug=True)