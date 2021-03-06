## Setup Node
import logging
import socket
import pip
import getpass
import pymysql
import urllib.request
import os 
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')



## Requirements for a node/ instance
# 1. A MySQL Server
# 2. Application
# 3. Consensus Algorithm

def getHostName():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        public_ip_addr = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    finally:
        return hostname, ip_address, public_ip_addr

def contactCentralNode(instance):
    ## Save details in host server
    logging.warning('Central Node Successfully Updated')

def updateDatabase(cur):
    logging.warning('Installing Blockchain onto Database')

def MySQLConnect(accountInfo):
    conn = pymysql.connect( 
        host= accountInfo['host'], 
        user= accountInfo['user'],  
        password = accountInfo['password'], 
        db= accountInfo['database'], 
        ) 
    return conn.cursor()

def getMySQLDetails():
    username = str(input('Enter Database Username (Root not recommended): '))
    password = getpass.getpass('Enter Database Password: ')
    host = str(input('Enter Database Host: '))
    port = int(input('Enter Database Port (Default 3306): '))
    database = str(input('Enter Database name: '))
    return {
        'user' : username,
        'password' : password,
        'host' : host,
        'port' : port,
        'database' : database
    }

def databaseSetUp():
    logging.info('Must be running MySQL 5.5 or above, or MariaDB 5.5 or above')
    logging.info('Attempting to Use Database Connection Package (PyMySQL)')
    accountInfo = getMySQLDetails()
    try: 
        cur = MySQLConnect(accountInfo)
    except pymysql.err.OperationalError:
        logging.error('Connection Unsuccessful, aborting and exiting')
        exit()
    else:
        cur.execute('SELECT @@version')
        logging.warning('DATABASE VERSION' + str(cur.fetchall()[0]))
        return cur
    

def setUp():    
    print ('Set Up for Blockchain Development Node')
    logging.warning('Starting Set Up for Blockchain on this Instance')
    logging.warning(getHostName()), contactCentralNode(getHostName())
    logging.warning('Starting Database Set Up. Please ensure an empty database has been created')
    cur = databaseSetUp()
    logging.warning('Updating Database')
    updateDatabase(cur)
    os.system('python main.py')


    

if __name__ == "__main__":
    setUp()
