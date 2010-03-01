from google.appengine.ext import db

class MyEntity(db.Model):
  name = db.StringProperty()
