from flask_login import UserMixin

class User(UserMixin):
    """docstring for User."""
    def __init__(self, user_id):
        super(User, self).__init__()
        self.user_id = user_id
    def is_authenticated(self ):
        pass
    def is_active(self, arg):
        pass
    def is_anoymous(self, arg):
        pass
    def get_id(self):
        return self.user_id
