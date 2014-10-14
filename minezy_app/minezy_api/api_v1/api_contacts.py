from minezy_api import app
from api_common import support_jsonp, query_params
from query_contacts import query_contacts
from flask import jsonify, request, redirect, url_for


@app.route('/1/contacts/', methods=['GET'])
@app.route('/1/<int:account>/contacts/', methods=['GET'])
@support_jsonp
def contacts(account=None):
    params = query_params(request)
    resp = query_contacts(account, params)
    return jsonify( { 'contacts' : resp } )


@app.route('/1/contacts/count/', methods=['GET'])
@app.route('/1/<int:account>/contacts/count/', methods=['GET'])
@support_jsonp
def contacts_count(account=None):
    params = query_params(request)
    resp = query_contacts(account, params, countResults=True)
    return jsonify( { 'contacts' : resp } )
    