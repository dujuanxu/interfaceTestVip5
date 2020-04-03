#1.比较2个版本version1"1.12.1"和"1.12.3"哪个版本号大

def get_max_version(version1, version2):
    l1 = version1.split('.')
    l2 = version2.split('.')

    i = 0
    while i < len(l1) and i <len(l2):
        if int(l1[i]) > int(l2[i]):
            return version1
        elif int(l1[i]) < int(l2[i]):
            return version2
        i += 1
    return version1

#测试方法
# print(get_max_version('1.3.3', '1.12.2'))


#2.下面是我们的日志文件,里面都是一条条这样的数据
# 为了将读取的日志文件存入mysql,我们需要读取日志文件,然后按照指定格式切割出需要的数据
# 表字段会是time, ip , level, message
# 2019-11-24 16:46:35,  10.0.101.11,  4,  AltenoOS <appsvc>:Certiificate WebManagementCert has expire1
def read_log(path):
    data = []
    with open(path,'r') as f:
        for line in f:
            a = line.split(',')
            print(a, type(a))
            # print(time,ip, level,msg)




read_log('D:\PycharmProjects\interfaceTestVip5\log.txt')