from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '24c7de95f8cd34eeb3c208416aa5fd32'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///config/khub_config.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from khub import routes