import pyrebase
import json
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore


#from grandeurs.models import Grandeur, Mesure 

firebase_config = {
    "apiKey": "AIzaSyAOhDGvMEiidRc_uObr3Ul0Vb5aU1A2BSA",
    "authDomain": "flutterfirebaseapp-e151d.firebaseapp.com",
    "databaseURL": "https://flutterfirebaseapp-e151d-default-rtdb.firebaseio.com",
    "projectId": "flutterfirebaseapp-e151d",
    "storageBucket": "flutterfirebaseapp-e151d.firebasestorage.app",
    "messagingSenderId": "173148386558",
    "appId": "1:173148386558:web:b646c093f09098fd1621af",
}

firebase=pyrebase.initialize_app(firebase_config)
database=firebase.database()


#init firestore
cred = credentials.Certificate(r"C:\pc-nizar\django_firebase_certif\firebase_private_certif.json")
firebase_admin.initialize_app(cred)

db_firestore = firestore.client()

def persistData(message):
    #Firebase: RealTime DB
    json_object = json.loads(message)
    json_object['time']= str(datetime.now())
    # Firebase Realtime db persist data
    database.child('temperature').push(json_object)
    # Firebase firestore persist data
    doc_ref = db_firestore.collection("temperature").document()
    doc_ref.set(json_object)
