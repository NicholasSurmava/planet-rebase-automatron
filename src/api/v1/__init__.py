from .site_controller import sites
from flask import (
    Blueprint, jsonify
)

api = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api.route('/')
def api_v1_index():
    return 'swagger for api'


@api.route('/heartbeat')
def api_v1_heartbeat():
    return jsonify({'heartbeat': 'badum badum badum'})


api.register_blueprint(sites)
