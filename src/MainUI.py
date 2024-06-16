# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctvd.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 510)
        MainWindow.setMinimumSize(QtCore.QSize(500, 510))
        MainWindow.setMaximumSize(QtCore.QSize(500, 610))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(240, -1, 2, 501))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(11, 239, 219, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 248, 78, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 11, 78, 16))
        self.label.setObjectName("label")
        self.tableWidget_Config = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Config.setGeometry(QtCore.QRect(11, 32, 219, 201))
        self.tableWidget_Config.setObjectName("tableWidget_Config")
        self.tableWidget_Config.setColumnCount(2)
        self.tableWidget_Config.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Config.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Config.setHorizontalHeaderItem(1, item)
        self.tableWidget_List = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_List.setGeometry(QtCore.QRect(11, 269, 219, 201))
        self.tableWidget_List.setObjectName("tableWidget_List")
        self.tableWidget_List.setColumnCount(1)
        self.tableWidget_List.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_List.setHorizontalHeaderItem(0, item)
        self.flash_program = QtWidgets.QPushButton(self.centralwidget)
        self.flash_program.setGeometry(QtCore.QRect(205, 6, 25, 25))
        self.flash_program.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/flash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flash_program.setIcon(icon)
        self.flash_program.setIconSize(QtCore.QSize(20, 20))
        self.flash_program.setObjectName("flash_program")
        self.flash_list = QtWidgets.QPushButton(self.centralwidget)
        self.flash_list.setGeometry(QtCore.QRect(205, 242, 25, 25))
        self.flash_list.setText("")
        self.flash_list.setIcon(icon)
        self.flash_list.setIconSize(QtCore.QSize(20, 20))
        self.flash_list.setObjectName("flash_list")
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(250, 10, 240, 141))
        self.label_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_img.setScaledContents(True)
        self.label_img.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img.setObjectName("label_img")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(250, 160, 240, 20))
        self.label_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_title.setObjectName("label_title")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(250, 190, 240, 170))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 238, 168))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_introduce = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_introduce.setGeometry(QtCore.QRect(5, 0, 235, 170))
        self.label_introduce.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_introduce.setObjectName("label_introduce")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 430, 240, 40))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 370, 240, 50))
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.actionfile = QtWidgets.QAction(MainWindow)
        self.actionfile.setObjectName("actionfile")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionout = QtWidgets.QAction(MainWindow)
        self.actionout.setObjectName("actionout")
        self.actionsetting = QtWidgets.QAction(MainWindow)
        self.actionsetting.setObjectName("actionsetting")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionfrom_file = QtWidgets.QAction(MainWindow)
        self.actionfrom_file.setObjectName("actionfrom_file")
        self.actionfrom_link = QtWidgets.QAction(MainWindow)
        self.actionfrom_link.setObjectName("actionfrom_link")
        self.menu.addAction(self.actionfile)
        self.menu.addAction(self.actionsetting)
        self.menu.addAction(self.actionabout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menu_3.addAction(self.actionfrom_file)
        self.menu_3.addAction(self.actionfrom_link)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.actionout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "视频列表"))
        self.label.setText(_translate("MainWindow", "节目信息"))
        item = self.tableWidget_Config.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget_Config.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_List.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "名称"))
        self.label_img.setText(_translate("MainWindow", "暂无图片qwq"))
        self.label_title.setText(_translate("MainWindow", "暂无标题"))
        self.label_introduce.setText(_translate("MainWindow", "<html><head/><body><p>暂无介绍</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>暂无时间</p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "程序"))
        self.menu_2.setTitle(_translate("MainWindow", "节目"))
        self.menu_3.setTitle(_translate("MainWindow", "导入节目单"))
        self.actionfile.setText(_translate("MainWindow", "打开文件保存位置"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
        self.actionout.setText(_translate("MainWindow", "导出节目单"))
        self.actionsetting.setText(_translate("MainWindow", "设置"))
        self.actionabout.setText(_translate("MainWindow", "关于..."))
        self.actionfrom_file.setText(_translate("MainWindow", "从文件导入"))
        self.actionfrom_link.setText(_translate("MainWindow", "从链接导入"))
import resources.resources
