import db_fake
from utils import notify

users = db_fake.users_entity


def get():
    return users


def get_by_id(user_id):
    find_user = [user for user in users if user['id'] == user_id]
    if find_user:
        return find_user[0]
    else:
        return False


def get_user_by_email(email):
    find_user = list(filter(lambda user: user['email'] == email, users))
    if find_user:
        return find_user[0]
    else:
        return False


def post(user):
    finder_user = get_user_by_email(user['email'])
    if finder_user:
        notify(f'User with email {user["email"]} already registered')
    else:
        users.append(user)
        notify('New contact successfully saved!')


def put(user_to_edit):
    finder_user = get_by_id(user_to_edit['id'])
    if finder_user:
        for user in users:
            if user['id'] == user_to_edit['id']:
                user['name'] = user_to_edit['name']
                user['email'] = user_to_edit['email']
                user['phone'] = user_to_edit['phone']
        notify(f'Contact updated as success!')
    else:
        notify('User not found!')


def delete(user_to_delete):
    global users
    finder_user = get_by_id(user_to_delete['id'])
    if finder_user:
        users = list(filter(lambda contact: contact['id'] != user_to_delete['id'], users))
        notify('Successfully deleted contact!')
    else:
        notify('User not found!')
