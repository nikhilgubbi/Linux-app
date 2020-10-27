#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
myx = mydata.getvalue("x")
o = subprocess.getoutput("sudo  " + myx )
print(o)
