#!/usr/bin/python3

import cgi
# to recv data from web http protocol

print("Content-type:text/html")
print("")


html_data=cgi.FieldStorage()
#only looking for form data and those variables data as well

tech=html_data.getvalue('t')

if tech == "docker" :
     print("<meta http-equiv='refresh'  content='0;url=http://3.86.241.155/service.html' >")

else :
    print("<meta http-equiv='refresh'  content='0;url=http://3.86.241.155/service.html' >")
