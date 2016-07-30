from app import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    races = db.relationship('Race', backref='runner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>' .format(self.races)


class Race(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    raceinfo = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    def __repr__(self):
        return '<Race {}>' .format(self.raceinfo)

