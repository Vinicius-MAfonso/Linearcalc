from linearcalc.config import Config
from flask import Flask

def create_app(config_obj=Config):
    app = Flask(__name__)
    if config_obj is not None:
        app.config.from_object(config_obj)
        
    from .main.routes import main
    app.register_blueprint(main)
    
    return app

