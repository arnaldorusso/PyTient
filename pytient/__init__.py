from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask("pytient")
# app.config.from_object('pytient.config')
app.config["MONGODB_SETTINGS"] = {'DB': "dbpacientes"}
app.config["SECRET_KEY"] = "S333cr3t"

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from pytient.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
        app.run()


