from sqlalchemy import (
    Column,
    Unicode,
    DateTime,
    Index,
    Integer
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime)

    def __init__(self, *args, **kwargs):
        """Modify the init method to do more things."""
        super(MyModel, self).__init__(*args, **kwargs)

    def to_dict(self):
        """Take all model distrubutes and render them as dict."""
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'creation_date': self.creation_date.strftime('%m/%d/%Y')
        }
# Index('my_index', MyModel.name, unique=True, mysql_length=255)
