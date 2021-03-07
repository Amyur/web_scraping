from sqlalchemy import Column, String, Integer

from base import Base 

class Article(Base):
	__tablename__ = "articles"

	id = Column(Integer, primary_key=True)
	name = Column(String)
	price = Column(Integer)

	def __init__(self, idx, name, price):
		self.idx = idx
		self.name = name
		self.price = price

