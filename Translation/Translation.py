import sys
from PyQt5 import QtWidgets
from textblob import TextBlob
from Ui_Kılavuz import Ui_Kilavuz
from Ui_Turkce import Ui_Turkce
from Ui_Ingilizce import Ui_Ingilizce
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QListWidget, QInputDialog, QRadioButton,  QGridLayout, QCompleter


class Windows(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Kilavuz()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.turkce)
        self.ui.pushButton_2.clicked.connect(self.ingilizce)
        
        
        

    def turkce(self):
      
       self.t = Windows2()
       self.t.show()
    
    def ingilizce(self):
      
       self.t=Windows3()
       self.t.show()
      

class Windows2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Turkce()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Tamam)


        layout = QGridLayout()
        self.setLayout(layout)
                                               
        names = ["Ampul", "ampul", "Akıl", "akıl", "Bardak", "bardak", "Bez", "bez" "Cilt", "cilt", "Cam", "cam" "Derin", "derin", "Dolap", "dolap", "Merhaba", "merhaba", "Okul", "okul" ]
        completer = QCompleter(names)
                              
        self.ui.lineEdit.setCompleter(completer)
        layout.addWidget(self.ui.lineEdit, 3, 7)

       
    
    def Tamam(self):

        tr = self.ui.lineEdit.text()
        text = TextBlob(tr)
        en = text.translate(to="en")
        en = str(en)
        
        self.ui.listWidget.addItem("" + self.ui.lineEdit.text())
        self.ui.listWidget_2.addItem(en)
        self.ui.listWidget_3.addItem(en)
 

class Windows3(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Ingilizce()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Tamam)
        

        
        layout = QGridLayout()
        self.setLayout(layout)
                                               
        names = ["Apple", "apple","Air", "air", "Berry", "berry","Black", "black", "Center", "center", "Cool", "cool", "Dark", "dark", "Edit", "edit", "Hello", "hello", "School", "school", ]
        completer = QCompleter(names)
                              
        self.ui.lineEdit.setCompleter(completer)
        layout.addWidget(self.ui.lineEdit, 3, 7)


    def Tamam(self):

    
        en = self.ui.lineEdit.text()
        text = TextBlob(en)
        tr = text.translate(to="tr")
        tr = str(tr)

        self.ui.listWidget.addItem("" + self.ui.lineEdit.text())
        self.ui.listWidget_2.addItem(tr)
        self.ui.listWidget_3.addItem(tr)

        
app = QApplication(sys.argv)
win = Windows()
win.show()
sys.exit(app.exec_())