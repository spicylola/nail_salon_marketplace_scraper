import logging

# from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_cors import CORS
# from flask_apscheduler import APScheduler

from nail_salon_marketplace_scraper.app_init import create_app
# Create the app instance
app = create_app()




if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)

