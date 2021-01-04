from flask import Flask, request, render_template

from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

# initiating app for Flask app
mysql.init_app(app)

@app.route('/')
def my_form():

    # extract the content to html page
    return render_template('from_ex.html')


@app.route('/',methods = ['POST'])
def Authenticate():

    username = request.form['u']
    password  = request.form['p']
    cursor = mysql.connect().cursor()
    cursor.execute("select * from User where usename " + username + "and password= " + password + "")
    data = cursor.fetchone()

    if data is None:
        return "Username or Password is wrong"

    else:
        return "Successfully logged in"

    if __name__ = "__main__":
        app.run()

