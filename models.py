from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
db_uri = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
db = create_engine(db_uri)

session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=db))

base = declarative_base()
# We will need this for querying
base.query = session.query_property()
base.metadata.create_all(db)


class Post(base):
    __tablename__ = 'posts'

    title = Column(String)
    body = Column(String)
    userId = Column(Integer)
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "user_id": self.userId,
            "body": self.body
        }


class Comment(base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    postId = Column(Integer, ForeignKey("posts.id"))
    name = Column(String)
    email = Column(String)
    body = Column(String)
    createdAt = Column(String)
    updatedAt = Column(String)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "post_id": self.postId,
            "body": self.body,
            "email": self.email,
            "created_at": self.createdAt,
        
        }
