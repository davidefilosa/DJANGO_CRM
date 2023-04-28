import mysql.connector

dataBase = mysql.connector.connect(host="localhost", user='root', passwd='290784df')

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE app")

print("ALL done")