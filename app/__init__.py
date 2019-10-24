from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from app.site.routes import site_bp
from app.api.routes import api_bp

bootstrap = Bootstrap()
migrate = Migrate()


def create_app(config, db):
    app = Flask(__name__)
    app.config.from_object(config)

    # init extension
    bootstrap.init_app(app)
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)

    # init blueprints
    app.register_blueprint(site_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
