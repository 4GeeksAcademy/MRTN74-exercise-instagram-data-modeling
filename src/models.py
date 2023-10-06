import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))


class Follow(Base):
    __tablename__ = 'follow'
    id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.id'))
    user_id2 = Column(Integer, ForeignKey('user.id'))


class Feeditem(Base):
    __tablename__ = 'feed_item'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    Content = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
