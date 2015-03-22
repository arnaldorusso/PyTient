from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask("pytient")
# app.config.from_object('pytient.config')
app.config["MONGODB_SETTINGS"] = {'DB': "dbpacientes"}
app.config["SECRET_KEY"] = "S333cr3t"

db = MongoEngine(app)


if __name__ == '__main__':
        app.run()


