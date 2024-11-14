from time import sleep
import requests

class ClientCore:
    #client request setup

    def __init__(self):
        self.base_url = "https://api.artifactsmmo.com"
        self.base_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    #post req
    def _post(self, url='', data=None):
        return self._do_request(method='post', url=url, data=data)
    

    #get req
    def _get(self, url='', data=None):
        return self._do_request(method='get', url=url, data=data)
    

    def _processRequest(self, method='get', url='', data=None):
        params = {
            'method': method,
            'url': self.base_url + url,
            'headers': self.base_headers,
        }

        if method == 'get':
            params.update(params=data or {})
        elif method == 'post':
            params.update(json=data or {})

        while True:
            try:
                print("Pass")
                request = requests.request(**params)
                request.json()
                break
            except (requests.exceptions.ConnectionError, requests.exceptions.JSONDecodeError):
                sleep(1)
                continue

        return request