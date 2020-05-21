from flask import Blueprint
from .bluetooth_encounter import BluetoothEncounterList, BluetoothEncounter
from flask_restful import Api

from .beat import Beat

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/ohioh/api/v1')

api.add_resource(Beat, '/')
api.add_resource(BluetoothEncounterList, '/bluetooth-encounter')
api.add_resource(BluetoothEncounter, '/bluetooth-encounter/<user_id>')
