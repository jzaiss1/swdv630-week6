# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 6 Assignment - Storing Objects in the Database

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# ORM capable Class created from the Base class
Base = declarative_base()

class Item(Base):
  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.quantity = 1
    # TODO: Increment the quantity

    __tablename__ = 'inventory'

    id = column(Integer, primary_key=True)
    name = column(String)
    price = column(Integer)
    quantity = column(Integer)
  
  def __str__(self):
        return "{}: $ {}".format(self.name, self.price)

class OrderIterator:
  def __init__(self, items):
    self.indx = 0
    self.items = items

  def has_next(self):
    return False if self.indx >= len(self.items) else True

  def next(self):
    item = self.items[self.indx]
    self.indx += 1
    return item

  def remove(self):
    return self.items.pop()

class Sale:
  def __init__(self):
    self.items = []
  
  def add(self, item):
    self.items.append(item)
  
  def iterator(self):
    return OrderIterator(self.items)


def main():
  print(sqlalchemy.__version__)
  engine = create_engine('sqlite:///:memory:', echo=True)

  Base.metadata.create_all(engine)

  Session = sessionmaker(bind=engine)
  session = Session()

main()