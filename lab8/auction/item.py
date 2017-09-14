class item_type(object):
    """docstring for item_type."""
    def __init__(self):
        super(item_type, self).__init__()
        __type_list =[]
    def get_type_name(self, id):
        pass
    def set_new_type(self,name):
        pass
    def get_type_id(self,name):
        pass

class item_node(object):
    """docstring for item_node."""
    def __init__(self,id,name,type,description,owner):
        super(item_node, self).__init__()
        self.__type_id
        self.__name
        self.__description
        self.__owner_id
    def get_type(self):
        pass
    def set_type(self):
        pass
    def get_name(self, arg):
        pass
    """.... i don't want to write the getter and setter"""


class item(object):
    """docstring for item."""
    def __init__(self):
        super(item, self).__init__()
        self.items = {}
    def add_type(self,typename):
        pass
    def create_item(self):
        pass
    def get_item(self):
        pass
