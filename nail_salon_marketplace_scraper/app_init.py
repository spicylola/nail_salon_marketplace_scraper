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

# Set up logging
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)


def create_app(config_class=DevelopmentConfig):
    """
    Factory function to create a Flask application.
    """
    app = Flask(__name__)

    # Configure the app
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    import nail_salon_marketplace_scraper.models  # Ensure models are loaded
    migrate.init_app(app, db)
    cors.init_app(app)

    # Initialize and start the scheduler
    scheduler.init_app(app)
    scheduler.start()

    # Register routes
    app.add_url_rule("/update-data", methods=["POST"], view_func=update_data)
    app.add_url_rule("/export-data", methods=["POST"], view_func=export_data)

    # Simple test route
    @app.route('/', methods=['GET'])
    def hello_world():
        return jsonify(message="Hello, World!")

    return app
# Schedule the job to run at regular intervals using Flask-APScheduler
@scheduler.task('interval', id='populate_nail_salons', seconds=60, misfire_grace_time=900)
def scheduled_job():
    """
    Scheduled job to run the populate_nail_salons function regularly.
    """
    print("Running scheduled job to populate nail salons...")
    from nail_salon_marketplace_scraper.jobs.google_map_job import populate_nail_salons
    populate_nail_salons()
