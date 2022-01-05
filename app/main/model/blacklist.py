from .. import db
import datetime


class BlacklistToken(db.Document):
    token = db.StringField(max_length=10000, unique=True)
    blacklisted_on = db.DateTimeField(default=datetime.datetime.utcnow())

    def fill(self):
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token: str) -> bool:
        # check whether auth token has been blacklisted
        res = BlacklistToken.objects(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False
