#!/usr/bin/python3

import cgi,cgitb
cgitb.enable()
# to recv data from web http protocol

print("Content-type:text/html")
print("")


html_data=cgi.FieldStorage()
#only looking for form data and those variables data as well
select=html_data.getvalue('s')


if select == "whp" :
     print("<meta http-equiv='refresh'  content='0;url=http://3.86.241.155/whp.html'>")

else :
   print("<meta http-equiv='refresh'  content='0;url=http://3.86.241.155/whm.html'>")
