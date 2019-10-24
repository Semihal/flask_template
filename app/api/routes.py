from flask import jsonify, make_response

from . import api_bp


@api_bp.route('/message', methods=['GET'])
def index():
    return make_response(jsonify(messge='Hello world!'), 200)
