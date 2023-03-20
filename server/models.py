from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Mission(db.Model, SerializerMixin):
    __tablename__ = 'missions'

    serialize_rules = ('-planet', '-scientist',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    scientist_id = db.Column(db.Integer, db.ForeignKey('scientists.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    # scientist = db.relationship('Scientist', back_populates='missions')

    @validates('name')
    def validates_name(self, key, value):
        if not value:
            raise ValueError('Name must be provided.')
        return value

    @validates('scientist_id')
    def validates_scientist_id(self, key, value):
        scientists = Scientist.query.all()
        ids = [scientist.id for scientist in scientists]
        # missions = Mission.query.all()
        if not value:
            raise ValueError('Scientist must be provided.')
        elif not value in ids:
            raise ValueError('Scientist must exist.')

        return value

    @validates('planet_id')
    def validates_planet_id(self, key, value):
        planets = Planet.query.all()
        ids = [planet.id for planet in planets]
        if not value:
            raise ValueError('planet must be provided.')
        elif not value in ids:
            raise ValueError('planet must exist.')
        return value

    def __repr__(self):
        return f'<Mission id:{self.id}, scientist_id: {self.scientist_id}, planet_id: {self.planet_id}, name: {self.name}>'


class Scientist(db.Model, SerializerMixin):
    __tablename__ = 'scientists'

    serialize_rules = ('-missions', '-created_at', '-updated_at', )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    field_of_study = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    @validates('name')
    def validates_name(self, key, value):
        scientists = Scientist.query.all()
        names = [scientist.name for scientist in scientists]
        if not value:
            raise ValueError('Name must be provided.')
        elif value in names:
            raise ValueError('Name already exists.')
        return value

    @validates('field_of_study')
    def validates_field_of_study(self, key, value):
        if not value:
            raise ValueError('Field of study must be provided.')
        return value

    missions = db.relationship(
        'Mission', backref='scientist', cascade="all, delete, delete-orphan")
    planets = association_proxy('missions', 'planet')


class Planet(db.Model, SerializerMixin):
    __tablename__ = 'planets'

    serialize_rules = ('-missions', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    distance_from_earth = db.Column(db.String)
    nearest_star = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now())

    missions = db.relationship('Mission', backref='planet')
    scientists = association_proxy('missions', 'scientist')
