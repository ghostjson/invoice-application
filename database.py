import sqlite3
import json
import sys
import eel

DB = "./database.db"

#execute query against database
@eel.expose
def dbGET(query):

	print("dbGET execution started\n\n\n")
	print("Query going to execute is " + query + "\n\n\n")

	conn = sqlite3.connect( DB )
	conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name'] 
	db = conn.cursor()

	rows = db.execute(query).fetchall()

	formated = json.dumps([ dict(ix) for ix in rows] )

	conn.commit()
	conn.close()

	print("result is " + formated + "\n\n\n")

	print("dbGET execution finished" + "\n\n\n")
   
	return formated
