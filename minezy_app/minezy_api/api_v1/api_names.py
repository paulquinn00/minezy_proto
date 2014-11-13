from minezy_api import app
from api_common import support_jsonp, query_params
from query_names import query_names
from flask import jsonify, request
from flask.ext.cache import Cache


@app.route('/1/names/', methods=['GET'])
@app.route('/1/<int:account>/names/', methods=['GET'])
@app.cache.cached(timeout=300) 
@support_jsonp
def names(account=None):
    params = query_params(request)
    resp = query_names(account, params)
    return jsonify( { 'names' : resp } )


@app.route('/1/names/count/', methods=['GET'])
@app.route('/1/<int:account>/names/count/', methods=['GET'])
@app.cache.cached(timeout=300) 
@support_jsonp
def names_count(account=None):
    params = query_params(request)
    resp = query_names(account, params, countResults=True)
    return jsonify( { 'names' : resp } )
    
