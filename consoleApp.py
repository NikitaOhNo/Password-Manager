from Passwords import PasswordManager
from config import password, options

passwordManager = PasswordManager()


def print_block(platform, login, password):
    print('\n' + '+' + '-' * 40 + '+')
    print(f'|Platform: {platform}\n|Login: {login}\n|Password: {password}')
    print('+' + '-' * 40 + '+')


while input('Password: ') != password:
    print('Incorect password')
    continue
else:
    print(options)
    while True:
        option = input('\nChose the option: ')
        if option == 'cr':
            password = passwordManager.create_random_password()
            platform = input('Platform: ')
            login = input('Login: ')
            passwordManager.insert_login_data_to_db(platform, login, password)
            print_block(platform, login, password)

        elif option == 'cwoc':
            chosed_chars = input('Chars: ')
            password = passwordManager.password_without_chosed_chars(chosed_chars)
            platform = input('Platform: ')
            login = input('Login: ')
            passwordManager.insert_login_data_to_db(platform, login, password)
            print_block(platform, login, password)

        elif option == 'cwc':
            chosed_chars = input('Chars: ')
            password = passwordManager.password_with_chosed_chars(chosed_chars)
            platform = input('Platform: ')
            login = input('Login: ')
            passwordManager.insert_login_data_to_db(platform, login, password)
            print_block(platform, login, password)

        elif option == 'sa':
            all_db_data = passwordManager.get_everything_from_db()
            if all_db_data != []:
                print('\n' + '+' + '-' * 40 + '+')
                for item in all_db_data:
                    platform, login, password = item
                    print(f'|Platform: {platform}\n|Login: {login}\n|Password: {password}')
                    print('+' + '-' * 40 + '+')
            else:
                print('DB is empty')

        elif option == 'ss':
            while True:
                platform = input('Planform name: ')
                all_db_data = passwordManager.get_data_by_name(platform)
                if all_db_data != None:
                    platform, login, password = all_db_data
                    print_block(platform, login, password)
                    break

                elif platform == 'exit':
                    break

                else:
                    print('No such key in db')

        elif option == 'change password':
            while True:
                exist_platforms = passwordManager.gel_all_platform_names_from_db()
                platform = input('Platform: ')
                if platform in exist_platforms:
                    option = input('Do you need a password (y/n): ')
                    if option == 'n':
                        password = input('Password: ')
                        passwordManager.update_password(platform, password)
                        break
                    elif option == 'y':
                        while True:
                            option = input('random, without chosed, with choosed (r/woc/wc): ')
                            if option == 'r':
                                password = passwordManager.create_random_password()
                                passwordManager.update_password(platform, password)
                                break
                            elif option == 'woc':
                                chosed_chars = input('Choose unexeptible chars: ')
                                password = passwordManager.password_without_chosed_chars(
                                    chosed_chars)
                                passwordManager.update_password(platform, password)
                                break
                            elif option == 'wc':
                                chosed_chars = input('Choose exeptible chars: ')
                                password = passwordManager.password_with_chosed_chars(chosed_chars)
                                passwordManager.update_password(platform, password)
                                break
                            elif option == 'exit':
                                break
                            else:
                                print("option dosen't exist")
                    elif option == 'exit':
                        break
                    else:
                        print('Option does not exist')
                elif platform == 'exit':
                    break
                else:
                    print('Platform does not exist')

        elif option == 'change_login':
            while True:
                exist_platforms = passwordManager.gel_all_platform_names_from_db()
                platform = input('Platform: ')
                if platform in exist_platforms:
                    login = input('Login: ')
                    passwordManager.update_login(platform, login)
                    break
                elif platform == 'exit':
                    break
                else:
                    print('Platform does not exist')

        elif option == 'add':
            while True:
                platform, login, password = input('Platform: '), input(
                    'Login: '), input('Password: ')
                print_block(platform, login, password)
                option = input('Is that correct?(y/n) ')
                if option == 'y':
                    passwordManager.insert_login_data_to_db(platform, login, password)
                    print('Your data was successfuly added')
                    break
                elif option == 'n':
                    continue
                else:
                    passwordManager.insert_login_data_to_db(platform, login, password)
                    print('Okey... lets think that you agreed')
                    break

        elif option == 'delete':
            exist_platforms = passwordManager.gel_all_platform_names_from_db()
            for item in exist_platforms:
                print(f'|{item}')
            platform = input('\nWhich platform would you like to delete: ')
            if platform in exist_platforms:
                passwordManager.delete_item_by_platform_name(platform)

            elif option == 'exit':
                pass
            else:
                print('There is no such platform')

        elif option == 'exit':
            break

        else:
            print('Incorrect option')
