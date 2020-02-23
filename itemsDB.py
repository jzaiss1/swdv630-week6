# John Zaiss (GitHub id jzaiss1)
# SWDV 630: OBJECT-ORIENTATED CODING 1W 20/SP1
# Week 6 Assignment - Storing Objects in the Database

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

# ORM capable Class created from the Base class
Base = declarative_base()

class Item(Base):
  def __init__(self, date, name, quantity, price):
    self.name = name
    self.price = price
    self.quantity = quantity
    # TODO: Increment the quantity

  __tablename__ = 'inventory'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  price = Column(Float)
  quantity = Column(Integer)
  
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

  session.add_all([
    Item{'2016-05-03 00:00:00','12oz Drinking Jar w Lid & Straw',1,2},
    Item{'2017-05-09 00:00:00','1950''s Sip n Snack Illistrated Napkins',1,8},
    Item{'2017-07-20 00:00:00','1980 Cardinals Media Guide',1,3.75},
    Item{'2017-07-08 00:00:00','1987 Cardinals T-Shirt',1,4},
    Item{'2017-04-23 00:00:00','1987 Donruss Cardinals Team Set',1,2},
    Item{'2017-03-18 00:00:00','1987 Topps Cardinals Team Set',1,2},
    Item{'2016-05-05 00:00:00','1988 & 89 Score Wax Packs',1,1.5},
    Item{'2017-09-05 00:00:00','1988 Fleer Cardinals Team Set',1,2},
    Item{'2017-05-18 00:00:00','1988 Score Wax Packs',1,1.5},
    Item{'2017-04-08 00:00:00','1988 Topps Cardinals Team Set',1,2},
    Item{'2017-05-23 00:00:00','1988 Topps Wax Packs',1,1.75},
    Item{'2017-10-21 00:00:00','1989 Topps Cardinals Team Set',1,2},
    Item{'2017-09-04 00:00:00','1989 Topps Wax Packs',1,1.75},
    Item{'2016-05-19 00:00:00','1990 & 91 Donruss Wax Packs',1,1.25},
    Item{'2017-02-19 00:00:00','1990 & 91 Fleer Wax Packs',1,1.5},
    Item{'2017-06-16 00:00:00','1990 Donruss Wax Packs',1,5.25},
    Item{'2017-08-10 00:00:00','1990 Donruss Wax Packs',1,1.5},
    Item{'2017-09-05 00:00:00','1990 Topps Cardinals Team Set',1,2},
    Item{'2017-05-18 00:00:00','1990 Topps Wax Packs',1,1.75},
    Item{'2017-05-08 00:00:00','1991 Fleer Cardinals Team Set',1,1.5},
    Item{'2016-06-04 00:00:00','1991 Fleer Ultra & ProSet Wax Packs',1,1.25},
    Item{'2017-03-04 00:00:00','1991 Fleer Ultra & Score Wax Packs',1,1.25},
    Item{'2016-10-17 00:00:00','1991 Score & ProSet Wax Packs',1,1.25},
    Item{'2016-11-19 00:00:00','1994 World Series Ball',1,9},
    Item{'2017-08-18 00:00:00','2 Bird Bottles',1,6},
    Item{'2016-02-14 00:00:00','3 ft. Coax',1,1},
    Item{'2016-03-26 00:00:00','3 Rings',1,2.5},
    Item{'2017-06-30 00:00:00','4ft Mini USB',1,2},
    Item{'2017-04-23 00:00:00','4x6 Silver Wedding Frame',1,3},
    Item{'2016-04-25 00:00:00','6ft USB',1,3},
    Item{'2016-08-20 00:00:00','78 RPM Record',3,1.25},
    Item{'2016-03-18 00:00:00','90-91 & 91-92 Opee-Chee Hockey Wax Packs',1,1.25},
    Item{'2016-03-13 00:00:00','All Star T Shirt',1,9},
    Item{'2017-08-07 00:00:00','Aluminium Measuring Spoons',1,1.5},
    Item{'2017-09-03 00:00:00','Aluminum Color Craft Pitcher',1,2},
    Item{'2017-06-13 00:00:00','Aluminum Nursery Rhyme Cup',1,4},
    Item{'2017-11-21 00:00:00','American girl Doll Patio Table',1,12},
    Item{'2016-10-11 00:00:00','Antique Cabbage Cutter',1,10},
    Item{'2017-02-28 00:00:00','Antique J7 iron/club',1,20},
    Item{'2016-05-22 00:00:00','Bacon Press',1,7},
    Item{'2017-09-02 00:00:00','Bakers mix instant chocolate tin',1,2.75},
    Item{'2016-12-11 00:00:00','Baseball Card Lot',1,1},
    Item{'2017-03-17 00:00:00','baseball cards',1,3},
    Item{'2016-11-19 00:00:00','Batman Forever 4 pc Set',1,18},
    Item{'2017-03-25 00:00:00','Batting Helmet',1,5},
    Item{'2017-01-23 00:00:00','Bear Decanter',1,10},
    Item{'2016-06-03 00:00:00','Bills Glass',1,2},
    Item{'2017-03-02 00:00:00','Bird Scenery jar w handle',1,3},
    Item{'2016-06-24 00:00:00','Black & Glass Crystal Chandelier',1,20},
    Item{'2017-06-22 00:00:00','Black Metal Hanging Organizers',2,3.75},
    Item{'2016-11-12 00:00:00','Blue Boy Milk Bottle',1,10},
    Item{'2017-08-05 00:00:00','Blue Jar',1,2},
    Item{'2016-06-14 00:00:00','Blue Owl Vases',2,5},
    Item{'2017-05-28 00:00:00','Blue Speckled Enamel Cake Pan',1,6},
    Item{'2017-04-21 00:00:00','Blues Media Guide',1,5},
    Item{'2017-11-12 00:00:00','Blues Media Guide',8,5},
    Item{'2016-02-20 00:00:00','Blues Team Set',1,2.5},
    Item{'2016-05-05 00:00:00','Boat Trip DVD',1,2.25},
    Item{'2017-02-03 00:00:00','Brass & colbalt blue glass candleholder',1,2.25},
    Item{'2017-02-03 00:00:00','Brass Butterfly Waste Basket w Liner',1,15},
    Item{'2017-08-19 00:00:00','Brass Switch',1,5},
    Item{'2017-08-20 00:00:00','Brass/Wood Mallards',1,15},
    Item{'2017-08-25 00:00:00','Bud Glass',1,2},
    Item{'2017-10-19 00:00:00','Bud Glass',1,2},
    Item{'2017-11-24 00:00:00','Bud Glass',1,2},
    Item{'2016-12-24 00:00:00','Bud Light Bottle',1,5},
    Item{'2017-01-22 00:00:00','Bud Light Bottle',1,5},
    Item{'2016-02-03 00:00:00','Bud Light Spuds MacKenzie Mug',1,7},
    Item{'2016-04-11 00:00:00','Bud Light Spuds MacKenzie Mug',1,1.75},
    Item{'2016-09-03 00:00:00','Bumper Sticker',1,0.6},
    Item{'2017-03-31 00:00:00','Carage',1,19},
    Item{'2017-10-05 00:00:00','Cardinals button',1,2.5},
    Item{'2017-03-24 00:00:00','Cardinals Dog Bowl',1,2},
    Item{'2017-07-13 00:00:00','Cardinals Hat',1,2},
    Item{'2017-11-06 00:00:00','Cardinals Hat',1,2},
    Item{'2017-03-28 00:00:00','Cardinals Metal Sign',1,3.5},
    Item{'2016-03-13 00:00:00','Cardinals Rocks Glass',1,3.25},
    Item{'2016-03-13 00:00:00','Cardinals Rocks Glass',1,3.25},
    Item{'2017-08-13 00:00:00','Cardinals Team Set',1,2.5},
    Item{'2017-08-31 00:00:00','Cardinals Team Set',3,2.5},
    Item{'2017-08-31 00:00:00','Cardinals Team Set',1,3},
    Item{'2016-06-11 00:00:00','Cardinals Team Set',1,3},
    Item{'2016-07-02 00:00:00','Cardinals Team Set',1,3},
    Item{'2016-07-25 00:00:00','Cardinals Team Set',1,3},
    Item{'2016-08-26 00:00:00','Cardinals Team Set',1,3},
    Item{'2016-08-26 00:00:00','Cardinals Team Set',1,3},
    Item{'2016-08-26 00:00:00','Cardinals Team Set',1,3},
    Item{'2017-03-28 00:00:00','Cardinals Team Set',1,2.5},
    Item{'2017-03-08 00:00:00','Carnival Glass Plate',1,4},
    Item{'2017-09-13 00:00:00','Carona Beer Bucket',1,3},
    Item{'2017-09-22 00:00:00','Carona Extra Beer Bucket',1,3},
    Item{'2016-08-20 00:00:00','Caro-nan Wooden Hand Bag',1,8},
    Item{'2017-06-27 00:00:00','Cast Iron Corn Bread Pan',1,6},
    Item{'2016-04-30 00:00:00','Ceiling Speaker Wire',1,3.5},
    Item{'2016-08-13 00:00:00','Charger',1,3},
    Item{'2017-04-10 00:00:00','Chick Chimney',1,7},
    Item{'2016-06-06 00:00:00','Chicken Sponge Holder',1,3},
    Item{'2017-04-02 00:00:00','Childrens Reusable Shopping Bag',1,1},
    Item{'2017-06-13 00:00:00','Childrens Reusable Shopping Bag',1,1},
    Item{'2017-06-29 00:00:00','Childrens Reusable Shopping Bag',1,1},
    Item{'2016-08-13 00:00:00','Chinco Tray Strawberry Shortcake',1,8},
    Item{'2017-07-23 00:00:00','Clifford DVD',1,2.5},
    Item{'2017-05-16 00:00:00','Colonial Viper',1,3},
    Item{'2016-11-19 00:00:00','Colorodo Rockies Termo Cup',1,2},
    Item{'2017-07-20 00:00:00','Coors Field Ball',1,5},
    Item{'2017-04-08 00:00:00','Copper & Brass Brushes Can',1,5},
    Item{'2016-12-07 00:00:00','Copper Bucket w porcelian handles',1,25},
    Item{'2017-05-27 00:00:00','Copper Chicken Wire Basket',1,3.75},
    Item{'2017-10-17 00:00:00','Death to Smoochy DVD',1,3},
    Item{'2017-02-09 00:00:00','Desk',1,60},
    Item{'2017-04-14 00:00:00','Diary of a Wimpy Kid Dog Days DVD',1,2.5},
    Item{'2017-04-14 00:00:00','Diary of a Wimpy Kid DVD',1,2.5},
    Item{'2016-07-11 00:00:00','Disney Book',1,10},
    Item{'2016-05-08 00:00:00','Disney VHS',1,3},
    Item{'2017-07-17 00:00:00','Disney VHS',1,3},
    Item{'2017-08-04 00:00:00','Dodgeball DVD',1,2.5},
    Item{'2017-09-13 00:00:00','Dos Equis Beer Bucket',1,3},
    Item{'2017-03-31 00:00:00','DVD',2,3},
    Item{'2016-08-03 00:00:00','Enamel Bowl w Red Trim',1,12},
    Item{'2017-09-02 00:00:00','Enamel Cup with lid "Crabby''s"',1,3.25},
    Item{'2017-05-22 00:00:00','Evan Almighty DVD',1,2.5},
    Item{'2017-04-12 00:00:00','Face Powls',4,2},
    Item{'2017-10-21 00:00:00','Fenton Art Glass Bell',1,4},
    Item{'2016-05-19 00:00:00','Fenton Milk Glass Creamer',1,4},
    Item{'2016-05-12 00:00:00','Fenton Milk Glass Sugar Bowl',1,4},
    Item{'2017-03-04 00:00:00','Football Card Set Chiefs',1,2.5},
    Item{'2017-03-18 00:00:00','Football Card Set Chiefs',1,2.5},
    Item{'2017-04-04 00:00:00','Football Card Set Chiefs',2,2.5},
    Item{'2016-08-27 00:00:00','Full Size Bed Spread',1,13.5},
    Item{'2017-06-22 00:00:00','Glass ',1,5},
    Item{'2017-09-30 00:00:00','Glass & Brass Oil Lantern',1,11.7},
    Item{'2017-06-14 00:00:00','Glass & Silver Plate/Stand',1,3},
    Item{'2016-06-18 00:00:00','Glass Boot Mug',1,2},
    Item{'2017-09-29 00:00:00','Glass Bottle',1,6},
    Item{'2016-06-18 00:00:00','Glass Dairy Milk Jug',1,1.25},
    Item{'2016-08-13 00:00:00','Glass Dairy Milk Jug',1,1.25},
    Item{'2017-06-30 00:00:00','Glass Jar with Red Seal & Clamp Lid',1,2.5},
    Item{'2017-10-22 00:00:00','Glass Jar with Red Seal & Clamp Lid',1,2.5},
    Item{'2017-04-20 00:00:00','Gold Glove Baseball',1,10},
    Item{'2017-07-06 00:00:00','Gold Star Decoration',1,9},
    Item{'2016-06-15 00:00:00','Green Ball Pint Jars',2,2},
    Item{'2016-04-11 00:00:00','Green Chalkboard',1,0.5},
    Item{'2016-04-30 00:00:00','Green Chalkboard',1,2},
    Item{'2016-04-08 00:00:00','Green tupperware w lid',1,2},
    Item{'2017-05-15 00:00:00','H & K Coffee Can',1,2.25},
    Item{'2017-07-07 00:00:00','Hammer',1,4},
    Item{'2017-10-01 00:00:00','Heavy Busch Mug',1,3},
    Item{'2017-10-01 00:00:00','Heavy Busch Mug',1,3},
    Item{'2017-10-01 00:00:00','Heavy Busch Mug',1,3},
    Item{'2017-05-27 00:00:00','Highlander DVD',1,1.88},
    Item{'2017-02-19 00:00:00','Home sign with boxwood wreath',1,12},
    Item{'2017-04-22 00:00:00','Hoosier Glass Vase',1,1},
    Item{'2017-04-22 00:00:00','How to Train Your Dragon 2 DVD',1,3},
    Item{'2017-04-22 00:00:00','How to Train Your Dragon DVD',1,3},
    Item{'2017-06-26 00:00:00','iPhone 5s',1,1.25},
    Item{'2017-03-28 00:00:00','iPhone 5s Case',1,1.25}])

main()