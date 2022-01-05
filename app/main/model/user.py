from .. import db, flask_bcrypt
import datetime
from app.main.model.blacklist import BlacklistToken
from ..config import key
import jwt
from typing import Union
from mongoengine import signals
class Permissions(db.Document):
    name=db.StringField(max_length=80, unique=True)
    keyword=db.StringField(max_length=80, unique=True)
    def __str__(self) -> str:
        return self.name
class Role(db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)
    default_permissions=db.ListField(db.ReferenceField(Permissions), default=[])

    def __str__(self) -> str:
        return self.name
    def attech_permissions(self,permissions):
        self.default_permissions=[Permissions.objects(name=x['name']).first() for x in permissions if Permissions.objects(name=x['name']).first()]
class User(db.Document):
    email = db.StringField(max_length=80, unique=True)
    registered_on = db.DateTimeField()
    active = db.BooleanField(default=True)
    admin = db.BooleanField(default=False)
    public_id = db.StringField(max_length=80, unique=True)
    username = db.StringField(max_length=80, unique=True)
    password_hash = db.StringField(max_length=80)
    roles = db.ListField(db.ReferenceField(Role), default=[])
    permissions_user=db.ListField(db.ReferenceField(Permissions), default=[])
    def __str__(self):
        return self.username
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return flask_bcrypt.check_password_hash(self.password_hash, password)
    def handle_roles(self,roles):
        if roles!=[]:
            self.roles=[Role.objects(name=x['name']).first() for x in roles if Role.objects(name=x['name']).first()]
    def handle_permissions(self,permissions_user):
        if permissions_user!=[]:
            self.permissions_user=[Permissions.objects(keyword=x['keyword']).first() for x in permissions_user if Permissions.objects(keyword=x['keyword']).first()]
    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        if document.roles!=[]:
            per=[]
            for x in document.roles:
                for i in x.default_permissions:
                    per.append(i)
            document.permissions_user=per

    @staticmethod
    def encode_auth_token(user_id: str) -> bytes:
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token: str) -> Union[str, int]:
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 23
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 45
        except jwt.InvalidTokenError:
            return 56

    def __repr__(self):
        return "<User '{}'>".format(self.username)

signals.pre_save.connect(User.pre_save,sender=User)