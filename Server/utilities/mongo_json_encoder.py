__author__ = 'Peixi Zhao'

import json
from bson.objectid import ObjectId


# Custom JSONEncoder that extracts the strings from MongoDB ObjectIDs


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)
