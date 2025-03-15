import datetime
import sqlalchemy
# from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


# from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    email = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    # jobs = orm.relationship("Jobs", back_populates='user')
    #
    # def set_password(self, password):
    #     self.hashed_password = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.hashed_password, password)
    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'