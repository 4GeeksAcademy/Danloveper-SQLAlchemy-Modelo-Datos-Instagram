from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False)
    email : Mapped[str] = mapped_column(String(40),)
    password : Mapped[str] = mapped_column(String(60),)
    
    posts: Mapped[list['Post']] = relationship(back_populates='user')

class Post(db.Model):
    __tablename__='post'

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    img : Mapped[str] = mapped_column(String)
    title : Mapped[str] = mapped_column(String)
    Description : Mapped[str] = mapped_column(String)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped['User'] = relationship(back_populates="autor")