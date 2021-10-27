<<<<<<< HEAD
# Create flask app
=======
>>>>>>> react native
from flask import (
   Flask 
)
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD

# Mysql primary 
import mysql.connector
=======
from flask_marshmallow import Marshmallow
>>>>>>> react native

application = Flask(
    __name__,
    template_folder="../layer/A_PUI_layer"
)
<<<<<<< HEAD

# # ORM with sqlalchemy
# application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://b5ccecc68435b4:715fc6a8@us-cdbr-east-04.cleardb.com/heroku_ce6f8f81c233b36"
# application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# database = SQLAlchemy(application)

# application.config['MYSQL_HOST'] = 'us-cdbr-east-04.cleardb.com'
# application.config['MYSQL_USER'] = 'b5ccecc68435b4'
# application.config['MYSQL_PASSWORD'] = '715fc6a8'
# application.config['MYSQL_DB'] = 'heroku_ce6f8f81c233b36'

# Primary way to connect with mysql
# Config
database = mysql.connector.connect(
    host='us-cdbr-east-04.cleardb.com',
    user="b5ccecc68435b4",
    password="715fc6a8",
    database="heroku_ce6f8f81c233b36"
)
=======
application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://b5ccecc68435b4:715fc6a8@us-cdbr-east-04.cleardb.com/heroku_ce6f8f81c233b36"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(application)
marshmallow = Marshmallow(application)
>>>>>>> react native
