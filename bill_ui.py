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
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 621)
        Form.setMinimumSize(QSize(850, 0))
        self.horizontalLayout_8 = QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_3 = QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Table = QTableWidget(self.tab)
        if (self.Table.columnCount() < 7):
            self.Table.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.Table.setObjectName(u"Table")
        self.Table.setLayoutDirection(Qt.LeftToRight)
        self.Table.setStyleSheet(u"/*\u8868\u683c\u7684\u4e00\u79cd\u7f8e\u5316\u65b9\u5f0f*/\n"
"QHeaderView{\n"
"    /*font-size:18px;*/\n"
"    background:transparent;\n"
"}\n"
"/* \u8868\u683c\u5934\u90e8\u7684\u5de6\u4e0a\u89d2\u6309\u94ae */\n"
"QTableCornerButton::section{\n"
"	background:rgb(126, 145, 176);\n"
"}\n"
"/* \u8868\u683c\u5934\u90e8\u7684\u5217\u540d */\n"
"QHeaderView::section{\n"
"    color:#FFFFFF;\n"
"    background:rgb(126, 145, 176);\n"
"    border:none;\n"
"	border-left: 1px solid #333333;\n"
"    text-align:center;\n"
"    padding-left:2px;\n"
"	padding-right:2px;\n"
"}\n"
"/* \u8868\u683c\u63a7\u4ef6 */\n"
"QTableWidget{\n"
"    background:#FFFFFF;\n"
"    border:none;\n"
"	outline:none;\n"
"    /*font-size:18px;*/\n"
"    color:#666666;\n"
"}\n"
"\n"
"/* \u8868\u683c\u4e2d\u9009\u4e2d\u7684\u5355\u5143\u683c */\n"
"QTableWidget::item::selected{\n"
"    color:rgb(0, 0, 0);\n"
"    background:#449EFF;\n"
"}\n"
"\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u6837\u5f0f */\n"
"QScrollBar::vertical{\n"
"background:transp"
                        "arent;\n"
"width:12px;\n"
"border:none;\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u5411\u4e0a\u7bad\u5934 */\n"
"QScrollBar::add-line:vertical{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u5411\u4e0b\u7bad\u5934 */\n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u5411\u4e0a\u6ed1\u5757 */\n"
"QScrollBar::add-page:vertical{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u5411\u4e0b\u6ed1\u5757 */\n"
"QScrollBar::sub-page:vertical{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u6ed1\u5757 */\n"
"QScrollBar::handle:vertical{\n"
"background: rgba(111, 134, 147, 100);\n"
"border-radius:4px;\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684\u6ed1\u5757\u60ac\u505c\u65f6 */\n"
"QScrollBar::handle:vertical:hover{\n"
"background: rgba(111, 134, 147, 180);\n"
"}\n"
"/* \u5782\u76f4\u6eda\u52a8\u6761\u7684"
                        "\u6ed1\u5757\u6309\u4e0b\u65f6 */\n"
"QScrollBar::handle:vertical:pressed{\n"
"background: rgba(111, 134, 147, 255);\n"
"}\n"
"\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u6837\u5f0f */\n"
"QScrollBar::horizontal{\n"
"background:transparent;\n"
"height:12px;\n"
"border:none;\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u5411\u5de6\u7bad\u5934 */\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u5411\u53f3\u7bad\u5934 */\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"border:none;\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u5411\u5de6\u6ed1\u5757 */\n"
"QScrollBar::add-page:horizontal{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u5411\u53f3\u6ed1\u5757 */\n"
"QScrollBar::sub-page:horizontal{\n"
"background:transparent;\n"
"border:none;\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u6ed1\u5757 */\n"
"QScrollBar::handle:horizontal{\n"
"background: rgba(111, "
                        "134, 147, 100);\n"
"border-radius:4px;\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u6ed1\u5757\u60ac\u505c\u65f6 */\n"
"QScrollBar::handle:horizontal:hover{\n"
"background: rgba(111, 134, 147, 180);\n"
"}\n"
"/* \u6c34\u5e73\u6eda\u52a8\u6761\u7684\u6ed1\u5757\u6309\u4e0b\u65f6 */\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background: rgba(111, 134, 147, 255);\n"
"}\n"
"\n"
"")
        self.Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Table.setGridStyle(Qt.SolidLine)

        self.horizontalLayout_3.addWidget(self.Table)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout_9 = QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Table_old = QTableWidget(self.tab_2)
        if (self.Table_old.columnCount() < 7):
            self.Table_old.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setText(u"\u76ee\u6807\u5bf9\u8c61");
        self.Table_old.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setText(u"\u6b20\u6b3e\u91d1\u989d");
        self.Table_old.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setText(u"\u5165\u8d26\u65e5\u671f");
        self.Table_old.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setText(u"\u51fa\u8d26\u65e5\u671f");
        self.Table_old.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setText(u"\u6b20\u6b3e\u7c7b\u578b");
        self.Table_old.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Table_old.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Table_old.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.Table_old.setObjectName(u"Table_old")
        self.Table_old.setLayoutDirection(Qt.LeftToRight)
        self.Table_old.setStyleSheet(u"/*\u8868\u683c\u7684\u4e00\u79cd\u7f8e\u5316\u65b9\u5f0f*/\n"
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
        self.Table_old.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Table_old.setSelectionMode(QAbstractItemView.SingleSelection)
        self.Table_old.setGridStyle(Qt.SolidLine)

        self.horizontalLayout_9.addWidget(self.Table_old)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_8.addWidget(self.tabWidget)

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
        self.FinishTodoButton = QPushButton(self.Right_other)
        self.FinishTodoButton.setObjectName(u"FinishTodoButton")

        self.verticalLayout_2.addWidget(self.FinishTodoButton)

        self.UpdateTodoButton = QPushButton(self.Right_other)
        self.UpdateTodoButton.setObjectName(u"UpdateTodoButton")

        self.verticalLayout_2.addWidget(self.UpdateTodoButton)

        self.OutputTodoButton = QPushButton(self.Right_other)
        self.OutputTodoButton.setObjectName(u"OutputTodoButton")

        self.verticalLayout_2.addWidget(self.OutputTodoButton)


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

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8d26\u5355\u8bb0\u5f55\u5de5\u5177", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(5)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None));
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(6)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"id", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5f85\u529e", None))
        ___qtablewidgetitem2 = self.Table_old.horizontalHeaderItem(5)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u5907\u6ce8", None));
        ___qtablewidgetitem3 = self.Table_old.horizontalHeaderItem(6)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"id", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u5df2\u529e", None))
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
        self.FinishTodoButton.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210\u4efb\u52a1", None))
        self.UpdateTodoButton.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u4efb\u52a1", None))
        self.OutputTodoButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u8868\u683c", None))
        self.Right_message.setTitle(QCoreApplication.translate("Form", u"\u6d88\u606f", None))
        self.MessageLabel.setText("")
    # retranslateUi

