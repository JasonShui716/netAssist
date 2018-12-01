from flask import url_for
import os
def ftpls(host,user,password,directory):
    cmd = './ftp_ls'+ ' ' + host + ' ' + user + ' ' + password + ' ' + directory + ' | ./get_list | python3 sort.py'
    print(cmd)
    output = os.popen(cmd)
    str = """
        <html>
            <head>
                <link rel='stylesheet' href= """ + url_for('static',filename='custom.css') + """>
            </head>
            <body>
    """
    str += output.read()
    str += """
                <script type="text/javastript" src=""" + url_for('static', filename='make_dir.js') + """></script>
            </body>
        </html>
    """

    return str
