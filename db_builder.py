#August Ray Jones
#09 DB Builder


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
course = csv.DictReader(open("courses.csv"))
command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)"          
c.execute(command)    
for row in course:
#	print row
	command = "INSERT INTO courses VALUES ('"+row['code']+"',"+row['mark']+","+row['id']+")"          
	c.execute(command)    


peeps = csv.DictReader(open("peeps.csv"))
command = "CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)"          
c.execute(command)    
for row in peeps:
#	print row
	command = "INSERT INTO peeps VALUES ('"+row['name']+"',"+row['age']+","+row['id']+")"          
	c.execute(command)    
#==========================================================
db.commit() #save changes
db.close()  #close database

