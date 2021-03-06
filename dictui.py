# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dict_Window(object):
    def setupUi(self, Dict_Window):
        Dict_Window.setObjectName("Dict_Window")
        Dict_Window.resize(500, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Assets/Assets/letter-v-button-of-square-shape-with-one-rounded-corner.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dict_Window.setWindowIcon(icon)
        Dict_Window.setStyleSheet("background-color: rgb(248, 249, 250);")
        self.centralwidget = QtWidgets.QWidget(Dict_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgb(42, 77, 105);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 bold italic 19pt \"Times New Roman\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(0, 380, 125, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.home_button.setFont(font)
        self.home_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Assets/Assets/home (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QtCore.QSize(100, 40))
        self.home_button.setObjectName("home_button")
        self.dictionary_button = QtWidgets.QPushButton(self.centralwidget)
        self.dictionary_button.setGeometry(QtCore.QRect(125, 380, 125, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.dictionary_button.setFont(font)
        self.dictionary_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Assets/Assets/big-dictionary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dictionary_button.setIcon(icon2)
        self.dictionary_button.setIconSize(QtCore.QSize(100, 40))
        self.dictionary_button.setObjectName("dictionary_button")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(375, 380, 125, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.exit_button.setFont(font)
        self.exit_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Assets/Assets/logout (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon3)
        self.exit_button.setIconSize(QtCore.QSize(100, 40))
        self.exit_button.setObjectName("exit_button")
        self.more_button = QtWidgets.QPushButton(self.centralwidget)
        self.more_button.setGeometry(QtCore.QRect(250, 380, 125, 80))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.more_button.setFont(font)
        self.more_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Assets/Assets/apps.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.more_button.setIcon(icon4)
        self.more_button.setIconSize(QtCore.QSize(100, 40))
        self.more_button.setObjectName("more_button")
        self.SR = QtWidgets.QGroupBox(self.centralwidget)
        self.SR.setGeometry(QtCore.QRect(5, 110, 490, 270))
        self.SR.setMinimumSize(QtCore.QSize(490, 270))
        self.SR.setMaximumSize(QtCore.QSize(490, 270))
        self.SR.setBaseSize(QtCore.QSize(1, 1))
        self.SR.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SR.setAutoFillBackground(False)
        self.SR.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"background-color: rgb(248, 249, 250);\n"
"gridline-color: rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.SR.setObjectName("SR")
        self.word = QtWidgets.QLabel(self.SR)
        self.word.setGeometry(QtCore.QRect(15, 20, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.word.setFont(font)
        self.word.setStyleSheet("font: 18pt \"Cambria\";\n"
"color: rgb(0, 0, 127);")
        self.word.setText("")
        self.word.setTextFormat(QtCore.Qt.AutoText)
        self.word.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.word.setWordWrap(False)
        self.word.setObjectName("word")
        self.word_def = QtWidgets.QLabel(self.SR)
        self.word_def.setGeometry(QtCore.QRect(10, 150, 471, 110))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.word_def.setFont(font)
        self.word_def.setStatusTip("")
        self.word_def.setStyleSheet("font: 12pt \"Constantia\";\n"
"gridline-color: rgb(170, 170, 255);")
        self.word_def.setText("")
        self.word_def.setScaledContents(True)
        self.word_def.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.word_def.setWordWrap(True)
        self.word_def.setObjectName("word_def")
        self.pronunciation = QtWidgets.QLabel(self.SR)
        self.pronunciation.setGeometry(QtCore.QRect(15, 60, 480, 40))
        self.pronunciation.setStyleSheet("font: italic 12pt \"Times New Roman\";")
        self.pronunciation.setText("")
        self.pronunciation.setWordWrap(True)
        self.pronunciation.setObjectName("pronunciation")
        self.word_type = QtWidgets.QLabel(self.SR)
        self.word_type.setGeometry(QtCore.QRect(10, 120, 471, 30))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.word_type.setFont(font)
        self.word_type.setStyleSheet("font: 12pt \"Cambria\";\n"
"border-top:1px solid  rgb(234, 234, 234);")
        self.word_type.setText("")
        self.word_type.setScaledContents(True)
        self.word_type.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.word_type.setObjectName("word_type")
        self.t2s_button = QtWidgets.QPushButton(self.SR)
        self.t2s_button.setGeometry(QtCore.QRect(445, 20, 40, 40))
        self.t2s_button.setStyleSheet("border:none")
        self.t2s_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Assets/Assets/baseline_volume_up_black_18dp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.t2s_button.setIcon(icon5)
        self.t2s_button.setIconSize(QtCore.QSize(20, 30))
        self.t2s_button.setDefault(True)
        self.t2s_button.setObjectName("t2s_button")
        self.search_input = QtWidgets.QTextEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(5, 75, 350, 35))
        self.search_input.setMinimumSize(QtCore.QSize(330, 30))
        self.search_input.setMaximumSize(QtCore.QSize(350, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.search_input.setFont(font)
        self.search_input.setStyleSheet("font: italic 12pt \"Times New Roman\";")
        self.search_input.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.search_input.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.search_input.setObjectName("search_input")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(370, 75, 110, 35))
        self.search_button.setStyleSheet("font: italic bold 12pt \"Cambria\";\n"
"background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.search_button.setObjectName("search_button")
        Dict_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Dict_Window)
        self.statusbar.setObjectName("statusbar")
        Dict_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Dict_Window)
        QtCore.QMetaObject.connectSlotsByName(Dict_Window)

    def retranslateUi(self, Dict_Window):
        _translate = QtCore.QCoreApplication.translate
        Dict_Window.setWindowTitle(_translate("Dict_Window", "Dictionary"))
        self.label.setText(_translate("Dict_Window", "VOCA : VOCABULARY BUILDING TOOL"))
        self.home_button.setStatusTip(_translate("Dict_Window", "Home"))
        self.dictionary_button.setStatusTip(_translate("Dict_Window", "Dictionary"))
        self.exit_button.setStatusTip(_translate("Dict_Window", "Exit"))
        self.more_button.setStatusTip(_translate("Dict_Window", "More"))
        self.SR.setTitle(_translate("Dict_Window", "SEARCH RESULT"))
        self.t2s_button.setStatusTip(_translate("Dict_Window", "speech"))
        self.search_input.setPlaceholderText(_translate("Dict_Window", "Enter a word"))
        self.search_button.setStatusTip(_translate("Dict_Window", "Search"))
        self.search_button.setText(_translate("Dict_Window", "SEARCH"))
import Main_rc
