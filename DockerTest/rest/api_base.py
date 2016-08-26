""" Base API app module """
import json
import time
from flask import Response, Blueprint
from flask import g


rest_api = Blueprint('rest', __name__, url_prefix='/rest')


@rest_api.before_request
def before_request():
    """ before filter for api response time """
    g.start = time.time()


class ApiBase:
    """ Base API for app response """
    @staticmethod
    def success_repsonse(data):
        """ Base API for success response """
        result = {'success': True, data: data, 'error': None, 'rcode': None,
                  'processingTime': time.time()-g.start}
        return Response(json.dumps(result), status=200, mimetype='application/json')
