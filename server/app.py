from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_jwt_extended import JWTManager
from flask_cors import CORS  # Import CORS
from config import Config
from models import db
from routes import api

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
cache = Cache(app)
jwt = JWTManager(app)

# Enable CORS for all routes
CORS(app)  # This will allow all origins

# Register your API blueprint
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True, port=5000)
