from pytient.pytient_app import app, db

if __name__ == "__main__":
    db.create_all()  # make our sqlalchemy tables
    app.run(debug=True, use_reloader=True)
