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
