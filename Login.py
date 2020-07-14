#!/usr/bin/env python3
#importing system
import sys
import logging
import datetime

x = datetime.datetime.now()

LOG_FILENAME = 'Logs.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

username = "Username"
password = "Password"

for i in range(2):
    usr = input("Username: ")
    i = 2
    if(usr == username):
        print("Username is correct!")
        break
    else:
        logging.debug('Failed User Login ' + str(datetime.datetime.now()))
        sys.exit("Please try again later")
        continue

for i in range(3):
    pwd = input("Password: ")
    j=3
    if(pwd == password):
        print("welcome!")
        logging.debug('Successful User Login ' + str(datetime.datetime.now()))
        break
    else:
        logging.debug('Failed User Login ' + str(datetime.datetime.now()))
        sys.exit("Please try again later")
        continue

