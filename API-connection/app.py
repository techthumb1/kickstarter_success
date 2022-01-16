from os import getenv
from flask import Flask#, jsonify, Blueprint, render_template, request


# Creates application
def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    #DB.init_app(app)

    #DATABASE_URI = "Kickstarter_2021-02-11T03_20_07_976Z.json"

    # Database and app configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Decorator listens for specific endpoint visits
    @app.route('/')
    def root():
        return "1, 2, 3, 4, 5" #render_template(request.value, request.data)


    @app.route('/success', methods=['POST'])
    def success():
        """If target data is successful or failed"""
        return 'Successful'

    @app.route('/state', methods=["POST"])
    def failed():
        if failed == True:
            print("UNSUCCESSFUL")
        return "Failed"

    return app