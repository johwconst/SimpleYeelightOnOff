import sqlite3

class createDB:
    def __init__(self):
        self.con = sqlite3.connect('db.sqlite3')
        self.cur = self.con.cursor()
        self.createTable()

    def createTable(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS simpleDB (
            nome TEXT,
            ip TEXT,
            location TEXT)''')

    def addBulb(self, name, ip, location):
        try:
            self.cur.execute(
                '''INSERT INTO simpleDB VALUES (?, ?, ?)''', (name, ip, location,))
        except Exception as e:
            self.con.rollback()
        else:
            self.con.commit()

    def getLastBulb(self):
        return self.cur.execute('SELECT MAX(rowid) FROM simpleDB').fetchone()

    def getBulb(self):
        return self.cur.execute('SELECT rowid, * FROM simpleDB').fetchall()

    def deleteBulb(self, rowid):
        try:
            self.cur.execute("DELETE FROM simpleDB WHERE rowid=?", (rowid,))
        except Exception as e:
            self.con.rollback()
        else:
            self.con.commit()
