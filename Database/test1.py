import mysql.connector as connection

#Establish a communication
mydb = connection.connect(host='localhost', user='root', passwd='8009')

#cursor creation
cursor = mydb.cursor()

cursor.execute('select CompanyName, CompanyWorkingIn from kamlesh.companyinformation')

new_list = []
for i in cursor.fetchall():
    new_list.append(i)

print(new_list)