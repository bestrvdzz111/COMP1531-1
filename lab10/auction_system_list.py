from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Add code to create a database engine that stores data in the local directory's library.db
engine = create_engine('sqlite:///auction.db')
Base=declarative_base()
DBsession = sessionmaker(bind =engine)
session = DBsession()

class User(Base):
    """ Table for user """
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    user_name = Column(String(255), nullable = False)
    def __str__(self):
        return "id = "+str(self.id)+ " user_name = "+self.user_name
class Post(Base):
    """ Table for all posted item """
    __tablename__ ="post"
    id = Column(Integer, primary_key= True)
    user_id = Column(ForeignKey("user.id"), nullable = False)
    item_id = Column(ForeignKey("item.id"), nullable = False)

class Bid(Base):
    """Table for Bid, record unit data of each bid."""
    __tablename__ = "bid"
    id = Column(Integer, primary_key = True)
    item_id = Column(ForeignKey("item.id"), nullable = False)
    user_id = Column(ForeignKey("user.id"), nullable = False)
    price = Column(Integer, nullable = False)

class Item(Base):
    """ Table for all the user create item informations """
    __tablename__ = "item"
    id = Column(Integer, primary_key = True)
    item_name = Column(String(255),nullable = False)
    desc = Column(String(255),nullable = False)
    user_id = Column(ForeignKey("user.id"),nullable = False)
    type = Column(String(255),nullable = False)
    # for reference to the subclasses
    __mapper_args__= {
        'polymorphic_identity':'item',
        'polymorphic_on':'type'
    }

    def __str__(self):
        string =  "id = "+ str(self.id)+" item_name = "+str(self.item_name)
        if self.type == "book" :
            string += " author = "+ self.author + " year = "+ self.publish_year
        elif self.type == "elec":
            string += " voltage = "+ str(self.voltage)+"V brand = "+ self.brand
        elif self.type == "fur":
            string += " age = "+ str(self.age) + "year material = "+ self.material


        # new line and with the bid info
        string += "\n"



        return string

class Book(Item):
    """Table for book, join search item"""
    __tablename__ = "item_book"

    id = Column(Integer, ForeignKey('item.id'),primary_key = True)
    author = Column(String(255),nullable = False)
    publish_year = Column(String(255),nullable = False)
    # for map back to item
    __mapper_args__ = {
        'polymorphic_identity':'book'
    }

class Electronic(Item):
    """Table for Electronic, join search item."""
    __tablename__ = "item_elec"
    id = Column(Integer, ForeignKey('item.id'),primary_key = True)
    voltage = Column(Integer, nullable = False)
    brand = Column(Integer, nullable = False)
    # for map back to item
    __mapper_args__ = {
        'polymorphic_identity':'elec'
    }

class Furniture(Item):
    """table for Furniture, join table item."""
    __tablename__ = "item_fur"
    id = Column(Integer, ForeignKey('item.id'),primary_key = True)
    age = Column(Integer,nullable = False)
    material = Column(String(255),nullable = False)
    # for map back to item
    __mapper_args__ = {
        'polymorphic_identity':'fur'
    }


class AuctionSystem(object):


    def register_user(self, user_id, name):
        session.add(User(id = user_id,user_name = name ))
        session.commit()
    def post_item(self, item):
        item.add()
        session.add(user_id = item.user_id, item_id = item.id)
        session.commit()


    def make_bid(self, user_id, item_id, price):
        session.add(Bid(user_id = user_id, item_id = item_id, price = price))
        session.commit()

    def get_items(self):
        for item in session.query(Item).all():
            print(item)

    def get_user(self, user_id = None):
        for user in session.query(User).all():
            print(user)

    #
    # def search_posts(self, user_id):
    #     posts = []
    #     for user in self._users:
    #         if user.id == user_id:
    #             posts = user.posts
    #     for post in posts:
    #         print(post)
    #
    # def search_user_bids(self, user_id):
    #     bids = []
    #     for user in self._users:
    #         if user.id == user_id:
    #             bids = user.bids
    #     for bid in bids:
    #         print(bid)
    #
    # def search_item_bids(self, item_id):
    #     bids = []
    #     for item in self._items:
    #         if item.id == item_id:
    #             bid = item.bid
    #     print(bid)


if __name__ == '__main__':
    # create the database
    Base.metadata.create_all(engine)

    system = AuctionSystem()
    system.register_user(1,"Jack")
    system.register_user(2,"Tom")
    system.register_user(3,"Jason")
    system.register_user(4,"David")
    session.add(Book(id = 1,item_name = "Agile Design",desc ="AnAgile Design Guide book", user_id =1, author ="Aarthi", \
                publish_year ="1996"))
    session.add(Electronic(id = 2,item_name = "Iphone7",desc ="latest iphone",user_id = 3,voltage = 220,\
                            brand = "Apple"))
    session.add(Furniture(id = 3,item_name = "Table",desc ="a nice table",user_id = 3,material = "Wood", age = 5 ))

    system.make_bid(2,1, 800)
    system.make_bid(3,1, 900)
    system.make_bid(3,2, 200)
    system.make_bid(4,2, 220)
    system.make_bid(1,2, 250)
    system.make_bid(4,2, 300)
    system.make_bid(1,2, 350)
    system.make_bid(4,1, 920)
    system.make_bid(4,3, 40)
    system.make_bid(2,3, 50)
    system.make_bid(1,3, 60)
    system.make_bid(2,3, 80)


    system.get_user()
    print("---------------------")
    system.get_items()
