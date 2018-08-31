import requests
import json
import os


class CyRESTInstance:
    """ Parameters that describe CyREST """

    _PORT = 1234
    _BASE_URL = "http://localhost"

    def __init__(self, base_url=None, port=None):
        """ Constructor remembers CyREST location """
        if base_url is None:
            base_url = os.getenv("CYREST_URL", CyRESTInstance._BASE_URL)
        if port is None:
            port = os.getenv("CYREST_PORT", CyRESTInstance._PORT)
        self.port = port
        self.base_url = base_url


class CyCaller:
    """Basic functions for calling CyREST"""

    def __init__(self, cy_rest_instance=None):
        """Constructor remembers CyREST location and NDEx credentials"""
        if cy_rest_instance is None:
            cy_rest_instance = CyRESTInstance()
        self.cy_rest_instance = cy_rest_instance

    @staticmethod
    def _return_ci_json(result):
        """Pulls CI data out of a result or throws an exception"""
        return_json = CyCaller._return_json(result)
        if type(return_json) != dict:
            return return_json

        errors = return_json["errors"]
        if len(errors) == 0:
            return return_json["data"]
        else:
            raise Exception(errors)

    @staticmethod
    def _return_json(result):
        """Return JSON if the call was successful, or an exception if not"""
        try:
            return_json = result.json()
        except Exception:
            raise Exception("Failed to parse json from " + str(result.content))
        return return_json

    def _execute(self, http_method, endpoint, data=None, params=None):
        """Set up a REST call with appropriate headers, then return result"""
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        if type(data) == dict:
            data = json.dumps(data)

        result = requests.request(http_method,
                                  self.cy_rest_instance.base_url + ":" + str(self.cy_rest_instance.port) + endpoint,
                                  data=data,
                                  params=params,
                                  headers=headers)
        return CyCaller._return_json(result)

    def post(self, endpoint, data=None):
        """Execute a REST call using POST"""
        return self._execute("post", endpoint, data)

    def put(self, endpoint, data=None):
        """Execute a REST call using PUT"""
        return self._execute("put", endpoint, data)

    def get(self, endpoint, params=None):
        """Execute a REST call using GET"""
        return self._execute("get", endpoint, params=params)

    def delete(self, endpoint, data=None):
        """Execute a REST call using DELETE"""
        return self._execute("delete", endpoint, data=data)
