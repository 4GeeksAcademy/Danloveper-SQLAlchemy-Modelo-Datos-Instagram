from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    #fields
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False)
    email : Mapped[str] = mapped_column(String(40),)
    password : Mapped[str] = mapped_column(String(60),)
    
    #relation
    posts: Mapped[list['Post']] = relationship(back_populates='user')
    comments: Mapped[list['Comment']] = relationship(back_populates='user')

class Post(db.Model):
    __tablename__ = 'post'

    #fields
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    img : Mapped[str] = mapped_column(String)
    title : Mapped[str] = mapped_column(String)
    description : Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    #relation
    user: Mapped['User'] = relationship(back_populates="posts")
    tags: Mapped[list['Tag']] = relationship(secondary="post_tag", back_populates='posts')
    comments: Mapped[list['Comment']] = relationship(back_populates='post')

class Tag(db.Model):
    __tablename__ = 'tag'

    #fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    color: Mapped[str] = mapped_column(String)

    #relation
    posts: Mapped[list['Post']] = relationship(secondary="post_tag", back_populates='tags')


class Comment(db.Model):
    __tablename__ = 'comment'

    #fields
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))

    #relation
    user: Mapped['User'] = relationship(back_populates='comments')
    post: Mapped['Post'] = relationship(back_populates='comments')

post_tag = Table(
    "post_tag",
    db.metadata,
    Column("post_id", ForeignKey("post.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"),primary_key=True)
)