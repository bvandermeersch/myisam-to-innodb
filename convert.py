#!/usr/bin/python
#Convert MySQL Database from MyISAM to InnoDB
#
#Might need to install MySQLdb package
#pip install MySQL-python
#
#created by Brandon Vander Meersch
 
import MySQLdb
 
def engineListMYISAM():
    #get list of mysiam tables
    cur.execute("SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = '%s' AND engine = 'MyISAM'" % (DataBase))
    return
 
def engineListInnoDB():
    #get list of innodb tables
        cur.execute("SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA = '%s' AND engine = 'InnoDB'" % (DataBase))
    return
 
def createDBConnect(hostName, userName, DBpassword, DataBase):
    #create DB connection
    db = MySQLdb.connect(host=hostName,         # host, usually localhost
                     user=userName,             # username
                     passwd=DBpassword,         # password
                     db=DataBase)               # name of the database
    return db
 
def printList():
    #Print the list
    for row in cur.fetchall():
            print row[0]
    return
 
#Get Database info from user
hostName = raw_input('Host(localhost): ')
userName = raw_input('User Name(root): ')
DBpassword = raw_input('Password: ')
DataBase = raw_input('Database: ')
 
db = createDBConnect(hostName, userName, DBpassword, DataBase)
 
# Create Cursor objects. This will let you execute all the queries you need
cur = db.cursor()
cur2 = db.cursor()
 
engineListMYISAM()
 
print "\nMyIASM Tables\n----------------------"
printList()
print "----------------------"
question = raw_input('Would you like to convert these tables to InnoDB? (y/n): ')
if (question == "y"):
    print "----------------------\nConverting MyISAM to InnoDB..."
    engineListMYISAM()
    #Loop through list
    for row in cur.fetchall():
        tableName = row[0]
        #Convert
        cur2.execute("ALTER TABLE %s ENGINE = InnoDB" % (tableName))
        print tableName + " --> Converted!"
        #Commit the change
        db.commit()
 
    print "\nInnoDB Tables\n----------------------"
    #List the InnoDB tables
    engineListInnoDB()
    printList()
    print "----------------------\nComplete!"
else:
    print "---------------------\nConversion Cancelled!"
db.close()
