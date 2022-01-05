from app.main.model.user import User
from ..service.blacklist_service import save_token
from typing import Dict, Tuple


class Auth:
    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            user = User.objects(email=data.get('email')).first()
            print(user.check_password(data.get('password')))
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(str(user.id))
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_user(data: str) -> Tuple[Dict[str, str], int]:
        if data:
            auth_token = data

        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            
            if  isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_user(new_request):
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            print(resp)
            user = User.objects(id=resp).first()
            if user is not None:
                data=dict(user_id=str(user.id),
                        email=user.email,
                        admin=user.admin,
                        registered_on=str(user.registered_on))
                response_object = {
                    'status': 'success',
                }
                response_object['data']=data
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
    @staticmethod
    def get_permission_lavel(new_request):
        auth_token = new_request.headers.get('Authorization')
        if auth_token:
            resp=User.decode_auth_token(auth_token)
            if not isinstance(resp,str):
                user=User.objects(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'permissions': [x.keyword for x in user.permissions_user],
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401


