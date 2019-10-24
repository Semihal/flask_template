from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app
import config
from app.models import db


app = create_app(config, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
