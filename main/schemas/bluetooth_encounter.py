from datetime import datetime

from marshmallow import Schema, EXCLUDE
import marshmallow.fields as ms_fields


class BluetoothEncounterSchema(Schema):
    user_id = ms_fields.Str(required=True)
    user_timestamp = ms_fields.DateTime(default=datetime.now())
    encounter_user_id = ms_fields.Str(default="")

    class Meta:
        unknown = EXCLUDE


