#ELIMINEM LOGS PESANTS 
import os
import subprocess



#----------------------------------------------
print ("-------------------------------------------------------------")
print ("")
print ("*****************")
print ("* INITIAL SIZE *")
print ("*****************")
print ("")
print subprocess.check_output("df -h | head -2",shell=True);
print ("-------------------------------------------------------------")

#----------------------------------------------
#BUIDA FITXERS LOG
os.system("cp /dev/null /var/log/debug")
os.system("cp /dev/null /var/log/kern.log")
os.system("cp /dev/null /var/syslog")
os.system("cp /dev/null /var/log/mail.*")
os.system("cp /dev/null /var/log/mail.*.*")
os.system("cp /dev/null /var/log/backup_dropbox.log")
os.system("cp /dev/null /var/log/debug")
os.system("cp /dev/null /var/log/bandwidth")
os.system("rm -r /var/log/*.gz")
os.system("rm -r /var/log/*.1")
os.system("rm -r /var/log/*.*.1")
os.system("rm -r /var/log/*.log.*")
os.system("rm -r /var/log/syslog.*.gz")
os.system("rm -r /var/log/btmp.*")




#---- neteja apt-get
print("")
print ("*********************************")
print ("* REMOVE APT-GET CACHE PACKAGES *")
print ("*********************************")
print("")
os.system("apt-get autoclean")
os.system("apt-get clean")

#----------------------------------------------
#ENVIA CORREU 
import smtplib

sender = 'denisgualda@batetdelaserra.cat'
receivers = ['denisgualda@batetdelaserra.cat']

message = """From: From Person <denisgualda@batetdelaserra.cat>
To: To Person <denisgualda@batetdelaserra.cat>
Subject: LOGS DE SISTEMA ESBORRATS

LOGS ESBORRATS
---------------------------
/var/log/debug.l")
/var/log/debug")
/var/log/kern.log")
/var/log/kern.log.l")
/var/log/*.1")
var/log/*.gz")

"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"
#----------------------------------------------

#TAMANY FINAL
print ("-------------------------------------------------------------")
print ("")
print ("**************")
print ("* FINAL SIZE *")
print ("**************")
print ("")
print subprocess.check_output("df -h | head -2",shell=True);
print ("")
print ("-------------------------------------------------------------")
