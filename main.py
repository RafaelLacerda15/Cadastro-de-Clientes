################################################################################################################################################
# Imports
import os
import sys
import sqlite3
import openpyxl
################################################################################################################################################
# Froms
from ui_inteface import *
from PySide6.QtWidgets import QMessageBox, QFileDialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PySide6.QtGui import QIcon, QPixmap
########################################################################################################################################################
class MainWindow(QMainWindow):
    ####################################################################################################################################################
    #Functions    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ################################################################################################################################################
        # Icon Window
        icon_window = QIcon("Icons\Plano de Fundo.png")
        self.setWindowIcon(icon_window)

        pixmap = QPixmap("Icons\minha-img.png")
        self.ui.img_minha.setPixmap(pixmap)
        ################################################################################################################################################
        # Remove Window
        #self.setWindowFlag(Qt.FramelessWindowHint)
        ################################################################################################################################################
        # Function Buttom
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_home))
        self.ui.btn_register.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_register))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_database))
        self.ui.btn_about.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.list_abount))
        ################################################################################################################################################
        # DataBase
        def exportar_xls():
            # Abrir ou criar o arquivo Excel
            workbook = openpyxl.Workbook()
            sheet = workbook.active

            # Escrever os dados na planilha
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    cell_item = self.ui.tableWidget.item(row, col)
                    if cell_item is not None:
                        cell_value = cell_item.text()
                        sheet.cell(row=row+1, column=col+1, value=cell_value)

            # Salvar o arquivo
            filename, _ = QFileDialog.getSaveFileName(
                self, 'Exportar para Excel', '', 'Arquivo Excel (*.xlsx)'
            )
            if filename:
                workbook.save(filename)
                certo()

        
    ################################################################################################################################################
        # Save Client        
        def save_client():
            print('Certo')
            nome = self.ui.line_nome.text()
            idade = self.ui.line_idade.text()
            celular = self.ui.line_numero.text()
            cep = self.ui.line_cep.text()
            endereco = self.ui.line_endereco.text()
            email = self.ui.line_email.text()

            # Connect to database
            conn = sqlite3.connect('clients.db')
            c = conn.cursor()

            # Create table if it doesn't exist
            c.execute('''CREATE TABLE IF NOT EXISTS clientes
                        (nome text, idade text, celular text, cep text, endereco text, email text)''')

            # Read existing data from table
            c.execute("SELECT * FROM clientes")
            existing_data = c.fetchall()

            # Add new data to list
            new_data = (nome, idade, celular, cep, endereco, email)
            all_data = existing_data + [new_data]

            # Save data to database
            c.execute("DELETE FROM clientes")
            c.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)", all_data)
            conn.commit()

            # Close database connection
            conn.close()
            
            # Adicionar nova linha
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)

            # Preencher as células
            self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(nome))
            self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(idade))
            self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(celular))
            self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(cep))
            self.ui.tableWidget.setItem(row_count, 4, QTableWidgetItem(endereco))
            self.ui.tableWidget.setItem(row_count, 5, QTableWidgetItem(email))

        self.ui.btn_save.clicked.connect(save_client)
        ################################################################################################################################################
        # load DataBase
        def load_data():
            try:
                conn = sqlite3.connect("clients.db")
                cur = conn.cursor()
                cur.execute("SELECT * FROM clientes")
                rows = cur.fetchall()

                for row in rows:
                    nome = row[0]
                    idade = row[1]
                    celular = row[2]
                    cep = row[3]
                    endereco = row[4]
                    email = row[5]

                    # Adicionar nova linha
                    row_count = self.ui.tableWidget.rowCount()
                    self.ui.tableWidget.insertRow(row_count)

                    # Preencher as células
                    self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(nome))
                    self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(idade))
                    self.ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(celular))
                    self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(cep))
                    self.ui.tableWidget.setItem(
                        row_count, 4, QTableWidgetItem(endereco))
                    self.ui.tableWidget.setItem(row_count, 5, QTableWidgetItem(email))

                conn.close()

            except sqlite3.Error as error:
                print("Failed to read data from sqlite table", error)
        load_data()
        ################################################################################################################################################
        # DialogBox
        def certo():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Sua informção foi Salva")
            msg.setWindowTitle("Banco de Dados")
            msg.exec()

        def erro():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Não foi possível salvar. Por favor, digite um nome válido.")
            msg.setWindowTitle("Error")
            msg.exec()

        def check_nome():
            line_nome = self.ui.line_nome.text().strip()
            if line_nome == '':
                erro()
                self.ui.btn_save.setDisabled(True)
            else:
                self.ui.btn_save.setEnabled(True)
                self.ui.btn_save.clicked.connect(certo)

            
        #remove a conexão existente, se houver
            self.ui.line_nome.textChanged.disconnect()
        self.ui.exportar.clicked.connect(exportar_xls)
        self.ui.exportar.clicked.connect(certo)
        self.ui.line_nome.textChanged.connect(check_nome)
        ################################################################################################################################################
        
        
        self.show()
########################################################################
# EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ####################################################################
    
    ####################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
########################################################################
# END===>
########################################################################
