
from app.utils.calculate import calc


old_users = ['user1', 'user2']
new_users = ['user3', 'user4']


def count_users():
    return calc(old_users, new_users)
