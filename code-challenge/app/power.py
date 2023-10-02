from config import db


class Power(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    power_heroes = db.relationship('HeroPower', backref='power', lazy=True)