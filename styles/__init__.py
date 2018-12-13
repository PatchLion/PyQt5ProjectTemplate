import os
qss_path = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))
print("QSS File Path==>", qss_path)
def loadAllStyles(app):
    qss = ""
    for root, dirs, files in os.walk(qss_path):
        for file in files:
            infos = os.path.splitext(file)
            if infos[1].lower() == ".qss":
                try:
                    with open(os.path.join(qss_path, file), 'rt', encoding='utf-8') as f:
                        qss = qss + "\n" + f.read()
                        print("Load qss file:", file)
                except Exception as e:
                    print("Failed to load qss: ", e)

    app.setStyleSheet(qss)