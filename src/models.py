import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorite_people = relationship('Favorite_People', backref="user")
    favorite_planet = relationship('Favorite_Planet', backref="user")
    favorite_starship = relationship('Favorite_Starship', backref="user")


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250))
    height = Column(Integer, nullable=False)
    favorite_people = relationship('Favorite_People', backref="people")
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer, nullable=False)
    climate = Column(String(255), nullable=False)
    favorite_planet = relationship('Favorite_Planet', backref="planet")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)
    model= Column(String(250), nullable=False)
    favorite_starship = relationship('Favorite_Starship', backref="starship")
    

class Favorite_People(Base):
    __tablename__ = 'favorite_people'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    people_id= Column(Integer, ForeignKey('people.id'))

class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    planet_id= Column(Integer, ForeignKey('planet.id'))

class Favorite_Starship(Base):
    __tablename__ = 'favorite_starship'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))
    starship_id= Column(Integer, ForeignKey('starship.id'))

    def to_dict(self):
        return {}


