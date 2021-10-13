from flask import (
   Flask 
)
from flask_sqlalchemy import SQLAlchemy

application = Flask(
    __name__,
    template_folder="../layer/A_PUI_layer"
)
application.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://b5ccecc68435b4:715fc6a8@us-cdbr-east-04.cleardb.com/heroku_ce6f8f81c233b36"
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = SQLAlchemy(application)