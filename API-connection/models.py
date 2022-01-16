from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()

migrate = Migrate()

class User(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String, nullable=False)
    profile = DB.Column(DB.String)
    currency = DB.Column(DB.String)
    launched_at = DB.Column(DB.BigInteger, nullable=False)
    created_at = DB.Column(DB.BigInteger, nullable=False)
    goal = DB.Column(DB.Float, nullable=False)
    state = DB.Column(DB.String, nullable=False)

    def __repr__(self):
        return "<User: {}>".format(self.name)


class Pledge(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    converted_pledged_amount = DB.Column(DB.BigInteger)
    pledged = DB.Column(DB.Float, nullable=False)
    usd_pledged = DB.Column(DB.Float, nullable=False)
    vect = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
            "user.id"), nullable=False)

    user = DB.relationship("User", backref=db.backref("pledge", lazy=True))


def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON
    Param: database_records (a list of db.Model instances)
    Example: parse_records(User.query.all())
    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records