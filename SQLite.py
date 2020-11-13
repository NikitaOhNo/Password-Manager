import sqlite3 as sql


class SQLite:
    def __init__(self, database='data.db'):
        self.connect_to_database = sql.connect(database)
        self.cursor = self.connect_to_database.cursor()
        self.create_table_ifnot_exist()

    def create_table_ifnot_exist(self):
        with self.connect_to_database:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Passwords (
                                Platform text,
                                Login text,
                                Password text
                                )''')

    def insert_login_data_to_db(self, platform, login, password):
        with self.connect_to_database:
            self.cursor.execute('''INSERT INTO Passwords VALUES
                            (:Platform, :Login, :Password)''',
                                {'Platform': platform, 'Login': login, 'Password': password})
            self.connect_to_database.commit()

    def delete_item_by_platform_name(self, name):
        with self.connect_to_database:
            self.cursor.execute("""DELETE from Passwords WHERE
                                        Platform = :Platform""",
                                {'Platform': name})
            self.connect_to_database.commit()

    def update_login(self, platform_name, new_login):
        with self.connect_to_database:
            self.cursor.execute('''UPDATE Passwords
                    SET Login = :NewLogin WHERE Platform = :Platform''',
                                {'NewLogin': new_login, 'Platform': platform_name})
            self.connect_to_database.commit()

    def update_password(self, platform_name, new_password):
        with self.connect_to_database:
            self.cursor.execute('''UPDATE Passwords
                        SET Password = :Password WHERE Platform = :Platform''',
                                {'Password': new_password, 'Platform': platform_name})
            self.connect_to_database.commit()

    def get_everything_from_db(self):
        with self.connect_to_database:
            self.cursor.execute('SELECT * FROM Passwords')
            data = self.cursor.fetchall()
            return data

    def gel_all_platform_names_from_db(self):
        with self.connect_to_database:
            self.cursor.execute('''SELECT Platform FROM Passwords''')
            data = self.cursor.fetchall()
            platforms = [i[0] for i in data]
            return platforms

    def get_data_by_name(self, name_of_platform):
        with self.connect_to_database:
            self.cursor.execute('''SELECT * FROM Passwords WHERE Platform=:name''',
                                {'name': name_of_platform})
            login_data_for_platform = self.cursor.fetchone()
            return login_data_for_platform


if __name__ == '__main__':
    test = SQLite('data.db')
