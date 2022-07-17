import mysql.connector as connection

#Establish a communication
mydb = connection.connect(host='localhost', user='root', passwd='8009')

#cursor creation
cursor = mydb.cursor()

#query
#cursor.execute('create database kamlesh')
#cursor.execute('show databases')
#cursor.execute('create table kamlesh.CompanyInformation(CompanyName varchar(80), CompanyWorkingIn varchar(80))')
#cursor.execute('select * from kamlesh.basicinformation')
cursor.execute('insert into kamlesh.basicinformation values("Kamlesh")')
cursor.execute('insert into kamlesh.CompanyInformation values("Valmet Technologies", "Industrial Automation")')
mydb.commit()

cursor.execute('select * from kamlesh.CompanyInformation')

for i in cursor.fetchall():
    print(i)

