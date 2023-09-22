import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class UyeTakipSistemi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Üye Takip Sistemi")
        self.setGeometry(100, 100, 400, 400)
        
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label_adsoyad = QLabel("Ad Soyad:")
        self.input_adsoyad = QLineEdit()
        self.layout.addWidget(self.label_adsoyad)
        self.layout.addWidget(self.input_adsoyad)

        self.label_status = QLabel("Statü:")
        self.input_status = QLineEdit()
        self.layout.addWidget(self.label_status)
        self.layout.addWidget(self.input_status)

        self.label_baslangic = QLabel("Başlangıç Tarihi:")
        self.input_baslangic = QLineEdit()
        self.layout.addWidget(self.label_baslangic)
        self.layout.addWidget(self.input_baslangic)

        self.label_bitis = QLabel("Bitiş Tarihi:")
        self.input_bitis = QLineEdit()
        self.layout.addWidget(self.label_bitis)
        self.layout.addWidget(self.input_bitis)

        self.label_ucret = QLabel("Ödediği Ücret ₺:")
        self.input_ucret = QLineEdit()
        self.layout.addWidget(self.label_ucret)
        self.layout.addWidget(self.input_ucret)

        self.kaydet_button = QPushButton("Kaydet")
        self.layout.addWidget(self.kaydet_button)
        self.kaydet_button.clicked.connect(self.kaydet)

        self.central_widget.setLayout(self.layout)

        # Veritabanı bağlantısı
        self.conn = sqlite3.connect("uye_takip.db")
        self.cursor = self.conn.cursor()

        # Veritabanı tablosunu oluştur
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS uyeler (
                id INTEGER PRIMARY KEY,
                adsoyad TEXT,
                status TEXT,
                baslangic DATE,
                bitis DATE,
                ucret REAL
            )
        ''')
        self.conn.commit()

    def kaydet(self):
        adsoyad = self.input_adsoyad.text()
        status = self.input_status.text()
        baslangic = self.input_baslangic.text()
        bitis = self.input_bitis.text()
        ucret = self.input_ucret.text()

        # Veritabanına kaydet
        self.cursor.execute('''
            INSERT INTO uyeler (adsoyad, status, baslangic, bitis, ucret)
            VALUES (?, ?, ?, ?, ?)
        ''', (adsoyad, status, baslangic, bitis, ucret))
        self.conn.commit()

        # Inputları temizle
        self.input_adsoyad.clear()
        self.input_status.clear()
        self.input_baslangic.clear()
        self.input_bitis.clear()
        self.input_ucret.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UyeTakipSistemi()
    window.show()
    sys.exit(app.exec_())
