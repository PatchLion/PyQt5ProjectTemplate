import os
ui_file_path = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))
print("UI Files:", ui_file_path)
def updateUIFile():
    for root, dirs, files in os.walk(ui_file_path):
        for file in files:
            infos = os.path.splitext(file)
            if infos[1].lower() == ".ui":
                order = "pyuic5.exe -o {}/ui_{}.py {}/{}".format(ui_file_path, infos[0], ui_file_path, file)
                print(order)
                os.system(order)