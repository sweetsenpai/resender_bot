import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()


class Bans(Base):
    __tablename__ = 'bans'
    word_id = sql.Column(name='ban_id', type_=sql.Integer, primary_key=True)
    word = sql.Column(name='user_id', type_=sql.Integer)

    def __int__(self, ban_id, user_id):
        self.ban_id = ban_id
        self.user_id = user_id

    def __repr__(self):
        return f'{self.ban_id} : {self.user_id}'


basedir = os.path.abspath(os.path.dirname(__file__))
sqlite_url = "sqlite:///" + os.path.join(basedir, "bans.db")
engine = sql.create_engine(sqlite_url, echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
