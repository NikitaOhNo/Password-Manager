import random
import string
import json
from SQLite import SQLite


class PasswordManager(SQLite):
    def __init__(self):
        SQLite.__init__(self)

    def create_random_password(self, leight=16):
        password = ''
        for i in range(leight):
            x = random.randint(0, 94)
            password += string.printable[x]
        return password

    def password_without_chosed_chars(self, not_allowed, leight=16):
        password = ''
        new_print_table = ''
        for i in string.printable[:94]:
            if i not in not_allowed:
                new_print_table += i
        for i in range(leight):
            x = random.randint(0, len(new_print_table))
            password += new_print_table[x]
        return password

    def password_with_chosed_chars(self, allowed_chars, leight=16):
        new_printtable = string.printable[0:-38] + allowed_chars
        password = ''
        for i in range(leight):
            x = random.randint(0, len(new_printtable))
            password += new_printtable[x]
        return password


if __name__ == '__main__':
    test = PasswordManager()
    # print(string.printable[:94])
    # print(test.password_without_not_allowed_chars('*-+()~":'))
    # print(test.password_with_only_allowed_chars('-+^&*()_'))
    # print(test.show_all())
