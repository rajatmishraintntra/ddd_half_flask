from os import name
import uuid
import datetime

from flask_mongoengine import json

from app.main import db
from app.main.model.user import User,Role,Permissions
from typing import Dict, Tuple


def save_new_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    user = User.objects(email=data['email']).first() or User.objects(username=data['username']).first() or User.objects(public_id=data['public_id']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            registered_on=datetime.datetime.utcnow(),
            admin=data['admin'],
            active=data['active'],
        )
        new_user.handle_permissions(data['permissions_user'])
        new_user.handle_roles(data['roles'])
        new_user.password(data['password'])
        save_changes(new_user)
        return generate_token(new_user)
    else:
        msg=''
        if user.email in data.values() and user.username in data.values():
            msg='User already exists. Please Log in.'
        elif user.email not in data.values() and user.username in data.values():
            msg="username already taken. chose a different one"
        elif user.email  in data.values() and user.username not in data.values():
            msg='email already with another user'
        response_object = {
            'status': 'fail',
            'message': msg,
        }
        return response_object, 409

        
def update_role_data(data,id):
    Role.objects(id=id).update(**data)
    return {"status":"updated"},206

def update_user_data(data,public_id):
    User.objects(public_id=public_id).update(**data)
    return {"status":"updated"},206

def create_new_role(data):
    role=Role.objects(name=data['name']).first()
    if not role:
        new_role=Role(name=data['name'],description=data['description'])
        new_role.attech_permissions(data['default_permissions'])
        new_role.save()
        resp={
            'status': 'sucess',
            'message': 'Role Created',
        }
        return resp,201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Role already exists.Please Check',
        }
        return response_object, 409


def create_new_permissions(data):
    role=Permissions.objects(name=data['name']).first()
    if not role:
        new_role=Permissions(name=data['name'],keyword=data['description'])
        new_role.save()
        resp={
            'status': 'sucess',
            'message': 'Permissions Created',
        }
        return resp,201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Permissons already exists.Please Check',
        }
        return response_object, 409


def get_all_permissions():
    return Permissions.objects.to_json()


def get_a_permissions(id):
    return Permissions.objects(id=id).first()


def update_permissions_data(data,id):
    Permissions.objects(id=id).update(**data)
    return {"status":"updated"},206


def get_all_users():
    import json as jd
    ue=User.objects.to_json()
    return ue


def get_all_roles():
    import json as jd
    ue=Role.objects.to_json()
    return ue


def get_a_user(public_id):
    return User.objects(public_id=public_id).first()

def get_a_role(id):
    return Role.objects(id=id).first()


def generate_token(user: User) -> Tuple[Dict[str, str], int]:
    try:
        # generate the auth token
        auth_token = User.encode_auth_token(str(user.id))
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data: User) -> None:
    data.save()

