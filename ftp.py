import os
def ftp_test(host,user,password):
    cmd = '../nginx/html/auto_ftp'+ ' ' + host + ' ' + user + ' ' + password + ' | ../nginx/html/getList'
    print(cmd)
    output = os.popen(cmd)
    str = output.read()
    return str
