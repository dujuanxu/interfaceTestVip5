
import requests

class ConfigHttp(object):

    def get(self, url, param):
        r = requests.get(url=url, params=eval(param))
        return r


    def post(self, url, param):
        r = requests.post(url=url, data= eval(param))
        return r


    def getRequest(self, url, method,param):
        if method == 'get':
            return self.get(url, param)
        elif method == 'post':
            return self.post(url,param)