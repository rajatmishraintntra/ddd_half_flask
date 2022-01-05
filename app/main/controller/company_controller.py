from flask import request
from flask.wrappers import Response
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, permission,token_required
from ..util.dto import CityDto, CompanyDto, CountryDto, StateDto
from ..service.company_service import *
from typing import Dict, Tuple

company_api=CompanyDto.api
_company=CompanyDto.company_master
city_api=CityDto.api
_city=CityDto.city_model
state_api=StateDto.api
_state=StateDto.state_model
country_api=CountryDto.api
_country=CountryDto.country_model
@company_api.route('/')
class CompanyApi(Resource):
    @company_api.doc('List all Companies')
    def get(self):
        """List all Companies"""
        return get_all_companies()

    @company_api.expect(_company, validate=True)
    @company_api.response(201, 'Company successfully created.')
    @company_api.doc('create a new Company')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Company """
        data = request.json
        return save_a_company(data=data)

@company_api.route('/<id>')
@company_api.param('id', 'The User identifier')
@company_api.response(404, 'User not found.')
class CompanyApiUpdate(Resource):
    @company_api.doc("Get a Company")
    @company_api.doc('get a user')
    @company_api.marshal_with(_company)
    def get(self,id):
        """Get a Company"""
        return get_a_company(id=id)
    @company_api.expect(_company,validate=True)
    @company_api.response(206,"Permissions Updated")
    @company_api.param("id","the permission identifier")
    @company_api.doc("update_a_Permissions")
    def put(self,id):
        """Update a Company"""
        data=request.json
        return update_a_company(id=id,data=data)


@city_api.route('/')
class CityApi(Resource):
    @city_api.doc('List all city')
    def get(self):
        """List all city"""
        return get_all_cities()

    @city_api.expect(_city, validate=True)
    @city_api.response(201, 'City successfully created.')
    @city_api.doc('create a new City')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new City """
        data = request.json
        return save_city(data=data)

@city_api.route('/<id>')
@city_api.param('id', 'The city identifier')
@city_api.response(404, 'city not found.')
class CityApiUpdate(Resource):
    @city_api.doc("Get a City")
    @city_api.doc('get a city')
    @city_api.marshal_with(_city)
    def get(self,id):
        """Get a City"""
        return get_a_city(id=id)
    @city_api.expect(_company,validate=True)
    @city_api.response(206,"City Updated")
    @city_api.param("id","the City identifier")
    @city_api.doc("update_a_City")
    def put(self,id):
        """Update a City"""
        data=request.json
        return update_a_city(id=id,data=data)


@state_api.route('/')
class StateApi(Resource):
    @state_api.doc('List all state')
    def get(self):
        """List all state"""
        return get_all_states()

    @state_api.expect(_state, validate=True)
    @state_api.response(201, 'state successfully created.')
    @state_api.doc('create a new state')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new state """
        data = request.json
        return save_a_state(data=data)

@state_api.route('/<id>')
@state_api.param('id', 'The state identifier')
@state_api.response(404, 'state not found.')
class StateApiUpdate(Resource):
    @state_api.doc("Get a state")
    @state_api.doc('get a state')
    @state_api.marshal_with(_state)
    def get(self,id):
        """Get a City"""
        return get_a_state(id=id)
    @state_api.expect(_state,validate=True)
    @state_api.response(206,"state Updated")
    @state_api.param("id","the state identifier")
    @state_api.doc("update_a_state")
    def put(self,id):
        """Update a state"""
        data=request.json
        return update_a_state(id=id,data=data)



@country_api.route('/')
class CountryApi(Resource):
    @country_api.doc('List all country')
    def get(self):
        """List all country"""
        return get_all_country()

    @country_api.expect(_country, validate=True)
    @country_api.response(201, 'country successfully created.')
    @country_api.doc('create a new country')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new country """
        data = request.json
        return save_a_country(data=data)

@country_api.route('/<id>')
@country_api.param('id', 'The country identifier')
@country_api.response(404, 'country not found.')
class CountryApiUpdate(Resource):
    @country_api.doc("Get a country")
    @country_api.doc('get a country')
    @country_api.marshal_with(_country)
    def get(self,id):
        """Get a country"""
        return get_a_country(id=id)
    @country_api.expect(_state,validate=True)
    @country_api.response(206,"country Updated")
    @country_api.param("id","the country identifier")
    @country_api.doc("update_a_country")
    def put(self,id):
        """Update a country"""
        data=request.json
        return update_a_country(id=id,data=data)