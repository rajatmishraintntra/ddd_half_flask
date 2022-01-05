from ..model.company_master import *


def get_all_cities():
    return City.objects.to_json()

def get_a_city(id):
    return City.objects(id=id).first()

def save_city(data):
    new_city=City(**data)
    try:
        City.objects.get(**data)
        return {"city":"exists"}
    except:
        new_city.save()
    return City.objects.get(**data).to_json()

def update_a_city(data,id):
    City.objects(id=id).update(**data)
    return {"status":"updated"},206

def delete_a_city(id):
    City.objects(id=id).delete()
    return {"status":"delete"},204

def get_all_states():
    return State.objects.to_json()

def get_a_state(id):
    return State.objects(id=id).first()

def save_a_state(data):
    new_state=State(**data)
    try:
        State.objects.get(**data)
        return {"State":"exists"}
    except:
        new_state.save()
    return State.objects.get(**data).to_json()

def update_a_state(data,id):
    State.objects(id=id).update(**data)
    return {"status":"updated"},206

def delete_a_state(id):
    State.objects(id=id).delete()
    return {"status":"delete"},204

def get_all_country():
    return Country.objects.to_json()

def get_a_country(id):
    return Country.objects(id=id).first()

def save_a_country(data):
    new_country=Country(**data)
    try:
        Country.objects.get(**data)
        return {"Country":"exists"}
    except:
        new_country.save()
    return Country.objects.get(**data).to_json()

def update_a_country(data,id):
    Country.objects(id=id).update(**data)
    return {"status":"updated"},206

def delete_a_country(id):
    Country.objects(id=id).delete()
    return {"status":"delete"},204

def get_all_pincode():
    return PincodeMaster.objects.to_json()

def get_a_pincode(id):
    return PincodeMaster.objects(id=id).first()

def save_a_pincode(data):
    new_pincode=PincodeMaster(**data)
    try:
        PincodeMaster.objects.get(**data)
        return {"Country":"exists"}
    except:
        new_pincode.save()
    return PincodeMaster.objects.get(**data).to_json()

def update_a_pincode(data,id):
    PincodeMaster.objects(id=id).update(**data)
    return {"status":"updated"},206

def delete_a_pincode(id):
    PincodeMaster.objects(id=id).delete()
    return {"status":"delete"},204



def get_all_companies():
    return CompanyMaster.objects.to_json()

def get_a_company(id):
    return CompanyMaster.objects(id=id).first()

def save_a_company(data):
    new_company=CompanyMaster(**data)
    try:
        CompanyMaster.objects.get(**data)
        return {"Company":"exists"}
    except:
        new_company.save()
    return {"company":"Created"},201

def update_a_company(id,data):
    CompanyMaster.objects(id=id).update(**data)
    return {"company":"updated"},206

def delete_a_company(id):
    CompanyMaster.objects(id=id).delete()
    return {"company":"deleted"},204



    