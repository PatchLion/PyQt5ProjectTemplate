from PyQt5.QtGui import *
import os
fonts_path = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))
print("Fonts File Path==>", fonts_path)

def loadAllFonts():
    for root, dirs, files in os.walk(fonts_path):
        for file in files:
            infos = os.path.splitext(file)
            if infos[1].lower() == ".ttc":
                familyid = QFontDatabase.addApplicationFont(os.path.join(fonts_path, file))
                if -1 == familyid:
                    print("Failed to load font file:", file)
                else:
                    print("Font file {} loaded".format(file))