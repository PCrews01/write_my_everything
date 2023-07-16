from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import path

db = SQLAlchemy()
db_name = "wme.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "write+my+essay"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    
    db.init_app(app)
    
    from .templates.views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    from .templates.models import User, Essays, Schools
    
    if not path.exists('website/' + db_name):
        with app.app_context():
            db.create_all()
    return app