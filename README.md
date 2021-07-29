# Mailsender
A tool for sending emails to websites that are vulnerable  to stored XSS attacks
#the source code for the tool

import smtplib, ssl
import time

col1 = '\033[32m'
col2 = '\033[31m'
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
print (col1 + "[+]Make sure you already have a dispatch email before sending this mail: \nAnd i will not be held for whatever damage is done by this tool.")
time.sleep(8)
sender_email = input("[+]Enter your attacking email: ")
reciever_email = input(col2 + "[+]Enter victim email:  ")
msg = input("[+]Enter your message and hit enter:  ")
password = input("Type your password and press enter: ")
time.sleep(8)
# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, msg)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 

#requirements..

#smtplib
lxml
#os
#python
bs4

#the fancy update and upgrade scripts..

#!/bin/bash

apt update
echo "UPDATED SUCCESSFULLY!!!"
sleep 0.5
apt upgrade -y
echo"UPGRADED SUCCESFULLY!!"
sleep 0.7
apt install figlet
apt install toilet
apt install fish
echo "Finsh installed.. successfull \nNow type fish.."
clear
echo "Done.. now type 'bash install.sh' to get the necessary requirements to run this tool!  "
clear
toilet -f mono12 -F gay Xylofon

echo "THIS TOOL WAS CREATED BY XYLOFON MENDY "

figlet mailsender👹👿
echo "[+]NOW TYPE 'python mailsender.py' TO START THE TOOL "
