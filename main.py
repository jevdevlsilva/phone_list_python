from utils import notify, break_line, separator, clear
import time
import users_services

users = users_services.get()


def close_app():
    notify('Closing the App.')
    time.sleep(0.2)
    notify('Closing the App..')
    time.sleep(0.2)
    notify('Closing the App...')
    return


def save_edit():
    user_to_edit = int(input('Choose an user to edit: '))
    user = users_services.get_by_id(user_to_edit)
    update_user = {}
    notify(f'Editing {user["name"]}')
    notify(f'Register the new name:')
    update_user['name'] = input()
    notify(f'Register the new email:')
    update_user['email'] = input()
    notify(f'Register the new phone:')
    update_user['phone'] = input()
    update_user['id'] = user['id']
    if user['name'] and user['email'] and user['phone']:
        users_services.put(update_user)
    else:
        notify('Invalid data')


def save_user():
    clear()
    new_user = {}
    notify("Let's register a new user")
    notify("Enter  the name: ")
    new_user['name'] = input()
    notify("Enter the email: ")
    new_user['email'] = input()
    notify("Enter the phone: ")
    new_user['phone'] = input()
    new_user['id'] = users[-1]['id'] + 1

    if new_user['name'] and new_user['email'] and new_user['phone']:
        users_services.post(new_user)
    else:
        notify('Invalid user')


def main_menu():
    options = ['Quit', 'Show list', 'Register', 'Edit', 'Delete']
    notify('Choose a action'.title())
    break_line()
    for index, option in enumerate(options):
        notify(f'[{index}] {option}')
    break_line()
    action = int(input())

    if action == 0:
        close_app()
    elif action == 1:
        show_users()
        back_menu()
    elif action == 2:
        save_user()
        back_menu()
    elif action == 3:
        show_users()
        save_edit()
        back_menu()
    elif action == 4:
        show_users()
        delete_user()
        back_menu()
    else:
        print('Opção invalida')


def back_menu():
    options = ['quit', 'back to main Menu']
    separator()
    for index, option in enumerate(options):
        notify(f'Press [{index}] for {option}')
    break_line()
    action_sub_menu = int(input())
    separator()
    if action_sub_menu == 0:
        close_app()
    else:
        main_menu()


def show_users():
    clear()
    all_users = users_services.get()
    if len(all_users) > 0:
        notify('All Contacts')
        break_line()
        for user in users:
            notify(f'{user["id"]} |  Name: {user["name"]} | Email: {user["email"]} | Phone: {user["phone"]}')
        break_line()
    else:
        notify('No contacts')


def delete_user():
    global users
    user_to_delete_id = int(input('Choose an user to delete: '))
    user_to_delete = users_services.get_by_id(user_to_delete_id)
    if user_to_delete:
        users_services.delete(user_to_delete)


def main():
    clear()
    separator()
    notify('Welcome to Phone List'.upper())
    separator()
    break_line()
    main_menu()


main()
