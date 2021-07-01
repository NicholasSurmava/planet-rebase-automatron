from flask import (
    Blueprint, jsonify
)
from ...core.forager.warehouse import Site_Forager

sites = Blueprint('sites', __name__, url_prefix='/sites')


@sites.route('/get_towers')
def get_towers():

    tower_forager = Site_Forager('alarmDB', 'Towers')

    towers = tower_forager.get_towers()

    return jsonify(towers)
