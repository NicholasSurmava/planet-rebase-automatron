from flask import (
    Blueprint, flash, g, redirect, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from ..core.forager.warehouse import Site_Forager

api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/get_towers')
def get_towers():

    tower_forager = Site_Forager('alarmDB', 'Towers')

    towers = tower_forager.get_towers()

    return jsonify(towers)
