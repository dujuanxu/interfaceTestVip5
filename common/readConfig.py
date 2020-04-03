
import configparser
import os

filepath = os.path.abspath(__file__)
conf_dirpath = os.path.dirname(os.path.dirname(filepath))
conf_name = r'config.ini'
conf_file_path = os.path.join(conf_dirpath, conf_name)
print(conf_file_path)

class ReadConfig(object):
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(conf_file_path, encoding='utf-8-sig')

    def get_http(self, name):
        re = self.conf.get('HTTP', name)
        return re

    def get_data(self, name):
        re = self.conf.get('DATA',name)

    def get_mail(self, name):
        re = self.conf.get('EMAIL', name)
        return re

if __name__ == '__main__':
    rc = ReadConfig()
    sender = rc.get_mail('sender')
    # print(sender)
    rc.get_http('baseurl')
    rc.get_http('port')




