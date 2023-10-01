# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bill.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(880, 621)
        Form.setMinimumSize(QSize(850, 0))
        self.horizontalLayout_8 = QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Table = QTableWidget(Form)
        if (self.Table.columnCount() < 6):
            self.Table.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setText(u"\u76ee\u6807\u5bf9\u8c61");
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setText(u"\u6b20\u6b3e\u91d1\u989d");
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setText(u"\u5165\u8d26\u65e5\u671f");
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setText(u"\u51fa\u8d26\u65e5\u671f");
        self.Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setText(u"\u6b20\u6b3e\u7c7b\u578b");
        self.Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.Table.setObjectName(u"Table")
        self.Table.setLayoutDirection(Qt.LeftToRight)
        self.Table.setStyleSheet(u"/*\u8868\u683c\u7684\u4e00\u79cd\u7f8e\u5316\u65b9\u5f0f*/\n"
"QHeaderView{\n"
"    /*font-size:18px;*/\n"
"    background:transparent;\n"
"}\n"
"QTableCornerButton::section{\n"
"	background:rgb(126, 145, 176);\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    color:#FFFFFF;\n"
"    background:rgb(126, 145, 176);\n"
"    border:none;\n"
"	border-left: 1px solid #333333;\n"
"    text-align:center;\n"
"    padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"    background:#FFFFFF;\n"
"    border:none;\n"
"	outline:none;\n"
"    /*font-size:18px;*/\n"
"    color:#666666;\n"
"}\n"
"\n"
"QTableWidget::item{\n"
"	border-left:1px solid #EEF1F7;\n"
"    border-bottom:1px solid #EEF1F7;\n"
"}\n"
"\n"
"QTableWidget::item::selected{\n"
"    color:rgb(0, 0, 0);\n"
"    background:#449EFF;\n"
"}\n"
"/* QScrollBar Vertical Style */\n"
"QScrollBar::vertical{\n"
"background:transparent;\n"
"width:12px;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"border:none;\n"
"}\n"
""
                        "\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background: rgba(111, 134, 147, 100);\n"
"border-radius:4px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background: rgba(111, 134, 147, 180);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background: rgba(111, 134, 147, 255);\n"
"}\n"
"\n"
"/* QScrollBar Horizontal Style */\n"
"QScrollBar::horizontal{\n"
"background:transparent;\n"
"height:12px;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:tr"
                        "ansparent;\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background: rgba(111, 134, 147, 100);\n"
"border-radius:4px;\n"
"\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background: rgba(111, 134, 147, 180);\n"
"}\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background: rgba(111, 134, 147, 255);\n"
"}\n"
"")
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Table.setGridStyle(Qt.SolidLine)

        self.horizontalLayout_8.addWidget(self.Table)

        self.Right_layout = QVBoxLayout()
        self.Right_layout.setObjectName(u"Right_layout")
        self.Right_add = QGroupBox(Form)
        self.Right_add.setObjectName(u"Right_add")
        self.Right_add.setMinimumSize(QSize(210, 0))
        self.verticalLayout = QVBoxLayout(self.Right_add)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.Right_add)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.ObjectEdit = QLineEdit(self.Right_add)
        self.ObjectEdit.setObjectName(u"ObjectEdit")

        self.horizontalLayout.addWidget(self.ObjectEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.Right_add)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.MoneyEdit = QLineEdit(self.Right_add)
        self.MoneyEdit.setObjectName(u"MoneyEdit")

        self.horizontalLayout_2.addWidget(self.MoneyEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.Right_add)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.InDateEdit = QDateEdit(self.Right_add)
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

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.Right_add)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.OutDateEdit = QDateEdit(self.Right_add)
        self.OutDateEdit.setObjectName(u"OutDateEdit")
        self.OutDateEdit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.OutDateEdit)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.Right_add)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.TypeEdit = QComboBox(self.Right_add)
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

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.Right_add)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.RemarkEdit = QLineEdit(self.Right_add)
        self.RemarkEdit.setObjectName(u"RemarkEdit")

        self.horizontalLayout_5.addWidget(self.RemarkEdit)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.AddTodoButton = QPushButton(self.Right_add)
        self.AddTodoButton.setObjectName(u"AddTodoButton")

        self.verticalLayout.addWidget(self.AddTodoButton)


        self.Right_layout.addWidget(self.Right_add)

        self.Right_other = QGroupBox(Form)
        self.Right_other.setObjectName(u"Right_other")
        self.verticalLayout_2 = QVBoxLayout(self.Right_other)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.DeleteTodoButton = QPushButton(self.Right_other)
        self.DeleteTodoButton.setObjectName(u"DeleteTodoButton")

        self.verticalLayout_2.addWidget(self.DeleteTodoButton)

        self.UpdateTodoButton = QPushButton(self.Right_other)
        self.UpdateTodoButton.setObjectName(u"UpdateTodoButton")

        self.verticalLayout_2.addWidget(self.UpdateTodoButton)

        self.FinishTodoButton = QPushButton(self.Right_other)
        self.FinishTodoButton.setObjectName(u"FinishTodoButton")

        self.verticalLayout_2.addWidget(self.FinishTodoButton)


        self.Right_layout.addWidget(self.Right_other)

        self.Right_message = QGroupBox(Form)
        self.Right_message.setObjectName(u"Right_message")
        self.verticalLayout_4 = QVBoxLayout(self.Right_message)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.MessageLabel = QLabel(self.Right_message)
        self.MessageLabel.setObjectName(u"MessageLabel")
        self.MessageLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.MessageLabel)


        self.Right_layout.addWidget(self.Right_message)

        self.Right_layout.setStretch(0, 2)
        self.Right_layout.setStretch(1, 1)
        self.Right_layout.setStretch(2, 1)

        self.horizontalLayout_8.addLayout(self.Right_layout)

        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8d26\u5355\u8bb0\u5f55\u5de5\u5177", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(5)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None));
        self.Right_add.setTitle(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u5bf9\u8c61", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6b20\u6b3e\u91d1\u989d", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5165\u8d26\u65e5\u671f", None))
        self.InDateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u51fa\u8d26\u7c7b\u578b", None))
        self.OutDateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/dd", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6b20\u6b3e\u7c7b\u578b", None))
        self.TypeEdit.setItemText(0, QCoreApplication.translate("Form", u"\u82b1\u5457", None))
        self.TypeEdit.setItemText(1, QCoreApplication.translate("Form", u"\u501f\u5457", None))
        self.TypeEdit.setItemText(2, QCoreApplication.translate("Form", u"\u7f51\u5546\u8d37", None))
        self.TypeEdit.setItemText(3, QCoreApplication.translate("Form", u"\u91d1\u661f", None))
        self.TypeEdit.setItemText(4, QCoreApplication.translate("Form", u"\u5f69\u9676\u574a", None))
        self.TypeEdit.setItemText(5, QCoreApplication.translate("Form", u"\u501f\u6b3e", None))
        self.TypeEdit.setItemText(6, QCoreApplication.translate("Form", u"\u5176\u4ed6", None))

        self.label_5.setText(QCoreApplication.translate("Form", u"\u5907       \u6ce8", None))
        self.AddTodoButton.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u4efb\u52a1", None))
        self.Right_other.setTitle(QCoreApplication.translate("Form", u"\u5176\u4ed6", None))
        self.DeleteTodoButton.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u4efb\u52a1", None))
        self.UpdateTodoButton.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u4efb\u52a1", None))
        self.FinishTodoButton.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210\u4efb\u52a1", None))
        self.Right_message.setTitle(QCoreApplication.translate("Form", u"\u6d88\u606f", None))
        self.MessageLabel.setText("")
    # retranslateUi

