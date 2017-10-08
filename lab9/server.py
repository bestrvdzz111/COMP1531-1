from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Another_highly_secret_key'
login_manager = LoginManager(app=app, add_context_processor=True)
login_manager.login_view ="login"
