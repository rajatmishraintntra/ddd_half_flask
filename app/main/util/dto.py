
from flask_restx import Namespace, fields
from mongoengine.fields import DateTimeField

from app.main.model.company_master import Address

class PermissionsDto:
    api=Namespace("users_permissions",description="Permissions Assign For Users")
    users_permissions=api.model("users_permissions",{
        "name":fields.String(required=True,description="name"),
        "keyword":fields.String(required=True,description="keyword")
    })
class RoleDto:
    api=Namespace("user_role",description="Role Assign For Users")
    users_permissions=api.model("users_permissions",{
        "name":fields.String(required=True,description="name"),
        "keyword":fields.String(required=True,description="keyword")
    })
    user_role=api.model("user_role",{
        "name":fields.String(required=True,description="Role Name"),
        "description":fields.String(required=True,description="Role Name"),
        "default_permissions":fields.List(fields.Nested(users_permissions),description="Role Permissions")
    })
class UserDto:
    api = Namespace('user', description='user related operations')
    users_permissions=api.model("users_permissions",{
        "name":fields.String(required=True,description="name"),
        "keyword":fields.String(required=True,description="keyword")
    })
    user_role=api.model("user_role",{
        "name":fields.String(required=True,description="Role Name"),
        "description":fields.String(required=True,description="Role Name"),
        "default_permissions":fields.List(fields.Nested(users_permissions),description="Role Permissions")
    })
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier'),
        "active":fields.Boolean(default=True),
        "admin":fields.Boolean(default=False),
        "roles":fields.List(fields.Nested(user_role),required=False, description='Role'),
        "permissions_user":fields.List(fields.Nested(users_permissions),required=False,description="permissions")
    })
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password'),
    })

class CityDto:
    api=Namespace("citydto",description="city info data")
    city_model=api.model("city",{
        "name":fields.String(required=True,description="city name")
    })
class StateDto:
    api=Namespace("StateDto",description="State info data")
    state_model=api.model("state",{
        "name":fields.String(required=True,description="city name")
    })
class CountryDto:
    api=Namespace("countryDto",description="country info data")
    country_model=api.model("country",{
        "name":fields.String(required=True,description="city name")
    })
class CompanyDto:
    api=Namespace("companydto",description='company related optations')
    ref_data=api.model("ref_data",{"$oid": fields.String(description="ref_id")})
    ref_date=api.model("ref_date",{"$date": fields.Integer(description="ref date int formet")})
    pincode=api.model("pincode",{
                     "pincode":fields.Integer(description='pincode'),
                     "area":fields.String(required=True,description='area'),
                     "city":fields.Nested(ref_data,description="city info"),
                     "state":fields.Nested(ref_data,description="state info"),
                     "country":fields.Nested(ref_data,description="country info")
                  })
    address_data=api.model("address_data",{
                  "address1":fields.String(required=True,description='address'),
                  "landmark":fields.String(required=True,description='landmark'),
                  "pincode":fields.Nested(pincode,description="pincode info")
               })
    verification_auth=api.model("verification_auth",{
            "name":fields.String(required=True,description='company reg no'),
            "url":fields.List(fields.Url(description="url info")),
            "addresses":fields.Nested(address_data,description="address"),
            "verification_type":fields.String(required=True,description='verification_type')
         })
    reg_info=api.model("reginfo",{
         "reg_name":fields.String(required=True,description='company registration Name'),
         "reg_reg_no":fields.String(required=True,description='company reg no'),
         "ref_doc":fields.Nested(ref_data,description='ref_doc'),
         "verification_type":fields.String(required=True,description='reg verification type'),
         "is_verified":fields.Boolean(default=False,description='is_verified'),
         "verification_authority":fields.Nested(verification_auth,description="verification_authority")
      })
    bank_info=api.model("bank_info",{
               "bank_name":fields.String(required=True,description='bank_name'),
               "code_type":fields.String(required=True,description='code_type'),
               "code":fields.String(required=True,description='code'),
               "a_c_no":fields.String(required=True,description='a_c_no'),
               "a_c_type":fields.String(required=True,description='a_c_type'),
               "is_verified":fields.Boolean(default=False,description='is_verified')
            })
    currency=api.model("currency",{
               "name":fields.String(required=True,description='name'),
               "icon":fields.Nested(ref_data,description='icon'),
               "exchange_rate_to_usd":fields.Float(),
               "exchange_rate_to_inr":fields.Float()
            })
    branch_data=api.model("branch_data",{
         "branch_name":fields.String(required=True,description='branch_name'),
         "address":fields.Nested(address_data),
         "reg_info":fields.Nested(reg_info),
         "bank_info":fields.List(fields.Nested(bank_info)),
         "accepted_currences":fields.List(fields.Nested(currency))
      })
    company_master=api.model("company_master",{
   "comp_code":fields.String(required=True,description='company code'),
   "name":fields.String(required=True,description='company Name'),
   "Reg_info":fields.List(fields.Nested(reg_info)),
   "comp_type":fields.String(required=True,description='comp_type'),
   "branches":fields.List(fields.Nested(branch_data)),
   "bank_info":fields.List(fields.Nested(bank_info)),
   "created_on":fields.Nested(ref_date),
   "updated_on":fields.Nested(ref_date),
   "created_by":fields.Nested(ref_data)
})

