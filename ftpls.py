import os
def ftpls(host,user,password):
    cmd = './ftp_ls'+ ' ' + host + ' ' + user + ' ' + password + ' | ./get_list'
    print(cmd)
    output = os.popen(cmd)
    str = output.read()
    return str
