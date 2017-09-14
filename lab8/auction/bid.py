from item import item


class bid_node(object):
    """docstring for bid_node."""
    def __init__(self):
        super(bid_node, self).__init__()
        self.__bid_id
        self.__start_time
        self.__item_id
        self.__bid_history
    def get_start_time(self):
        pass
    def set_start_time(self, time):
        pass
    def get_item_id(self):
        pass
    def set_bid(self,price,user_id):
        pass
    def set_bid_id(self, arg):
        pass
    def get_bid_id(self):
        pass
    def is_close_bid(self):
        pass
    def get_winner(self):
        pass

class bid(object):
    """docstring for bid."""
    def __init__(self):
        super(bid).__init__()
        #  store all the bid_node
        bids ={}
    def create_bid(self, item_id):
        pass
    def show_item(self):
        pass
    def has_win_bid(self, user_id):
        pass
