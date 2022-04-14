import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    mail = Column(String, unique=True)
    password = Column(String)
    bio = Column(String, nullable=True)


class Post(Base):
    __tablename__ = 'Post'

    Post_id = Column(Integer, primary_key=True)

    User_id = Column(Integer, ForeignKey('User.id'))
    Description = Column(String, nullable=True)


class Media(Base):
    __tablename__ = 'Media'

    Media_id = Column(Integer, primary_key=True)
    Post_id = Column(Integer, ForeignKey('Post.Post_id'))
    Source_Media = Column(String)
    # preguntar por enum si es por tipo de formato del file
    Type_Media = Column(Enum)


class Comment(Base):
    __tablename__ = 'Comment'

    Comment_id = Column(Integer, primary_key=True)
    Post_id = Column(Integer, ForeignKey('Post.Post_id'))
    User_id = Column(Integer, ForeignKey('User.id'))
    Comment = Column(String)


class Followers(Base):
    __tablename__ = 'Followers'

    Followers_id = Column(Integer, primary_key=True)
    User_From_id = Column(Integer, ForeignKey('User.id'))
    User_To_id = Column(Integer, ForeignKey('User.id'))


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
