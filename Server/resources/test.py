from flask_restful import Resource
from flask import request, jsonify
import logging


__author__= 'Peixi Zhao'

'''
    This is just a test resource
'''



class Test(Resource):
    logger = logging.getLogger('root')

    def post(self):
        new_mytest = request.json
        return "Received"


    def get(self, str=None):
        if not str:
            return {'Test': 'Empty'}
        self.logger.info("Received %s", str)
        response = jsonify(data=[])
        response.status_code = 404
        return {'Test': str}


