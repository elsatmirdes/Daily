from forms.decoderform import DECODER
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import pyAesCrypt
import sys
import sqlite3 as sql

class app(QtWidgets.QMainWindow):
    def __init__(self):
        super(app, self).__init__()
        self.ui = DECODER()
        self.ui.setupUi(self)

        location_file = str(os.getcwd())
        self.replace = location_file.replace("\\", "/")

        self.ui.pushButton.clicked.connect(self.dailypasswordcracked)
    def dailypasswordcracked(self):
        password = self.ui.password.text()
        buffersize = 512 * 1024
        username = self.ui.username.text()
        year = self.ui.year.text()
        month = self.ui.month.text()
        day = self.ui.day.text()
        # file_location = f"dailytext/{username}/{year}/{month}/{day}txt.aes"
        try:
            self.conn = sql.connect("data/users.sqlite")
            self.cur = self.conn.cursor()

            self.cur.execute("SELECT * FROM users WHERE username = '{}'".format(username))

            self.data = self.cur.fetchone()

            if self.data[1] != password:
                QMessageBox.critical(self,"PAROLA YANLIŞ","LÜTFEN DOSYA ŞİFRENİZİ DOĞRU GİRİNİZ")
            else:
                file_location = f"{self.replace}/dailytext/{username}/{year}/{month}/{day}.txt.aes"
                pyAesCrypt.decryptFile(str(file_location), str(file_location) + ".txt", password, buffersize)
                QMessageBox.information(self,"BAŞARILI","SEÇTİĞİNİZ GÜNLÜK DOSYASI AÇILDI")

        except Exception:
            QMessageBox.warning(self,"YANLIŞ DOSYA DİZİNİ", "LÜTFEN VAR OLAN BİR DOSYA DİZİNİ OLUŞTURUN")

def run():
    ap = QtWidgets.QApplication(sys.argv)
    win = app()
    win.show()
    sys.exit(ap.exec_())


if __name__ == "__main__":
    run()