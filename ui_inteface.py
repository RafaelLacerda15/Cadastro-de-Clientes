# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'intefacegwpRvG.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1138, 708)
        MainWindow.setMinimumSize(QSize(1138, 708))
        MainWindow.setMaximumSize(QSize(1138, 708))
        icon = QIcon()
        icon.addFile(u":/icon/Icons/Plano de Fundo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"border-radius: 5px;\n"
"text-align: center;")
        MainWindow.setIconSize(QSize(30, 30))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftmenu = QWidget(self.centralwidget)
        self.leftmenu.setObjectName(u"leftmenu")
        self.leftmenu.setStyleSheet(u"background-color: rgb(0, 80, 80);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.leftmenu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home = QWidget(self.leftmenu)
        self.home.setObjectName(u"home")
        self.verticalLayout_6 = QVBoxLayout(self.home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setStyleSheet(u"color: white;")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_home)


        self.verticalLayout_6.addWidget(self.frame)


        self.verticalLayout.addWidget(self.home)

        self.register_2 = QWidget(self.leftmenu)
        self.register_2.setObjectName(u"register_2")
        self.verticalLayout_8 = QVBoxLayout(self.register_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.register_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_register = QPushButton(self.frame_2)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setStyleSheet(u"color: white;")
        icon2 = QIcon()
        icon2.addFile(u":/icon/Icons/key.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_register.setIcon(icon2)
        self.btn_register.setIconSize(QSize(30, 30))

        self.verticalLayout_7.addWidget(self.btn_register)


        self.verticalLayout_8.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.register_2)

        self.database = QWidget(self.leftmenu)
        self.database.setObjectName(u"database")
        self.verticalLayout_4 = QVBoxLayout(self.database)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.database)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_database = QPushButton(self.frame_3)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icon/Icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon3)
        self.btn_database.setIconSize(QSize(30, 30))

        self.verticalLayout_9.addWidget(self.btn_database)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.database)

        self.abount = QWidget(self.leftmenu)
        self.abount.setObjectName(u"abount")
        self.verticalLayout_3 = QVBoxLayout(self.abount)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.abount)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_about = QPushButton(self.frame_4)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setStyleSheet(u"color: rgb(255, 253, 253);")
        icon4 = QIcon()
        icon4.addFile(u":/icon/Icons/at-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon4)
        self.btn_about.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.btn_about)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.abount)


        self.horizontalLayout.addWidget(self.leftmenu, 0, Qt.AlignLeft)

        self.mainmenu = QWidget(self.centralwidget)
        self.mainmenu.setObjectName(u"mainmenu")
        self.mainmenu.setEnabled(True)
        self.mainmenu.setStyleSheet(u"background-color: rgb(0, 113, 113);")
        self.horizontalLayout_3 = QHBoxLayout(self.mainmenu)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.mainmenu)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(803, 0))
        self.stackedWidget.setStyleSheet(u"text-align: center;")
        self.list_home = QWidget()
        self.list_home.setObjectName(u"list_home")
        self.text_home = QTextEdit(self.list_home)
        self.text_home.setObjectName(u"text_home")
        self.text_home.setGeometry(QRect(160, 610, 701, 81))
        self.text_home.setStyleSheet(u"color: white;\n"
"border: none;")
        self.stackedWidget.addWidget(self.list_home)
        self.list_register = QWidget()
        self.list_register.setObjectName(u"list_register")
        self.list_register.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.list_register)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 360, 321, 100))
        self.cep = QVBoxLayout(self.layoutWidget)
        self.cep.setSpacing(0)
        self.cep.setObjectName(u"cep")
        self.cep.setContentsMargins(0, 0, 0, 0)
        self.text_cep = QTextBrowser(self.layoutWidget)
        self.text_cep.setObjectName(u"text_cep")
        self.text_cep.setStyleSheet(u"border: none;")

        self.cep.addWidget(self.text_cep)

        self.line_cep = QLineEdit(self.layoutWidget)
        self.line_cep.setObjectName(u"line_cep")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.line_cep.setFont(font)
        self.line_cep.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 50);")
        self.line_cep.setAlignment(Qt.AlignCenter)
        self.line_cep.setDragEnabled(True)
        self.line_cep.setClearButtonEnabled(True)

        self.cep.addWidget(self.line_cep)

        self.layoutWidget_2 = QWidget(self.list_register)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(50, 130, 321, 100))
        self.idade = QVBoxLayout(self.layoutWidget_2)
        self.idade.setSpacing(0)
        self.idade.setObjectName(u"idade")
        self.idade.setContentsMargins(0, 0, 0, 0)
        self.text_idade = QTextBrowser(self.layoutWidget_2)
        self.text_idade.setObjectName(u"text_idade")
        self.text_idade.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);")

        self.idade.addWidget(self.text_idade)

        self.line_idade = QLineEdit(self.layoutWidget_2)
        self.line_idade.setObjectName(u"line_idade")
        self.line_idade.setFont(font)
        self.line_idade.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 50);")
        self.line_idade.setAlignment(Qt.AlignCenter)
        self.line_idade.setDragEnabled(True)
        self.line_idade.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_idade.setClearButtonEnabled(True)

        self.idade.addWidget(self.line_idade)

        self.layoutWidget_3 = QWidget(self.list_register)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(50, 470, 321, 100))
        self.endereco = QVBoxLayout(self.layoutWidget_3)
        self.endereco.setSpacing(0)
        self.endereco.setObjectName(u"endereco")
        self.endereco.setContentsMargins(0, 0, 0, 0)
        self.text_endereco = QTextBrowser(self.layoutWidget_3)
        self.text_endereco.setObjectName(u"text_endereco")
        self.text_endereco.setStyleSheet(u"border: none;")

        self.endereco.addWidget(self.text_endereco)

        self.line_endereco = QLineEdit(self.layoutWidget_3)
        self.line_endereco.setObjectName(u"line_endereco")
        self.line_endereco.setFont(font)
        self.line_endereco.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 50);")
        self.line_endereco.setAlignment(Qt.AlignCenter)
        self.line_endereco.setDragEnabled(True)
        self.line_endereco.setClearButtonEnabled(True)

        self.endereco.addWidget(self.line_endereco)

        self.btn_save = QPushButton(self.list_register)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(640, 230, 171, 171))
        self.btn_save.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icon/Icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon5)
        self.btn_save.setIconSize(QSize(120, 120))
        self.layoutWidget1 = QWidget(self.list_register)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 580, 321, 100))
        self.email = QVBoxLayout(self.layoutWidget1)
        self.email.setSpacing(0)
        self.email.setObjectName(u"email")
        self.email.setContentsMargins(0, 0, 0, 0)
        self.text_email = QTextBrowser(self.layoutWidget1)
        self.text_email.setObjectName(u"text_email")
        self.text_email.setStyleSheet(u"border: none;")

        self.email.addWidget(self.text_email)

        self.line_email = QLineEdit(self.layoutWidget1)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setFont(font)
        self.line_email.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 50);")
        self.line_email.setAlignment(Qt.AlignCenter)
        self.line_email.setDragEnabled(True)
        self.line_email.setClearButtonEnabled(True)

        self.email.addWidget(self.line_email)

        self.layoutWidget2 = QWidget(self.list_register)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 20, 321, 100))
        self.nome = QVBoxLayout(self.layoutWidget2)
        self.nome.setSpacing(0)
        self.nome.setObjectName(u"nome")
        self.nome.setContentsMargins(0, 0, 0, 0)
        self.text_nome = QTextBrowser(self.layoutWidget2)
        self.text_nome.setObjectName(u"text_nome")
        self.text_nome.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);")

        self.nome.addWidget(self.text_nome)

        self.line_nome = QLineEdit(self.layoutWidget2)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setFont(font)
        self.line_nome.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 50);")
        self.line_nome.setAlignment(Qt.AlignCenter)
        self.line_nome.setDragEnabled(True)
        self.line_nome.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_nome.setClearButtonEnabled(True)

        self.nome.addWidget(self.line_nome)

        self.layoutWidget_4 = QWidget(self.list_register)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(50, 240, 321, 100))
        self.numero = QVBoxLayout(self.layoutWidget_4)
        self.numero.setSpacing(0)
        self.numero.setObjectName(u"numero")
        self.numero.setContentsMargins(0, 0, 0, 0)
        self.text_numero = QTextBrowser(self.layoutWidget_4)
        self.text_numero.setObjectName(u"text_numero")
        self.text_numero.setFont(font)
        self.text_numero.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);")

        self.numero.addWidget(self.text_numero)

        self.line_numero = QLineEdit(self.layoutWidget_4)
        self.line_numero.setObjectName(u"line_numero")
        self.line_numero.setFont(font)
        self.line_numero.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 50);")
        self.line_numero.setAlignment(Qt.AlignCenter)
        self.line_numero.setDragEnabled(True)
        self.line_numero.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.line_numero.setClearButtonEnabled(True)

        self.numero.addWidget(self.line_numero)

        self.stackedWidget.addWidget(self.list_register)
        self.list_database = QWidget()
        self.list_database.setObjectName(u"list_database")
        self.widget_2 = QWidget(self.list_database)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-7, -1, 1251, 891))
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(9, 9, 901, 861))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, -10, 721, 701))
        self.tableWidget.setStyleSheet(u"background-color: rgb(0, 113, 113);")
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setGridStyle(Qt.DotLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)
        self.widget_3 = QWidget(self.frame_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(730, 0, 191, 131))
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(9, 9, 181, 111))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.exportar = QPushButton(self.frame_6)
        self.exportar.setObjectName(u"exportar")
        self.exportar.setGeometry(QRect(10, 20, 161, 71))
        font2 = QFont()
        font2.setPointSize(10)
        self.exportar.setFont(font2)
        self.exportar.setStyleSheet(u"color: white;\n"
"border-radius:10px;")
        self.exportar.setIcon(icon5)
        self.exportar.setIconSize(QSize(30, 30))
        self.stackedWidget.addWidget(self.list_database)
        self.list_abount = QWidget()
        self.list_abount.setObjectName(u"list_abount")
        self.text_abount = QTextEdit(self.list_abount)
        self.text_abount.setObjectName(u"text_abount")
        self.text_abount.setGeometry(QRect(210, 610, 611, 81))
        self.text_abount.setStyleSheet(u"color: white;\n"
"background-color: rgba(0, 0, 0, 150);\n"
"border: none;")
        self.text_abount.setReadOnly(True)
        self.img_minha = QLabel(self.list_abount)
        self.img_minha.setObjectName(u"img_minha")
        self.img_minha.setGeometry(QRect(370, 120, 311, 451))
        self.img_minha.setPixmap(QPixmap(u":/icon/Icons/minha-img.png"))
        self.stackedWidget.addWidget(self.list_abount)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.widget)


        self.horizontalLayout.addWidget(self.mainmenu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DataBase Client", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_database.setText(QCoreApplication.translate("MainWindow", u"Cadastrados", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.text_home.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">Sejam Bem-Vindos ao DataBaseClient</span></p></body></html>", None))
        self.text_cep.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">CEP:</span></p></body></html>", None))
        self.line_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu cep aqui...", None))
        self.text_idade.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Idade:</span></p></body></html>", None))
        self.line_idade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu idade aqui...", None))
        self.text_endereco.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Endere\u00e7o:</span></p></body></html>", None))
        self.line_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu endere\u00e7o aqui...", None))
        self.btn_save.setText("")
        self.text_email.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Email:</span></p></body></html>", None))
        self.line_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu email aqui...", None))
        self.text_nome.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Nome Completo:</span></p></body></html>", None))
        self.line_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu nome aqui...", None))
        self.text_numero.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:15pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Celular:</span></p></body></html>", None))
        self.line_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seu numero aqui...", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"nome completo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"idade", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"celular", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"cep", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"endereco", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"email", None));
        self.exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar para xml", None))
        self.text_abount.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:6px; margin-bottom:6px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Meu nome \u00e9 Rafael, sou desenvolvedor independente.</span></p></body></html>", None))
        self.img_minha.setText("")
    # retranslateUi

