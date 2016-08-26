""" Test api module """
from .api_base import ApiBase, rest_api


@rest_api.route('/test/api', methods=['GET'])
def test_api():
    """ API for test api function """
    return ApiBase.success_repsonse('API is working')
