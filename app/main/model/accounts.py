from .. import db
import datetime
from .user import User
from mongoengine import signals
import uuid
class AccountsType(db.Document):
    account_type=db.StringField(max_length=100)

class FinYear(db.Document):
    start_year=db.DateTimeField()
    end_year=db.DateTimeField()
    closed=db.BooleanField(default=False)
    def __str__(self):
        return str(self.start_year)+"-"+str(self.end_year)


class AccountMaster(db.Document):
    name=db.StringField(max_length=100)
    type=db.ReferenceField(AccountsType)
    ref_comp=db.ReferenceField("app.main.model.company_master.CompanyMaster")

class Items(db.EmbeddedDocument):
    acc_id=db.ReferenceField(AccountMaster)
    amount=db.FloatField()
    nature=db.StringField(max_length=2)

class GeneralLedger(db.Document):
    fin_year=db.ReferenceField(FinYear)
    trans_id=db.UUIDField(default=uuid.uuid4())
    trans_date=db.DateTimeField(default=datetime.datetime.utcnow().date)
    items=db.ListField(db.EmbeddedDocumentField(Items))

