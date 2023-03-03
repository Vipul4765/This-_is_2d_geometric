import mysql.connector
import sys


class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='demo-hir-db')
            self.mycursor = self.conn.cursor()
        except:
            print('Not connected to the database')
            sys.exit(0)
        else:
            print('connect to the database')

    def register(self, name, email, password):
        try:
            self.mycursor.execute(
                """INSERT INTO `student_data` (`id`, `Name`, `Email`, `password`) VALUES (NULL, '{}', '{}', '{}');
                """.format(name, email, password)
            )
            self.conn.commit()
        except:
            return -1
        else:
            return 1
