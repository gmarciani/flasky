from service.common.utils import AdvancedJSONEncoder as JSONEncoder
from json import dumps


def to_json(data):
    return dumps(data, cls=JSONEncoder)