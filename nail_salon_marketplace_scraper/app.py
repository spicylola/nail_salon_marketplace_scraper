import logging

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_apscheduler import APScheduler

from nail_salon_marketplace_scraper.settings import DevelopmentConfig
from nail_salon_marketplace_scraper.routes.routes import update_data, export_data
# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
scheduler = APScheduler()
logging.basicConfig()

def create_app(config_class=DevelopmentConfig):
    """
    Factory function to create a Flask application.
    """
    app = Flask(__name__)

    # Basic Configuration

    app.config.from_object(config_class)
    # Initialize extensions
    db.init_app(app)
    import nail_salon_marketplace_scraper.models
    migrate.init_app(app, db)
    cors.init_app(app)
    # initialize scheduler
    # if you don't wanna use a config, you can set options here:
    # scheduler.api_enabled = True
    scheduler.init_app(app)
    scheduler.start()
    #app.add_url_rule("/create-checkout-session", methods=["POST"], view_func=create_checkout_session)
    app.add_url_rule("/update-data", methods=["POST"], view_func=update_data)
    app.add_url_rule("/export-data", methods=["POST"], view_func=export_data)

    # Create a simple route
    @app.route('/', methods=['GET'])
    def hello_world():
        return jsonify(message="Hello, World!")

    # Register additional blueprints or routes here if needed

    return app

app = create_app()
if __name__ == '__main__':
    # Create the app and initialize the database


    # # Initialize database tables
    # with app.app_context():
    #     db.create_all()  # This will create tables based on the models

    # Run the Flask app
    app.run(debug=True)
