import os
def ftp_test(host,user,password):
    cmd = './auto_ftp'+ ' ' + host + ' ' + user + ' ' + password + ' | ./getList'
    print(cmd)
    output = os.popen(cmd)
    str = output.read()
    return str
