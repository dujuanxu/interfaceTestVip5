'''
加载所有的测试用例
运行用例并生成报告
发送邮件通知
'''

#加载所有的测试用例

import unittest
import os
import HTMLTestRunner
from common.configEmail import ConfigEmail

p = os.path.abspath(__file__)
# dirname = os.path.dirname(p)
dirname = os.path.dirname(p)
p = dirname + r'\testCase'

def create_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir=p,
        pattern='test*.py',
        top_level_dir=None)
    return  discover

if __name__ == '__main__':
    suite =create_suite()
    file_path = dirname + r'\report' + r'\testReport.html'

    with open(file_path, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='My unit test',description='This demonstrates the report output by HTMLTestRunner.')

        runner.run(suite)

    cf_email = ConfigEmail()
    cf_email.sendMail()

