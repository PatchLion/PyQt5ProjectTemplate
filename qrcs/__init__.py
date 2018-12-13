#pyrcc5.exe

import os
qrc_file_path = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))
print("QRC Files:", qrc_file_path)
def updateQRCFile():
    for root, dirs, files in os.walk(qrc_file_path):
        for file in files:
            infos = os.path.splitext(file)
            if infos[1].lower() == ".qrc":
                order = "pyrcc5.exe -o {}/{}_rc.py {}/{}".format(qrc_file_path, infos[0], qrc_file_path, file)
                print(order)
                os.system(order)