#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
from http.cookies import SimpleCookie

#CREATE SIMPLE LOGIN FORM

#set up cgi form
s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

#check if correct login info provided to cgi form
form_ok = username == secret.username and password == secret.password

#set up cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

#check if cookie username/password == secret username/password
cookie_ok = cookie_username == secret.username and cookie_password == secret.password

#... then set username/pass to cookie username/pass
if cookie_ok:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_ok:
    #set cookie iff login info is correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()


#from this point on, everything prints to html
#print("Content-Type: text/html")
#print()

#load login page, print user form info
if not username and not password:
    print(login_page())
elif username == secret.username and password == secret.password:
    print(secret_page(username, password))
else:
    print(after_login_incorrect())
