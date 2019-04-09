from app import db
import datetime

class RoboticProcessAutomation(db.Model):
    __tablename__ = "bots"
    rpa_id = db.Column(db.Unicode(36), primary_key=True, unique=True)
    rpa_name = db.Column(db.Unicode(120))
    creation_date = db.Column(db.DateTime())

    def __repr__(self):
        return '<RPA %r>' % self.rpa_name

class RPALogs(db.Model):
    __tablename__ = "logs"
    rpa_id = db.Column(db.Unicode(36), db.ForeignKey('bots.rpa_id'))
    log_id = db.Column(db.Unicode(36), primary_key=True, unique=True)
    idx = db.Column(db.Integer)
    message = db.Column(db.Unicode(120))
    tag = db.Column(db.Unicode(20))
    timestamp = db.Column(db.DateTime())
    tz = db.Column(db.Unicode(40))

    def __repr__(self):
        return '<Log %r>' % self.log_id