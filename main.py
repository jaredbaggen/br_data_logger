from ftplib import FTP
import os

FTP_HOST = '192.168.125.50'
FTP_USER = 'dev'
FTP_PASSWD = 'dev'
LOG_DIR = 'F:\DataLog\Logs\General'


# Establish the connection and log in
ftp = FTP(host=FTP_HOST)
ftp.login(user=FTP_USER, passwd=FTP_PASSWD)

# Set the current directory
ftp.cwd(dirname=LOG_DIR)

# Try to transfer log.csv
try:
    log = ftp.retrlines(cmd='RETR ' + 'log.csv')
except IOError as e:
    print(e)

print(log)