from datetime import datetime

from yacut import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def from_dict(self, data):
        dict_field = {'url': 'original', 'custom_id': 'short'}
        for field in dict_field:
            if field in data:
                setattr(self, dict_field[field], data[field])

    def to_dict(self):
        return dict(
            url=self.original,
            custom_id=self.short
        )
