import sqlite3


class SQLighter:
    def __init__(self, database_file):
        """Подключение к БД и сохранение курсора соединения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()



#Есть ли пользователь в таблице
    def user_exist(self, id_user):
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `referal` WHERE `id_user` = ?',
                                         (id_user,)).fetchall()
            return bool(len(result))
#Добавление пользователя
    def add_user(self, id_user, id_ref=None, first_name='NoName'):
        with self.connection:
            if id_ref != None:
                return self.cursor.execute('INSERT INTO `referal` (`id_user`, `id_ref`, `first_name`) VALUES (?,?,?)',
                                           (id_user, id_ref, first_name,))
            else:
                return self.cursor.execute('INSERT INTO `referal` (`id_user`, `first_name`) VALUES (?,?)',
                                           (id_user, first_name,))

#получить количество рефералов
    def count_user(self, id_user):
        with self.connection:
            return self.cursor.execute('SELECT COUNT(`id`) as count FROM `referal` WHERE `id_ref` = ?', (id_user,)).fetchone()[0]

#Получить список рефералов и\или пользоватей
    def get_all_refusers(self, who):
        with self.connection:
            if who == 'users':
                return self.cursor.execute('SELECT `id_user` FROM `referal` WHERE `id_ref` != ?', ('None',)).fetchall()
            elif who == 'referrars':
                return self.cursor.execute('SELECT `id_ref` FROM `referal` WHERE `id_ref` != ?', ('None',)).fetchall()
            else: return self.cursor.execute('SELECT `id_user`,`id_ref` FROM `referal` WHERE `id_ref` != ?', ('None',)).fetchall()

#получить имя пользователя чей реферал
    def get_firstname(self, id_ref):
        with self.connection:
            return self.cursor.execute('SELECT `first_name` FROM `referal` WHERE `id_user` = ?',
                                        (id_ref,)).fetchone()

    ##############################
###########УДАЛИТЬ############
##############################

#Удалить реферала пользователя
    def delete_user_ref(self, id_user, id_ref):
        with self.connection:
            return self.cursor.execute("DELETE FROM `referal` WHERE `id_user` = ? AND `id_ref` = ?", (id_user, id_ref,))


    def close(self):
        """Закрытие соединения"""
        self.connection.close()