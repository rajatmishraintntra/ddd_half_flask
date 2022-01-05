import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist
from flask import render_template
import shutil
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
@app.route("/")
def hello_world():
    return render_template("index.html")

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

def build_react():
    os.chdir('./app/static/sunrise')
    os.system("yarn build")
    os.replace('./build/index.html','../../templates/index.html')
    print("fronend build done ")
    os.chdir('../../../')
    return "ok"
@manager.command
def run():
    build_react()
    app.run(host="0.0.0.0")


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
