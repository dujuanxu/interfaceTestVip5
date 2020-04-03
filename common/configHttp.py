
import requests

class ConfigHttp(object):

    def get(self, url, param):
        r = requests.get(url=url, params= eval(param))
        status_code = r.status_code
        error_code = r.json()['errorCode']

        return status_code,error_code


    def post(self, url, param):
        r = requests.post(url=url, data= eval(param))
        # print(r)
        status_code = r.status_code
        error_code = r.json()['errorCode']
        return status_code, error_code


    def run(self, url, method,param):
        if method == 'get':
            return self.get(url, param)
        elif method == 'post':
            return self.post(url,param)