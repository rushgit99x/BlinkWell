from flask import Flask
from flask_login import LoginManager
from config import Config
from routes.auth import auth_bp
from routes.main import main_bp
from models.database import init_db
from models.user import load_user

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
init_db(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'

# Register user_loader
login_manager.user_loader(load_user)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)