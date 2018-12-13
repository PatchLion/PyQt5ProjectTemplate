import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from styles import loadAllStyles
from fonts import loadAllFonts
#from qrcs import images_rc
from app import MyWidget

if "__main__" == __name__:
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon(":/image/green_n.png"))
    loadAllStyles(app)
    loadAllFonts()
    w = MyWidget()
    w.show()
    sys.exit(app.exec())