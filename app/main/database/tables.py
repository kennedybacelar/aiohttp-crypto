from sqlalchemy import TIMESTAMP, Column, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, default=None)
    currency = Column(String)
    date_ = Column(TIMESTAMP)
    price = Column(Float)

    def to_dict(self):
        return {
            "id": self.id,
            "currency": self.currency,
            "date_": self.date_.isoformat(),
            "price": self.price,
        }

    def __repr__(self):
        return f"<Currency(id={self.id}, currency={self.currency}, date_={self.date_}, price={self.price})>"
