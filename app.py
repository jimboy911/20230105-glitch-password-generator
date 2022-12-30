from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Welcome', username=name)


if __name__ == '__main__':
    app.run()