'''
1.导入email的包
2.配置邮件的基本属性（发送人，接收人，邮件标题，用户名，密码，邮件服务器）
    添加附件
3.创建邮件发送实例
4.连接邮件服务器
5.发送邮件
'''
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import ReadConfig
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class ConfigEmail(object):

    def setupBox(self):
        self.cf = ReadConfig()

        self.sender = self.cf.get_mail('sender')
        self.receiver = self.cf.get_mail('receiver')
        self.smtpserver = self.cf.get_mail('smtpserver')
        self.username = self.cf.get_mail('username')
        self.passwd = self.cf.get_mail('passwd')

    def setupContent(self):
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        subject = '自动化测试结果_'+t
        content = '测试报告见附件'

        #文本内容
        msg = MIMEText(content, 'plain', 'utf-8')

        #添加附件
        htmlPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),r'report\testReport.html')
        print(htmlPath)
        htmlFilename = os.path.basename(htmlPath)
        print(htmlFilename)
        reportApart = MIMEApplication(open(htmlPath, 'rb').read())
        reportApart.add_header('Content-Disposition', 'attachment', filename=htmlFilename )

        #打包文本内容和附件内容,加标题，form,to
        self.m = MIMEMultipart()
        self.m.attach(msg)
        self.m.attach(reportApart)
        self.m['Subject'] = Header(subject, 'utf-8')
        self.m['From'] = self.sender
        self.m['To'] = self.receiver

    def sendMail(self):
        self.setupBox()
        self.setupContent()

        try:
            s = smtplib.SMTP()
            s.connect(self.smtpserver)
            s.login(self.username,self.passwd)
            s.sendmail(self.sender,self.receiver, self.m.as_string())
        except BaseException as m:
            print("邮件发送失败",m)
        else:
            print("邮件发送成功")
        finally:
            s.quit()


if __name__ == '__main__':
    cf_email = ConfigEmail()
    cf_email.sendMail()

