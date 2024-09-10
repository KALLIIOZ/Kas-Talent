from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Modelo de Actores
class Actor(db.Model):
    __tablename__ = 'actores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    biografia = db.Column(db.Text, nullable=False)
    foto1 = db.Column(db.String(255))  # Ruta de la foto 1
    foto2 = db.Column(db.String(255))  # Ruta de la foto 2
    foto3 = db.Column(db.String(255))  # Ruta de la foto 3
    foto4 = db.Column(db.String(255))  # Ruta de la foto 4
    curriculum = db.Column(db.String(255))  # Ruta del archivo PDF del currículum
    video = db.Column(db.String(255))  # Ruta del video del actor
    
    # Relaciones
    series = db.relationship('ActorSerie', back_populates='actor')
    peliculas = db.relationship('ActorPelicula', back_populates='actor')
    television = db.relationship('ActorTelevision', back_populates='actor')

# Modelo de Series
class Serie(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(255))  # Ruta de la imagen de la serie

# Relación Actor-Serie
class ActorSerie(db.Model):
    __tablename__ = 'actor_series'
    actor_id = db.Column(db.Integer, db.ForeignKey('actores.id'), primary_key=True)
    serie_id = db.Column(db.Integer, db.ForeignKey('series.id'), primary_key=True)
    actor = db.relationship('Actor', back_populates='series')
    serie = db.relationship('Serie')

# Modelo de Películas
class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(255))  # Ruta de la imagen de la película

# Relación Actor-Película
class ActorPelicula(db.Model):
    __tablename__ = 'actor_peliculas'
    actor_id = db.Column(db.Integer, db.ForeignKey('actores.id'), primary_key=True)
    pelicula_id = db.Column(db.Integer, db.ForeignKey('peliculas.id'), primary_key=True)
    actor = db.relationship('Actor', back_populates='peliculas')
    pelicula = db.relationship('Pelicula')

# Modelo de Televisión
class Television(db.Model):
    __tablename__ = 'television'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    imagen = db.Column(db.String(255))  # Ruta de la imagen del programa de TV

# Relación Actor-Televisión
class ActorTelevision(db.Model):
    __tablename__ = 'actor_television'
    actor_id = db.Column(db.Integer, db.ForeignKey('actores.id'), primary_key=True)
    television_id = db.Column(db.Integer, db.ForeignKey('television.id'), primary_key=True)
    actor = db.relationship('Actor', back_populates='television')
    television = db.relationship('Television')
