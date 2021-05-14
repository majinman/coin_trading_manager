from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm, func, and_, or_
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from config import getConfig

db = SQLAlchemy()

# base = declarative_base()
# engine = sqlalchemy.create_engine(getConfig().SQLALCHEMY_DATABASE_URI)
# Session = orm.sessionmaker(bind=engine)
# session = Session()
# session._model_changes = {}
#
# db.session = session
# session_factory = sessionmaker(bind=engine)
# db.session = scoped_session(session_factory)

# db.session.expire_on_commit = False