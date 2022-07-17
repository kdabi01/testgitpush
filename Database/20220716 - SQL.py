import mysql.connector as connection

#Establish a communication
mydb = connection.connect(host='localhost', user='root', passwd='8009')

#cursor creation
cursor = mydb.cursor()