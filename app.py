from flask import Flask, render_template

# Create a Flask app instance
app = Flask(__name__)


@app.route('/') #if i remove this - it stops working
@app.route('/index') #not sure why i have to add this to get it to readd my index.html file correctly.
def index():
    list_of_passwords = "List of Passwords Here!"
    return render_template('index.html', title='Password Generator v2.0', password_list=list_of_passwords)

if __name__ == '__main__':
    app.run()