from flask import Flask, render_template
from flask_cors import CORS
from .routes import api

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.register_blueprint(api, url_prefix='/api')
    
    # Serve frontend
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app 