import databases
import sqlalchemy

DATABASE_URL = "sqlite:///store.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(32)),
                         sqlalchemy.Column("surname", sqlalchemy.String(32)),
                         sqlalchemy.Column("email", sqlalchemy.String(128)),
                         sqlalchemy.Column("password", sqlalchemy.String(32)),
                         )


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
