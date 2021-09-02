from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Base(db.Model, SerializerMixin):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True),server_default=db.func.now())

    def save(self, commit: bool = True):

        try:
            db.session.add(self)

            if commit:
                db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise e


class Rooms(Base):

    __tablename__ = 'rooms'

    key = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100), nullable=False)
    owner_name = db.Column(db.String(100), nullable=True)
    owner_email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.Text, nullable=True)
    is_admin = db.Column(db.Boolean, default=True)
    #create_at = db.Column(db.DateTime(timezone=True),server_default=db.func.now())

    def __init__(self, name: str, key: str) -> None:
        super().__init__()
        self.name = name
        self.key = key

    def __repr__(self) -> str:
        return '<Room %r>' % self.name


    @staticmethod
    def get_by_key(key:str):
        
        room: dict = {}
        room = Rooms.query.filter_by(key=key).first()

        return room
    



def init_app(app):
    db.init_app(app)
