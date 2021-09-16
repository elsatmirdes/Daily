from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMessageBox
from forms.login import Ui_MainWindow
from forms.dailyform import Ui_MainWindowDaily
from forms.registerform import Register
from forms.decoderform import DECODER
from datetime import datetime
import sqlite3 as sql
import sys
import os

import pyAesCrypt
from getpass import getpass

class Daily(QtWidgets.QMainWindow):
    def __init__(self):
        super(Daily, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        if os.path.isdir("dailytext"):
            pass

        else:
            os.mkdir("dailytext")

        if os.path.isdir("data"):
            pass
        else:
            os.mkdir("data")

        self.conn = sql.connect("data/users.sqlite")
        self.cur = self.conn.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS users (username, password)")

        self.ui.pushButton.clicked.connect(self.sign)
        self.ui.pushButton_2.clicked.connect(self.winowreg)

    def sign(self):
        self.username = self.ui.username.text()
        self.password = self.ui.password.text()

        self.cur.execute("""SELECT * FROM users WHERE
        username = ? AND password = ?""", (self.username, self.password))

        self.data = self.cur.fetchone()

        if self.data:
            self.close()
            self.window()
            QMessageBox.information(self,"WELCOM",f"HOŞ GELDİN {self.username.upper()}")
            self.ui2.add.clicked.connect(self.regdaily)

        else:
            print("Tekrar Dene")
            QMessageBox.critical(self,"HATA","Eksik veya hatalı giriş.")

    def register(self):
        username = self.ui3.username.text()
        password = self.ui3.password.text()
        verifypass = self.ui3.verifypass.text()
        email = self.ui3.mail.text()


        if self.controlusernumber() >= 5:
            QMessageBox.warning(self,"KOTA SINIRI","SİSTEME SADECE BİR BİLGİSAYARDAN 1 KAYIT YAPILABİLİR")
            self.reg.close()

        if self.controlusernumber() < 5:
            self.cur.execute("SELECT * FROM users WHERE username = '{}'".format(username))
            data = self.cur.fetchone()

            if data:
                QMessageBox.critical(self,"MEVCUT","BU KULLANICI ADI ZATEN KULLANILIYOR")
                self.reg.close()

            else:
                if username == "":
                    QMessageBox.critical(self,"HATA","TÜM ALANLARI DOLDURUN")
                    self.reg.close()
                elif email == "":
                    QMessageBox.critical(self,"HATA","TÜM ALANLARI DOLDURUN")
                    self.reg.close()
                else:
                    if len(password) <= 5:
                        QMessageBox.warning(self,"UYARI","PAROLA 5 KARAKTERDEN BÜYÜK OLMALIDIR")
                        self.reg.close()
                    if len(password) > 5:
                        if password != verifypass:
                            QMessageBox.critical(self, "HATA", "PAROLALAR EŞLEŞMİYOR!")
                            self.reg.close()
                        elif password == verifypass:
                            self.cur.execute("INSERT INTO users VALUES ('{}','{}')".format(username, password))
                            self.conn.commit()
                            QMessageBox.information(self, "BAŞARILI", "KAYIT EKLENDİ")
                            self.reg.close()


    def window(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindowDaily()
        self.ui2.setupUi(self.window2)

        self.window2.show()


    def winowreg(self):

        self.reg = QtWidgets.QMainWindow()
        self.ui3 = Register()
        self.ui3.setupUi(self.reg)
        self.reg.show()
        self.ui3.pushButton.clicked.connect(self.register)

    def regdaily(self):
        text = self.ui2.text.toPlainText()
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y")

        year = now.year
        month = now.month
        day = now.day

        if os.path.isdir(f"dailytext/{self.username}"):
            if os.path.isdir(f"dailytext/{self.username}/{year}/"):
                if os.path.isdir(f"dailytext/{self.username}/{year}/{month}"):
                    pass
                else:
                    os.mkdir(f"dailytext/{self.username}/{year}/{month}")
            else:
                os.mkdir(f"dailytext/{self.username}/{year}/")
        else:
            os.mkdir(f"dailytext/{self.username}")

        with open(f"dailytext/{self.username}/{year}/{month}/{day}.txt", "w",encoding="utf-8") as file:
            file.write(text)
            QMessageBox.information(self,"BAŞARILI","GÜNLÜK BAŞARIYLA ŞİFRELENEREK KAYIT EDİLDİ\n")


        file_location = f"dailytext/{self.username}/{year}/{month}/{day}.txt"
        # günlüğü krypto teknoloji ile şifreleme
        dailypassword = self.password
        buffersize = 512 * 1024
        pyAesCrypt.encryptFile(str(file_location),str(file_location)+".aes", dailypassword,buffersize)

        os.remove(file_location)



    def controlusernumber(self):
        self.cur.execute("""SELECT * FROM users""")
        data = self.cur.fetchall()
        say = 0
        for i in data:
            say += 1
        return say


def run():
    ap = QtWidgets.QApplication(sys.argv)
    win = Daily()
    win.show()
    sys.exit(ap.exec_())


if __name__ == "__main__":
    run()
