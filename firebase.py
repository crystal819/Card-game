import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://cardgame-9f35f-default-rtdb.europe-west1.firebasedatabase.app/"})

ref = db.reference('/') #gets a reference to the root note in the database
ref.get() #returns all of the data from the database
 
#<node_ref>.set() overrides an existing nodes value with something
#<node_ref>.update() can add new key value pairs