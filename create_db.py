from extensions import db
from main import create_app
from models import User

app =create_app()

app.config.from_prefixed_env()

with app.app_context():

    db.create_all() #create the db
