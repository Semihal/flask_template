from flask import Flask
from flask_bootstrap import Bootstrap

from app.site.routes import site_bp
from app.api.routes import api_bp

bootstrap = Bootstrap()


def create_app():
    app = Flask(__name__)

    # init extension
    bootstrap.init_app(app)

    # init blueprints
    app.register_blueprint(site_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
