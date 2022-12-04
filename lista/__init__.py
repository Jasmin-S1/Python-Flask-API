from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///doctor.db'
app.config['SECRET_KEY'] = '8d299a7b3cd84ff897e8a4a0'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page' #kada user klikne Get Started, preusmjeri ga na login page
login_manager.login_message_category = 'info'
