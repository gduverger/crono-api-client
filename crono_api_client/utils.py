import json
import datetime

def encode_datetime(obj):

	if isinstance(obj, datetime.datetime):
		# ISO 8601 formatted UTC date and time
		return obj.isoformat()

	else:
		type_name = obj.__class__.__name__
		raise TypeError(f"Object of type '{type_name}' is not JSON serializable")

class DatetimeEncoder(json.JSONEncoder):

	def default(self, obj):

		if isinstance(obj, datetime.datetime):
			# ISO 8601 formatted UTC date and time
			return obj.isoformat()

		return json.JSONEncoder.default(self, obj)
