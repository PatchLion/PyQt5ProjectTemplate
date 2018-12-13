'''
打包参考资料：https://www.cnblogs.com/dcb3688/p/4211390.html
'''
import os

app_path = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))
print("Package App Path==>", app_path)
#order = "pyinstaller.exe -F -w {}/app.py --upx-dir={}".format(app_path, os.path.join(app_path, "upx308w"))
order = "pyinstaller.exe -F -w {}/app.py ".format(app_path)
print("Package Order==>", order)
os.system(order)