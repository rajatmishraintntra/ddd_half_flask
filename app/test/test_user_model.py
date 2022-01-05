import unittest

import datetime

from app.main import db
from app.main.model.user import User
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_encode_auth_token(self):
        user = User(
            email='test246@wertest.com',
            username="rajatfortest246",
            registered_on=datetime.datetime.utcnow(),
            public_id="rajatdefr246"
        )
        user.password("test")
        user.save()
        auth_token = User.encode_auth_token(user.username)
        self.assertTrue(isinstance(auth_token, bytes))

    def test_decode_auth_token(self):
        user = User(
            email='test247@wertest.com',
            username="rajatfortest247",
            registered_on=datetime.datetime.utcnow(),
            public_id="rajatdefr247"
        )
        user.password("test")
        user.save()
        auth_token = User.encode_auth_token(user.username)
        self.assertTrue(isinstance(auth_token, bytes))
        datafortest=User.decode_auth_token(auth_token)
        self.assertTrue(datafortest !=None)


if __name__ == '__main__':
    unittest.main()

