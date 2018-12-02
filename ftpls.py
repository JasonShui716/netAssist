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
                <p><a class='back' href='/back'>..Back to prev directory</a></p>
    """
    str += output.read()
    str += """
            <script>
                window.onload=function(){
	                var dirList = document.querySelectorAll('a.dir');
                    console.log(dirList);
                    dirList.forEach(function(dirItem){
                        dirItem.setAttribute("href",document.URL+dirItem.text);		
                        console.log(dirItem.getAttribute("href"));
                    });
                }
            </script>
            </body>
        </html>
    """

    return str
