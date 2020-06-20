import sqlite3


class SQLighter:

    def __init__(self, database_file):
        """Подключить базу данных"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def add_people(self, first_name, second_name, password, mail, subject, learning_moment, city, login):
        """Добавить человека в базу данных"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `data` (`first_name`, `second_name`,`password`,`mail`,`subject`,`learning_moment`,`city`,`login`) VALUES(?,?,?,?,?,?,?,?)",
                                       (first_name, second_name, password, mail, subject, learning_moment, city, login))

    def reg_mail_unic(self, mail):
        """Проверяем уникальность mail"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `data` WHERE `mail` = ?', (mail,)).fetchall()
            return bool(len(result))

    def log_in_people(self, mail, password):
        """Проверяем правильность логина и пароля"""
        with self.connection:
            result_log_in = self.cursor.execute('SELECT * FROM `data` WHERE `mail` = ? AND `password` = ?', (mail, password)).fetchall()
            return bool(len(result_log_in))

    def close(self):
        self.connection.close()

#  Copyright (c) 2020.  Designed TheFox
