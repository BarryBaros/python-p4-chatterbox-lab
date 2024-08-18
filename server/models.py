from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
import pytz

# Define East African Time timezone
EAT = pytz.timezone('Africa/Nairobi')

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

def get_eat_now():
    return datetime.now(EAT)

class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=get_eat_now)
    updated_at = db.Column(db.DateTime, onupdate=get_eat_now, default=get_eat_now)

    def __repr__(self):
        return f'<Message {self.body[:20]} by {self.username}>'
