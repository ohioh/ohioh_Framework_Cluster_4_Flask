import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class BluetoothEncounterSchema(Schema):
    user_id = ms_fields.Str()
    encounter_user_id = ms_fields.Str()
    date_time = ms_fields.DateTime(default=datetime.datetime.now())

    class Meta:
        unknown = EXCLUDE


