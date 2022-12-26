# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyModbus.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(689, 449)
        Form.setMinimumSize(QtCore.QSize(689, 449))
        Form.setMaximumSize(QtCore.QSize(689, 449))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        Form.setFont(font)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 11, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 43, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ipTxt = QtWidgets.QLineEdit(Form)
        self.ipTxt.setGeometry(QtCore.QRect(80, 7, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ipTxt.setFont(font)
        self.ipTxt.setInputMask("")
        self.ipTxt.setMaxLength(16)
        self.ipTxt.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.ipTxt.setObjectName("ipTxt")
        self.portTxt = QtWidgets.QLineEdit(Form)
        self.portTxt.setGeometry(QtCore.QRect(80, 40, 71, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.portTxt.setFont(font)
        self.portTxt.setInputMethodHints(QtCore.Qt.ImhNone)
        self.portTxt.setInputMask("")
        self.portTxt.setMaxLength(32767)
        self.portTxt.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.portTxt.setObjectName("portTxt")
        self.openBtn = QtWidgets.QPushButton(Form)
        self.openBtn.setGeometry(QtCore.QRect(10, 80, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.openBtn.setFont(font)
        self.openBtn.setObjectName("openBtn")
        self.closeBtn = QtWidgets.QPushButton(Form)
        self.closeBtn.setEnabled(True)
        self.closeBtn.setGeometry(QtCore.QRect(130, 80, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.closeBtn.setFont(font)
        self.closeBtn.setObjectName("closeBtn")
        self.rwDregister = QtWidgets.QGroupBox(Form)
        self.rwDregister.setGeometry(QtCore.QRect(10, 140, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rwDregister.setFont(font)
        self.rwDregister.setObjectName("rwDregister")
        self.dReadBtn = QtWidgets.QPushButton(self.rwDregister)
        self.dReadBtn.setGeometry(QtCore.QRect(13, 90, 75, 23))
        self.dReadBtn.setObjectName("dReadBtn")
        self.dWriteBtn = QtWidgets.QPushButton(self.rwDregister)
        self.dWriteBtn.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.dWriteBtn.setObjectName("dWriteBtn")
        self.label_3 = QtWidgets.QLabel(self.rwDregister)
        self.label_3.setGeometry(QtCore.QRect(13, 30, 47, 13))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.dAddrTxt = QtWidgets.QLineEdit(self.rwDregister)
        self.dAddrTxt.setGeometry(QtCore.QRect(13, 50, 71, 23))
        self.dAddrTxt.setObjectName("dAddrTxt")
        self.label_8 = QtWidgets.QLabel(self.rwDregister)
        self.label_8.setGeometry(QtCore.QRect(130, 30, 61, 13))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.dValTxt = QtWidgets.QLineEdit(self.rwDregister)
        self.dValTxt.setGeometry(QtCore.QRect(130, 50, 71, 23))
        self.dValTxt.setObjectName("dValTxt")
        self.rwWregister = QtWidgets.QGroupBox(Form)
        self.rwWregister.setGeometry(QtCore.QRect(10, 310, 221, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.rwWregister.setFont(font)
        self.rwWregister.setObjectName("rwWregister")
        self.label_5 = QtWidgets.QLabel(self.rwWregister)
        self.label_5.setGeometry(QtCore.QRect(13, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.wAddrTxt = QtWidgets.QLineEdit(self.rwWregister)
        self.wAddrTxt.setGeometry(QtCore.QRect(13, 50, 51, 23))
        self.wAddrTxt.setObjectName("wAddrTxt")
        self.label_6 = QtWidgets.QLabel(self.rwWregister)
        self.label_6.setGeometry(QtCore.QRect(80, 30, 47, 13))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.wBitTxt = QtWidgets.QLineEdit(self.rwWregister)
        self.wBitTxt.setGeometry(QtCore.QRect(80, 50, 51, 23))
        self.wBitTxt.setObjectName("wBitTxt")
        self.wReadBtn = QtWidgets.QPushButton(self.rwWregister)
        self.wReadBtn.setGeometry(QtCore.QRect(13, 90, 75, 23))
        self.wReadBtn.setObjectName("wReadBtn")
        self.wWriteBtn = QtWidgets.QPushButton(self.rwWregister)
        self.wWriteBtn.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.wWriteBtn.setObjectName("wWriteBtn")
        self.label_7 = QtWidgets.QLabel(self.rwWregister)
        self.label_7.setGeometry(QtCore.QRect(150, 30, 61, 13))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.wValTxt = QtWidgets.QLineEdit(self.rwWregister)
        self.wValTxt.setGeometry(QtCore.QRect(150, 50, 51, 23))
        self.wValTxt.setObjectName("wValTxt")
        self.outputTxt = QtWidgets.QTextEdit(Form)
        self.outputTxt.setEnabled(True)
        self.outputTxt.setGeometry(QtCore.QRect(270, 40, 401, 391))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.outputTxt.setFont(font)
        self.outputTxt.setMouseTracking(False)
        self.outputTxt.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.outputTxt.setFrameShape(QtWidgets.QFrame.Box)
        self.outputTxt.setReadOnly(True)
        self.outputTxt.setObjectName("outputTxt")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(270, 11, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setEnabled(True)
        self.clearBtn.setGeometry(QtCore.QRect(570, 10, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clearBtn.setFont(font)
        self.clearBtn.setObjectName("clearBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Omron_pyModbus TCP/IP"))
        self.label.setText(_translate("Form", "IP"))
        self.label_2.setText(_translate("Form", "Port"))
        self.ipTxt.setText(_translate("Form", "192.168.250.0"))
        self.portTxt.setText(_translate("Form", "502"))
        self.openBtn.setText(_translate("Form", "Open"))
        self.closeBtn.setText(_translate("Form", "Close"))
        self.rwDregister.setTitle(_translate("Form", "R/W Holding Register"))
        self.dReadBtn.setText(_translate("Form", "Read"))
        self.dWriteBtn.setText(_translate("Form", "Write"))
        self.label_3.setText(_translate("Form", "Addr:"))
        self.label_8.setText(_translate("Form", "Value:"))
        self.rwWregister.setTitle(_translate("Form", "R/W Work Register"))
        self.label_5.setText(_translate("Form", "Addr:"))
        self.label_6.setText(_translate("Form", "Bit:"))
        self.wReadBtn.setText(_translate("Form", "Read"))
        self.wWriteBtn.setText(_translate("Form", "Write"))
        self.label_7.setText(_translate("Form", "Value:"))
        self.label_9.setText(_translate("Form", "Response"))
        self.clearBtn.setText(_translate("Form", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())