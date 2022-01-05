from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from .config import config_by_name
from flask.app import Flask
from flask_admin import Admin,form
from flask_admin.contrib.mongoengine import ModelView
import os
db = MongoEngine()
flask_bcrypt = Bcrypt()

def create_app(config_name: str) -> Flask:
    template_dir = os.path.abspath('./app/templates')
    app = Flask(__name__,template_folder=template_dir,static_folder='./app/static/sunrise/build/static')
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    admin=Admin(app,name="sunrise")
    from .model.blacklist import BlacklistToken
    from .model.user import User,Permissions,Role
    from .model.company_master import CompanyMaster
    from .model.accounts import AccountMaster,AccountsType,GeneralLedger,FinYear
    class TestModelView(ModelView):
        pass
    admin.add_view(ModelView(User))
    admin.add_view(ModelView(BlacklistToken))
    admin.add_view(ModelView(Permissions))
    admin.add_view(ModelView(Role))
    admin.add_view(TestModelView(CompanyMaster))
    admin.add_view(TestModelView(AccountMaster))
    admin.add_view(TestModelView(AccountsType))
    admin.add_view(TestModelView(GeneralLedger))
    admin.add_view(TestModelView(FinYear))
    return app
