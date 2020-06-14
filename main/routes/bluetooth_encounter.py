import json
from flask import request
from main import mongo
from flask_restful import Resource
from ..schemas.bluetooth_encounter import BluetoothEncounterSchema
from ..services.db import DbOperations


bluetooth_encounter = mongo.ohioh.bluetooth_encounter
db = DbOperations(collections=bluetooth_encounter, schema=BluetoothEncounterSchema)


class BluetoothEncounterList(Resource):
    def get(self):
        return db.find_all()

    def post(self):
        payload = request.get_json()
        return db.insert(payload)


class BluetoothEncounter(Resource):
    def get(self, user_id):
        return db.find_one(
            criteria={'user_id': user_id}
        )

    def put(self, user_id):
        payload = request.get_json()
        return db.update(
            criteria={'user_id': user_id},
            update=payload
        )

    def delete(self, user_id):
        return db.delete(
            criteria={'user_id': user_id}
        )
