from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)



from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix="/api")

from app import models