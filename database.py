import sqlite3

class createDB:
    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()
        self.createTable()

    def createTable(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS simpleDB (
                nome TEXT,
                ip TEXT,
                location TEXT)''')
        except Exception as e:
            print('FAIL!' % e)
        else:
            print('DONE !')

    def addLamp(self, name, ip, location):
        try:
            self.cur.execute(
                '''INSERT INTO simpleDB VALUES (?, ?, ?)''', (name, ip, location,))
        except Exception as e:
            self.con.rollback()
        else:
            self.con.commit()

    def getLastLamp(self):
        return self.cur.execute('SELECT MAX(rowid) FROM simpleDB').fetchone()

    def getLamp(self):
        return self.cur.execute('SELECT rowid, * FROM simpleDB').fetchall()

    def deleteLamp(self, rowid):
        try:
            self.cur.execute("DELETE FROM simpleDB WHERE rowid=?", (rowid,))
        except Exception as e:
            self.con.rollback()
        else:
            self.con.commit()
