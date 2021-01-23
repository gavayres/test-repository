from app import app
from db import db

db.init_app(app)

@app.before_first_request  # runs below method before first request to app is made
def create_tables():
    db.create_all()