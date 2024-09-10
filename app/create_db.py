from app import create_app, db
from app.models import Actor, Serie, Pelicula, Television, ActorSerie, ActorPelicula, ActorTelevision

app = create_app()

with app.app_context():
    db.create_all()
    print("Base de datos y tablas creadas exitosamente.")
