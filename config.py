# configuration
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/issue_tracking_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
