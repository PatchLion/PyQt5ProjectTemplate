from PyQt5.QtWidgets import *
from uis.ui_login import Ui_LoginWidget


class MyWidget(QWidget):
    def __init__(self, *args):
        super(MyWidget, self).__init__(*args)
        self.resize(300,300)
        self._ui = Ui_LoginWidget()
        self._ui.setupUi(self)
        self._ui.pushButtonLogin.setProperty("class", "Blue")
        self._ui.pushButtonLogin.clicked.connect(self.slotLogin)
        self._ui.pushButtonCancel.setProperty("class", "Red")

    def slotLogin(self):
        print("LOGIN")
