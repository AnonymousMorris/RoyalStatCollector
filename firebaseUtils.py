import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databseURL": "https://royalscrape-e1868-default-rtdb.firebaseio.com/"})

root = db.reference("/")

# page is whether it's trending, rising stars, or best rated, etc..
def add_snapshot(time, page, fictions):
    root = db.reference("/")
    root.push({"time": time, "page": page, "fictions": fictions})