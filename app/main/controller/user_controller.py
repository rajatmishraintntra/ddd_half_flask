from flask import request
from flask.wrappers import Response
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, permission,token_required
from ..util.dto import UserDto,RoleDto,PermissionsDto
from ..service.user_service import get_all_roles, save_new_user, get_all_users, get_a_user,create_new_role,update_role_data,get_a_role,create_new_permissions,update_permissions_data,get_a_permissions,get_all_permissions,update_user_data
from typing import Dict, Tuple

api = UserDto.api
_user = UserDto.user
role_api=RoleDto.api
_role=RoleDto.user_role
permission_api=PermissionsDto.api
_permissions=PermissionsDto.users_permissions

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
    @api.expect(_user,validate=True)
    @api.response(206,"User Updated")
    @api.param("public_id","the User identifier")
    @api.doc("update_a_user")
    @api.marshal_with(_user)
    def put(self,public_id):
        """update a user given its identifier"""
        data=request.json
        return update_user_data(data=data,public_id=public_id)



@role_api.route('/roles')
class RolesView(Resource):
    @role_api.expect(_role,validate=True)
    @role_api.response(201,"Role Created")
    @role_api.doc("Create a New Role")
    @token_required
    def post(self):
        """ create a role """
        data=request.json
        return create_new_role(data=data)
    @role_api.doc("get_list_of_roles")
    @token_required
    def get(self):
        """ List all roles """
        return get_all_roles()
@role_api.route('/roles/<id>')
class RolesViewUpdate(Resource):
    @role_api.expect(_role,validate=True)
    @role_api.response(206,"Roles Updated")
    @role_api.param("id","the role identifier")
    @role_api.doc("update_a_role")
    def put(self,id):
        """ Update a role """
        data=request.json
        return update_role_data(data=data,id=id)
    @role_api.doc("get_a_role")
    def get(self,id):
        """ get a role with identifier """
        user=get_a_role(id)
        if not user:
            role_api.abort(404)
        else:
            return user

@permission_api.route('/permissions')
class PermissionsView(Resource):
    @permission_api.expect(_permissions,validate=True)
    @permission_api.response(201,"Permission Created")
    @permission_api.doc("Create a New Permission")
    @token_required
    def post(self):
        """ Create a permission """
        data=request.json
        return create_new_permissions(data=data)
    @permission_api.doc("get_list_of_permissions")
    @token_required
    def get(self):
        """ List all permissions """
        return get_all_permissions()
@permission_api.route('/permissions/<id>')
class RolesViewUpdate(Resource):
    @permission_api.expect(_role,validate=True)
    @permission_api.response(206,"Permissions Updated")
    @permission_api.param("id","the permission identifier")
    @permission_api.doc("update_a_Permissions")
    def put(self,id):
        """ Update a permission """
        data=request.json
        return update_permissions_data(data=data,id=id)
    @permission_api.doc("get_a_Permissions")
    def get(self,id):
        """ get a permission """
        user=get_a_permissions(id)
        if not user:
            permission_api.abort(404)
        else:
            return user

