from api import db


class DrawnCards(db.Model):
    __tablename__ = 'drawn_cards'
    uuid = db.Column(db.String(150), primary_key=True, nullable=False)
    name = db.Column(db.String(100))
    amount = db.Column(db.Integer)
    player_uuid = db.Column(db.String(150), db.ForeignKey("players.uuid"), nullable=False, index=True)
