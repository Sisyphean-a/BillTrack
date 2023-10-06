# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateTodo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(364, 359)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.ObjectEdit = QLineEdit(Form)
        self.ObjectEdit.setObjectName(u"ObjectEdit")

        self.horizontalLayout.addWidget(self.ObjectEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.MoneyEdit = QLineEdit(Form)
        self.MoneyEdit.setObjectName(u"MoneyEdit")

        self.horizontalLayout_2.addWidget(self.MoneyEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.InDateEdit = QDateEdit(Form)
        self.InDateEdit.setObjectName(u"InDateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InDateEdit.sizePolicy().hasHeightForWidth())
        self.InDateEdit.setSizePolicy(sizePolicy)
        self.InDateEdit.setAlignment(Qt.AlignCenter)
        self.InDateEdit.setTimeSpec(Qt.UTC)

        self.horizontalLayout_6.addWidget(self.InDateEdit)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.OutDateEdit = QDateEdit(Form)
        self.OutDateEdit.setObjectName(u"OutDateEdit")
        self.OutDateEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.OutDateEdit)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.TypeEdit = QComboBox(Form)
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.addItem("")
        self.TypeEdit.setObjectName(u"TypeEdit")

        self.horizontalLayout_4.addWidget(self.TypeEdit)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.RemarkEdit = QLineEdit(Form)
        self.RemarkEdit.setObjectName(u"RemarkEdit")

        self.horizontalLayout_5.addWidget(self.RemarkEdit)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.UpdateButton = QPushButton(Form)
        self.UpdateButton.setObjectName(u"UpdateButton")

        self.verticalLayout_2.addWidget(self.UpdateButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4fee\u6539\u4efb\u52a1", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u5bf9\u8c61", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6b20\u6b3e\u91d1\u989d", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5165\u8d26\u65e5\u671f", None))
        self.InDateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u51fa\u8d26\u65e5\u671f", None))
        self.OutDateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6b20\u6b3e\u7c7b\u578b", None))
        self.TypeEdit.setItemText(0, QCoreApplication.translate("Form", u"\u82b1\u5457", None))
        self.TypeEdit.setItemText(1, QCoreApplication.translate("Form", u"\u501f\u5457", None))
        self.TypeEdit.setItemText(2, QCoreApplication.translate("Form", u"\u7f51\u5546\u8d37", None))
        self.TypeEdit.setItemText(3, QCoreApplication.translate("Form", u"\u91d1\u661f", None))
        self.TypeEdit.setItemText(4, QCoreApplication.translate("Form", u"\u5f69\u9676\u574a", None))
        self.TypeEdit.setItemText(5, QCoreApplication.translate("Form", u"\u501f\u6b3e", None))
        self.TypeEdit.setItemText(6, QCoreApplication.translate("Form", u"\u8d37\u6b3e", None))
        self.TypeEdit.setItemText(7, QCoreApplication.translate("Form", u"\u5176\u4ed6", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u5907       \u6ce8", None))
        self.UpdateButton.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210\u4fee\u6539", None))
    # retranslateUi

