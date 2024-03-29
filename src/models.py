from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class People(db.Model):
    __tablename__ = 'peoples'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    thumbnail = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(255), default="")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,  
            "description": self.description,
            "thumbnail": self.thumbnail,
            "image": self.image
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    thumbnail = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String(255), default="")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,  
            "description": self.description,
            "thumbnail": self.thumbnail,
            "image": self.image
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorite_People(db.Model):
    __tablename__ = 'favorites_peoples'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    peoples_id = db.Column(db.Integer, db.ForeignKey("peoples.id"))

    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,  
            "peoples_id": self.peoples_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Favorite_Planet(db.Model):
    __tablename__ = 'favorites_planets'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
   
    def serialize(self):
        return {
            "id": self.id,
            "users_id": self.users_id,  
            "planets_id": self.planets_id,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()