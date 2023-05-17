from flask import Flask

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # your MySQL username
app.config['MYSQL_PASSWORD'] = ''  # your MySQL password
app.config['MYSQL_DB'] = 'flask-project'  # your MySQL database name
