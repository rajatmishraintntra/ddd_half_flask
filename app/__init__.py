from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import role_api as role_ns
from .main.controller.user_controller import permission_api as permissions_ns

from .main.controller.company_controller import company_api as comp_ns,city_api as city_ns,state_api as state_ns,country_api as country_ns

blueprint = Blueprint('api', __name__,url_prefix='/api')
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='Sunrise Api Docs',
    version='1.0',
    description='Api web Service',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns,path='/auth')
api.add_namespace(role_ns,path='/user_roles')
api.add_namespace(permissions_ns,path='/permissions')
api.add_namespace(comp_ns,path='/company')
api.add_namespace(city_ns,path='/city')
api.add_namespace(state_ns,path='/state')
api.add_namespace(country_ns,path='/country')
