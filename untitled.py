# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import configparser
import os
import time
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1051, 763)
        Form.setStyleSheet("background-color:black;")
        self.songs_list = []
        self.song_formats = ['mp3', 'm4a', 'flac', 'wav', 'ogg']
        self.settingfilename = 'setting.ini'
        self.player = QMediaPlayer()
        self.cur_path = os.path.abspath(os.path.dirname(__file__))
        self.cur_playing_song = ''
        self.is_switching = False
        self.is_pause = True

        self.stackedWidget_2 = QtWidgets.QStackedWidget(Form)
        self.stackedWidget_2.setGeometry(QtCore.QRect(210, 50, 831, 601))
        self.stackedWidget_2.setStyleSheet("background-color:white;")
        self.stackedWidget_2.setObjectName("stackedWidget_2")

        #右侧第一个页面
        self.zhu_1 = QtWidgets.QWidget()
        self.zhu_1.setObjectName("zhu_1")
        self.toolButton_1 = QtWidgets.QToolButton(self.zhu_1)
        self.toolButton_1.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_1.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_1.setText("")
        self.toolButton_1.setObjectName("toolButton_1")
        self.label_1 = QtWidgets.QLabel(self.zhu_1)
        self.label_1.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_1.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_1.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_1.setObjectName("label_1")
        self.listView = QtWidgets.QListView(self.zhu_1)
        self.listView.setGeometry(QtCore.QRect(20, 150, 791, 441))
        self.listView.setObjectName("listView")
        self.stackedWidget_2.addWidget(self.zhu_1)

        # 右侧第二个页面
        self.zhu_2 = QtWidgets.QWidget()
        self.zhu_2.setObjectName("zhu_2")
        self.label_2 = QtWidgets.QLabel(self.zhu_2)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_2.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.zhu_2)
        self.toolButton_4.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_4.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.stackedWidget_2.addWidget(self.zhu_2)

        # 右侧第三个页面
        self.zhu_3 = QtWidgets.QWidget()
        self.zhu_3.setObjectName("zhu_3")
        self.label_3 = QtWidgets.QLabel(self.zhu_3)
        self.label_3.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_3.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.toolButton_3 = QtWidgets.QToolButton(self.zhu_3)
        self.toolButton_3.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_3.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_3.setText("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.stackedWidget_2.addWidget(self.zhu_3)

        # 右侧第4个页面
        self.zhu_4 = QtWidgets.QWidget()
        self.zhu_4.setObjectName("zhu_4")
        self.label_4 = QtWidgets.QLabel(self.zhu_4)
        self.label_4.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_4.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.toolButton_4 = QtWidgets.QToolButton(self.zhu_4)
        self.toolButton_4.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_4.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_4.setText("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.stackedWidget_2.addWidget(self.zhu_4)

        # 右侧第5个页面
        self.zhu_5 = QtWidgets.QWidget()
        self.zhu_5.setObjectName("zhu_5")
        self.label_5 = QtWidgets.QLabel(self.zhu_5)
        self.label_5.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_5.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.toolButton_5 = QtWidgets.QToolButton(self.zhu_5)
        self.toolButton_5.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_5.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_5.setText("")
        self.toolButton_5.setObjectName("toolButton_5")
        self.stackedWidget_2.addWidget(self.zhu_5)

        # 右侧第6个页面
        self.zhu_6 = QtWidgets.QWidget()
        self.zhu_6.setObjectName("zhu_6")
        self.label_6 = QtWidgets.QLabel(self.zhu_6)
        self.label_6.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_6.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.toolButton_6 = QtWidgets.QToolButton(self.zhu_6)
        self.toolButton_6.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_6.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_6.setText("")
        self.toolButton_6.setObjectName("toolButton_6")
        self.stackedWidget_2.addWidget(self.zhu_6)

        # 右侧第7个页面
        self.zhu_7 = QtWidgets.QWidget()
        self.zhu_7.setObjectName("zhu_7")
        self.label_7 = QtWidgets.QLabel(self.zhu_7)
        self.label_7.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_7.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_7.setObjectName("label_7")
        self.toolButton_7 = QtWidgets.QToolButton(self.zhu_7)
        self.toolButton_7.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_7.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_7.setText("")
        self.toolButton_7.setObjectName("toolButton_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.zhu_7)
        self.pushButton_7.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.openDir)

        self.listView_7 = QtWidgets.QListWidget(self.zhu_7)
        self.listView_7.setGeometry(QtCore.QRect(20, 150, 791, 441))
        self.listView_7.setObjectName("listView_7")
        self.listView_7.itemDoubleClicked.connect(self.doubleClicked)

        self.stackedWidget_2.addWidget(self.zhu_7)

        # 右侧第8个页面
        self.zhu_8 = QtWidgets.QWidget()
        self.zhu_8.setObjectName("zhu_8")
        self.label_8 = QtWidgets.QLabel(self.zhu_8)
        self.label_8.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_8.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_8.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_8.setObjectName("label_8")
        self.toolButton_8 = QtWidgets.QToolButton(self.zhu_8)
        self.toolButton_8.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_8.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_8.setText("")
        self.toolButton_8.setObjectName("toolButton_8")
        self.stackedWidget_2.addWidget(self.zhu_8)

        # 右侧第9个页面
        self.zhu_9 = QtWidgets.QWidget()
        self.zhu_9.setObjectName("zhu_9")
        self.label_9 = QtWidgets.QLabel(self.zhu_9)
        self.label_9.setGeometry(QtCore.QRect(180, 20, 181, 41))
        self.label_9.setStyleSheet("font-weight:500;\nfont-size: 30px;")
        self.label_9.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_9.setObjectName("label_9")
        self.toolButton_9 = QtWidgets.QToolButton(self.zhu_9)
        self.toolButton_9.setGeometry(QtCore.QRect(20, 20, 121, 121))
        self.toolButton_9.setStyleSheet("image: url(./image/everyday.jpg);\n")
        self.toolButton_9.setText("")
        self.toolButton_9.setObjectName("toolButton_9")
        self.stackedWidget_2.addWidget(self.zhu_9)

        # 右侧第10个页面
        self.zhu_10 = QtWidgets.QWidget()
        self.zhu_10.setObjectName("zhu_10")
        self.label_10 = QtWidgets.QLabel(self.zhu_10)
        self.label_10.setGeometry(QtCore.QRect(150, 90, 54, 12))
        self.label_10.setObjectName("label_10")
        self.stackedWidget_2.addWidget(self.zhu_10)

        # 右侧第11个页面
        self.zhu_11 = QtWidgets.QWidget()
        self.zhu_11.setObjectName("zhu_11")
        self.label_11 = QtWidgets.QLabel(self.zhu_11)
        self.label_11.setGeometry(QtCore.QRect(110, 140, 171, 16))
        self.label_11.setObjectName("label_11")
        self.stackedWidget_2.addWidget(self.zhu_11)

        #左侧模块
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(29, 10, 181, 701))
        self.frame.setStyleSheet("background:gray;\n"
                                "border-top:1px solid white;\n"
                                "border-bottom:1px solid white;\n"
                                "border-left:1px solid white;\n"
                                "border-top-left-radius:10px;\n"
                                "border-bottom-left-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 181, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #最小化按钮
        self.pushButton_lo_ = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_lo_.setStyleSheet("background:#6DDF6D;\nborder-radius:5px;")
        self.pushButton_lo_.setObjectName("pushButton_lo_")
        self.horizontalLayout.addWidget(self.pushButton_lo_)
        #最大化按钮
        self.pushButton_loo = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_loo.setStyleSheet("background:#F7D674;\nborder-radius:5px;")
        self.pushButton_loo.setObjectName("pushButton_loo")
        self.horizontalLayout.addWidget(self.pushButton_loo)
        #关闭按钮
        self.pushButton_lox = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_lox.setStyleSheet("background:#F76677;\nborder-radius:5px;")
        self.pushButton_lox.setObjectName("pushButton_lox")
        self.horizontalLayout.addWidget(self.pushButton_lox)
        #创建左侧导航（按钮）
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 181, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")





        #顶部搜索模块
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(210, 10, 831, 41))
        self.frame_2.setStyleSheet("background-color:white;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        #搜索框
        self.lineEdit_sousukuang = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_sousukuang.setGeometry(QtCore.QRect(190, 10, 591, 20))
        self.lineEdit_sousukuang.setStyleSheet("border:1px solid gray;\n"
                                                "width:300px;\n"
                                                "border-radius:10px;\n"
                                                "padding:2px 4px;")
        self.lineEdit_sousukuang.setObjectName("lineEdit_sousukuang")
        #搜索lable
        self.label_sousu = QtWidgets.QLabel(self.frame_2)
        self.label_sousu.setGeometry(QtCore.QRect(110, 10, 61, 21))
        self.label_sousu.setScaledContents(False)
        self.label_sousu.setWordWrap(False)
        self.label_sousu.setOpenExternalLinks(False)
        self.label_sousu.setObjectName("label_sousu")

        #底部播放模块

        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(210, 650, 831, 61))
        self.frame_3.setStyleSheet("background-color:white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        #播放按钮
        self.pushButton_bofang = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_bofang.setGeometry(QtCore.QRect(390, 20, 41, 31))
        self.pushButton_bofang.setObjectName("pushButton_bofang")
        self.pushButton_bofang.clicked.connect(self.playMusic)

        #下一首按钮
        self.pushButton_xiayishou = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_xiayishou.setGeometry(QtCore.QRect(440, 30, 41, 23))
        self.pushButton_xiayishou.setObjectName("pushButton_xiayishou")
        self.pushButton_xiayishou.clicked.connect(self.nextMusic)
        #上一首按钮
        self.pushButton_shangyishou = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_shangyishou.setGeometry(QtCore.QRect(340, 30, 41, 23))
        self.pushButton_shangyishou.setObjectName("pushButton_shangyishou")
        self.pushButton_shangyishou.clicked.connect(self.previewMusic)
        #进度条
        self.slider = QtWidgets.QSlider(self.frame_3)
        self.slider.setGeometry(QtCore.QRect(60, 10, 710, 5))
        # self.slider.sliderMoved[int].connect(lambda: self.player.setPosition(self.slider.value()))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setStyle(QStyleFactory.create('Fusion'))
        self.slider.setObjectName("slider")
        #播放时间
        self.label_qian = QtWidgets.QLabel(self.frame_3)
        self.label_qian.setGeometry(QtCore.QRect(20,6, 30, 12))
        self.label_qian.setObjectName("label_qian")
        self.label_hou = QtWidgets.QLabel(self.frame_3)
        self.label_hou.setGeometry(QtCore.QRect(785,6, 30, 12))
        self.label_hou.setObjectName("label_hou")
        # --计时器
        self.timer = QtCore.QTimer(Form)
        self.timer.start(1000)
        self.timer.timeout.connect(self.playByMode)


        #右侧导航按钮
        self.but_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_1.setStyleSheet("border:none;\nborder-left:4px solid red;font-weight:700;")
        self.but_1.setObjectName("but_1")
        self.verticalLayout.addWidget(self.but_1)
        self.but_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_2.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_2.setObjectName("but_2")
        self.verticalLayout.addWidget(self.but_2)
        self.but_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_3.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_3.setObjectName("but_3")
        self.verticalLayout.addWidget(self.but_3)
        self.but_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_4.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_4.setObjectName("but_4")
        self.verticalLayout.addWidget(self.but_4)
        self.but_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_5.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_5.setObjectName("but_5")
        self.verticalLayout.addWidget(self.but_5)
        self.but_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_6.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_6.setObjectName("but_6")
        self.verticalLayout.addWidget(self.but_6)
        self.but_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_7.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_7.setObjectName("but_7")
        self.verticalLayout.addWidget(self.but_7)
        self.but_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_8.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_8.setObjectName("but_8")
        self.verticalLayout.addWidget(self.but_8)
        self.but_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_9.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_9.setObjectName("but_9")
        self.verticalLayout.addWidget(self.but_9)
        self.but_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_10.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_10.setObjectName("but_10")
        self.verticalLayout.addWidget(self.but_10)
        self.but_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.but_11.setStyleSheet("border:none;border-left:4px solid red;font-weight:700;")
        self.but_11.setObjectName("but_11")
        self.verticalLayout.addWidget(self.but_11)

        self.retranslateUi(Form)
        self.stackedWidget_2.setCurrentIndex(6) #打开默认页面
        self.but_1.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(0))
        self.but_2.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(1))
        self.but_3.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(2))
        self.but_4.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(3))
        self.but_5.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(4))
        self.but_6.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(5))
        self.but_7.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(6))
        self.but_8.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(7))
        self.but_9.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(8))
        self.but_10.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(9))
        self.but_11.clicked.connect(lambda:self.stackedWidget_2.setCurrentIndex(10))
        self.pushButton_lox.clicked.connect(Form.close)
        self.loadSetting()
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "每日推荐"))
        self.label_2.setText(_translate("Form", "华语流行"))
        self.label_3.setText(_translate("Form", "热门MV"))
        self.label_4.setText(_translate("Form", "华语推荐"))
        self.label_5.setText(_translate("Form", "在线FM"))
        self.label_6.setText(_translate("Form", "我的音乐"))
        self.label_7.setText(_translate("Form", "本地音乐"))
        self.label_8.setText(_translate("Form", "下载管理"))
        self.label_9.setText(_translate("Form", "我的收藏"))
        self.label_10.setText(_translate("Form", "反馈建议"))
        self.label_11.setText(_translate("Form", "联系与帮助"))
        self.label_qian.setText(_translate("Form", "00:00"))
        self.label_hou.setText(_translate("Form", "00:00"))
        self.pushButton_lo_.setText(_translate("Form", "___"))
        self.pushButton_loo.setText(_translate("Form", "口"))
        self.pushButton_lox.setText(_translate("Form", "X"))
        self.but_1.setText(_translate("Form", "😍 每日推荐"))
        self.but_2.setText(_translate("Form", "💿 华语流行"))
        self.but_3.setText(_translate("Form", "🎥 热门 MV"))
        self.but_4.setText(_translate("Form", "📼 华语流行"))
        self.but_5.setText(_translate("Form", "📺 在线FM"))
        self.but_6.setText(_translate("Form", "📕 我的音乐"))
        self.but_7.setText(_translate("Form", "📘 本地音乐"))
        self.but_8.setText(_translate("Form", "📚 下载管理"))
        self.but_9.setText(_translate("Form", "💖 我的收藏"))
        self.but_10.setText(_translate("Form", "😜 反馈建议"))
        self.but_11.setText(_translate("Form", "📜 联系与帮助"))
        self.lineEdit_sousukuang.setText(_translate("Form", "输入歌手、歌曲或用户，回车进行搜索"))
        self.label_sousu.setText(_translate("Form", "🍳 搜索"))
        self.pushButton_bofang.setText(_translate("Form", "播放"))
        self.pushButton_xiayishou.setText(_translate("Form", "下一首"))
        self.pushButton_shangyishou.setText(_translate("Form", "上一首"))
        self.pushButton_7.setText(_translate("Form", "选择本地文件"))



    def playByMode(self):
        if (not self.is_pause) and (not self.is_switching):
            self.slider.setMinimum(0)
            self.slider.setMaximum(self.player.duration())
            self.slider.setValue(self.slider.value() + 1000)
        self.label_qian.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))
        self.label_hou.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))
        # 顺序播放
        if self.player.position() == self.player.duration():
            self.nextMusic()
        # if (self.cmb.currentIndex() == 0) and (not self.is_pause) and (not self.is_switching):
        #     if self.qlist.count() == 0:
        #         return
        #     if self.player.position() == self.player.duration():
        #         self.nextMusic()
        # # 单曲循环
        # elif (self.cmb.currentIndex() == 1) and (not self.is_pause) and (not self.is_switching):
        #     if self.qlist.count() == 0:
        #         return
        #     if self.player.position() == self.player.duration():
        #         self.is_switching = True
        #         self.setCurPlaying()
        #         self.slider.setValue(0)
        #         self.playMusic()
        #         self.is_switching = False
        # # 随机播放
        # elif (self.cmb.currentIndex() == 2) and (not self.is_pause) and (not self.is_switching):
        #     if self.qlist.count() == 0:
        #         return
        #     if self.player.position() == self.player.duration():
        #         self.is_switching = True
        #         self.qlist.setCurrentRow(random.randint(0, self.qlist.count() - 1))
        #         self.setCurPlaying()
        #         self.slider.setValue(0)
        #         self.playMusic()
        #         self.is_switching = False

    '''打开文件夹'''

    def openDir(self):
        self.cur_path = QFileDialog.getExistingDirectory(None, "选取文件夹", self.cur_path)
        if self.cur_path:
            self.showMusicList()                #调用函数
            self.cur_playing_song = ''
            self.setCurPlaying()                #默认播放音乐
            self.label_qian.setText('00:00')    #时间置空
            self.label_hou.setText('00:00')     #时间置空
            self.slider.setSliderPosition(0)    #进度条置空
            self.is_pause = True
            self.pushButton_bofang.setText('播放')    #

    '''导入setting'''

    def loadSetting(self):
        if os.path.isfile(self.settingfilename):   #如果配置文件存在
            config = configparser.ConfigParser()   #初始化实例
            config.read(self.settingfilename)      #读取配置文件
            self.cur_path = config.get('MusicPlayer', 'PATH')   #读取路径
            self.showMusicList()  #调用函数显示
    #
    '''更新setting'''

    def updateSetting(self):
        config = configparser.ConfigParser()            #初始化实例
        config.read(self.settingfilename)               #读取配置文件
        if not os.path.isfile(self.settingfilename):    #如果文件不存在
            config.add_section('MusicPlayer')           #创建配置文件属性
        config.set('MusicPlayer', 'PATH', self.cur_path)    #添加配置
        config.write(open(self.settingfilename, 'w'))   #创建文件并写入

    '''显示文件夹中所有音乐'''

    def showMusicList(self):
        # self.listView_7.clear()
        self.updateSetting()    #调用函数更新配置文件
        for song in os.listdir(self.cur_path):  #循环文件夹下文件
            if song.split('.')[-1] in self.song_formats:   #查找符合文件类型 ['mp3', 'm4a', 'flac', 'wav', 'ogg']
                self.songs_list.append([song, os.path.join(self.cur_path, song).replace('\\', '/')])   #添加到歌曲列表
                self.listView_7.addItem(song)   #添加到listciew里
        self.listView_7.setCurrentRow(0)        #默认选中第一个
        if self.songs_list:     #如果列表有歌曲
            self.cur_playing_song = self.songs_list[self.listView_7.currentRow()][-1]  #正在播放列表倒数第一个，后添加的在前，倒数第一个实际为文件列表第一个

    '''双击播放音乐'''

    def doubleClicked(self):
        self.slider.setValue(0)    #置空进度掉
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

    '''设置当前播放的音乐'''

    def setCurPlaying(self):
        print(self.songs_list[self.listView_7.currentRow()][-1])
        self.cur_playing_song = self.songs_list[self.listView_7.currentRow()][-1]
        self.player.setMedia(QMediaContent(QUrl(self.cur_playing_song)))

    '''提示'''

    def Tips(self, message):
        QtWidgets.QMessageBox.about(QtWidgets.QWidget, "提示", message)

    '''播放音乐'''
    #
    def playMusic(self):
        if self.listView_7.count() == 0:            #列表数量0，没有可播放文件
            self.Tips('当前路径内无可播放的音乐文件')
            return
        if not self.player.isAudioAvailable():      #如果没有正在播放
            self.setCurPlaying()
        if self.is_pause or self.is_switching:
            self.player.play()
            self.is_pause = False
            self.pushButton_bofang.setText('暂停')
        elif (not self.is_pause) and (not self.is_switching):
            self.player.pause()
            self.is_pause = True
            self.pushButton_bofang.setText('播放')

    '''上一首'''

    def previewMusic(self):
        self.slider.setValue(0)
        if self.listView_7.count() == 0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        pre_row = self.listView_7.currentRow() - 1 if self.listView_7.currentRow() != 0 else self.listView_7.count() - 1
        self.listView_7.setCurrentRow(pre_row)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False

    '''下一首'''

    def nextMusic(self):
        self.slider.setValue(0)
        if self.listView_7.count() == 0:
            self.Tips('当前路径内无可播放的音乐文件')
            return
        next_row = self.listView_7.currentRow() + 1 if self.listView_7.currentRow() != self.listView_7.count() - 1 else 0
        self.listView_7.setCurrentRow(next_row)
        self.is_switching = True
        self.setCurPlaying()
        self.playMusic()
        self.is_switching = False
# import image_rc


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    Mainwindow=QtWidgets.QMainWindow()
    Mainwindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
    # Mainwindow.setWindowOpacity(0.9)  # 设置窗口透明度
    Mainwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
    ui=Ui_Form()
    ui.setupUi(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())