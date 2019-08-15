import os

#SHOW LOG SIZE
torigen = os.system("du -h /var/log")

print torigen


#emtpy blog file
os.system("cp /dev/null /var/log/debug.l")
os.system("cp /dev/null /var/log/debug")
os.system("cp /dev/null /var/log/kern.log")
os.system("cp /dev/null /var/log/kern.log.l")
os.system("cp /dev/null /var/log/*.1")
os.system("rm -r /var/log/*.gz")




#SEND EMAIL WHEN FINISH
import smtplib

sender = '***who send mail **** '
receivers = ['*** mail to send ***']

message = """From: From Person <****who send mail ****>
To: To Person <*** mail to send **** >
Subject: LOGS DE SISTEMA ESBORRATS

{torigen}
LOGS ESBORRATS

- Buidar (fitxer) /var/log/debug.l
- Buidar (fitxer) /var/log/debug
- Buidar (fitxer) /var/log/kern.log
- Buidar (fitxer) /var/log/kern.log.1
- Buidar (fitxer) /var/log/*.1
- Eliminar /var/log/*.gz


"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
