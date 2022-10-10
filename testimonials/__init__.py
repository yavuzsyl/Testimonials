from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# DB_NAME = os.environ.get('RDS_DB_NAME')
# DB_USERNAME = os.environ.get('RDS_USERNAME')
# DB_PASSWORD = os.environ.get('RDS_PASSWORD')
# DB_HOSTNAME = os.environ.get('RDS_HOSTNAME')

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://testimonials:q9OkCVqzYloxnsOPakjC@testimonials.c9z8hhscom0a.us-east-1.rds.amazonaws.com/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from testimonials.models import Testimonial

db.create_all()
testimonial = Testimonial(name="alkiv", testimonial="selam")
db.session.add(testimonial)
db.session.commit()
import testimonials.routes

# LGcKcqA4DakCcCPRcXrj