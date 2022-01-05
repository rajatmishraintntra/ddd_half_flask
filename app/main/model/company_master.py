from .. import db
import datetime
from .user import User
from mongoengine import signals
from .accounts import AccountMaster,AccountsType
from mongoengine import signals
class CurrencyMaster(db.EmbeddedDocument):
    name=db.StringField(max_length=100)
    icon=db.ImageField()
    exchange_rate_to_usd=db.DecimalField()
    exchange_rate_to_inr=db.DecimalField()
    def __str__(self) -> str:
        return self.name

class Country(db.Document):
    name=db.StringField(max_length=10000)
    def __str__(self):
        return self.name

class State(db.Document):
    name=db.StringField(max_length=10000)
    def __str__(self):
        return self.name

class City(db.Document):
    name=db.StringField(max_length=10000)
    def __str__(self):
        return self.name

class PincodeMaster(db.EmbeddedDocument):
    pincode=db.IntField()
    area=db.StringField(max_length=1000)
    city=db.ReferenceField(City)
    state=db.ReferenceField(State)
    country=db.ReferenceField(Country)
    def __str__(self) -> str:
        return str(self.pincode)


class Address(db.EmbeddedDocument):
    address1=db.StringField(max_length=10000)
    landmark=db.StringField(max_length=1000)
    pincode=db.EmbeddedDocumentField(PincodeMaster)
    def __str__(self) -> str:
        return self.address1

class VerificationAuthorityMaster(db.EmbeddedDocument):
    name=db.StringField(max_length=100)
    url=db.ListField(db.URLField(required=False),required=False)
    addresses=db.ListField(db.EmbeddedDocumentField(Address))
    verification_type=db.StringField(max_length=1000)
    def __str__(self) -> str:
        return self.name

class RegINFO(db.EmbeddedDocument):
    reg_name=db.StringField(max_length=1000)
    reg_reg_no=db.StringField(max_length=1000)
    ref_doc=db.FileField()
    verification_type=db.StringField(max_length=1000)
    is_verified=db.BooleanField(default=False)
    verification_authority=db.EmbeddedDocumentField(VerificationAuthorityMaster)
    def __str__(self) -> str:
        return self.reg_name

class BankDetailsMaster(db.EmbeddedDocument):
    bank_name=db.StringField(max_length=1000)
    code_type=db.StringField(max_length=1000)
    code=db.StringField(max_length=1000)
    a_c_no=db.StringField(max_length=1000)
    a_c_type=db.StringField(max_length=1000)
    is_verified=db.BooleanField(default=False)
    def __str__(self) -> str:
        return self.bank_name

class BranchMaster(db.EmbeddedDocument):
    branch_name=db.StringField(max_length=1000)
    address=db.EmbeddedDocumentField(Address)
    reg_info=db.EmbeddedDocumentField(RegINFO)
    bank_info=db.ListField(db.EmbeddedDocumentField(BankDetailsMaster))
    accepted_currences=db.ListField(db.EmbeddedDocumentField(CurrencyMaster))
    def __str__(self) -> str:
        return self.branch_name

class CompanyMaster(db.Document):
    comp_code=db.StringField(max_length=10)
    name=db.StringField(max_length=10000)
    Reg_info=db.ListField(db.EmbeddedDocumentField(RegINFO))
    comp_type=db.StringField(max_length=10000)
    branches=db.ReferenceField(AccountsType)
    credit_limit=db.FloatField()
    bank_info=db.ListField(db.EmbeddedDocumentField(BankDetailsMaster))
    created_on = db.DateTimeField(default=datetime.datetime.utcnow())
    updated_on = db.DateTimeField(default=datetime.datetime.utcnow())
    created_by = db.ReferenceField(User)
    def __str__(self):
        return self.name

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        data=AccountMaster(name=document.name,type=document.type,ref_comp=document)
        data.save()





signals.post_save.connect(CompanyMaster.post_save,sender=CompanyMaster)