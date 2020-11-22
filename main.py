#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
from PyQt5 import QtWidgets #Thư viện GUI PyQt5
from components import Database as db #import components xử lý data
from containers import Main

# Entry point for application
if __name__ == '__main__':
    if not db.checkSetup(): 
        db.setup() #Nếu trạng thái chương trình chưa được khởi động thì bắt đầu các hàm khởi tạo ban đầu
    app = QtWidgets.QApplication(sys.argv) 
    parent = QtWidgets.QMainWindow()
    Main.MainWindow(parent)
    parent.show()
    sys.exit(app.exec_())