import sys 
import csv
import re
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QAction, QHeaderView, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QPainter, QStandardItemModel, QIcon, QFontInfo, QWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries
from PyQt5 import uic, QtWidgets
import mysql.connector
from mysql.connector import cursor
from reportlab.pdfgen import canvas

# Variavel Global
numero_id = 0

# Conector do banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastroDePeca"
)

# Primeira tela
def MainForm():
    line1 = form.lineEdit.text()
    print("Nome da Cliente: ", line1)
    
    line2 = form.lineEdit_2.text()
    print("Nome da Peça: ", line2)

    line3 = form.lineEdit_3.text()
    print("Data de entrega: ", line3)

    line4 = form.lineEdit_4.text()
    print("Quantidade do Pedido:", line4)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cadastro (Nome,NomePeça,DataPedido,QuantPedido) VALUES (%s,%s,%s,%s)"
    dados = (str(line1),str(line2),str(line3),str(line4))
    cursor.execute(comando_SQL,dados)
    banco.commit()

    form.lineEdit.setText("")
    form.lineEdit_2.setText("")
    form.lineEdit_3.setText("")
    form.lineEdit_4.setText("")

# Segunda tela
def Data():
    data.show()
    
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadastro"
    cursor.execute(comando_SQL)
    dadosLidos= cursor.fetchall()

    data.tableWidget.setRowCount(len(dadosLidos))
    data.tableWidget.setColumnCount(5)

    for i in range(0, len(dadosLidos)):
        for j in range(0,5):
           data.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadosLidos[i][j])))

# Botão da segunda tela de gerar PDF
def gerarPDF():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cadastro"
    cursor.execute(comando_SQL)
    dadosLidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("CadastroDeClientes.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Clientes Cadastrados:")   
    pdf.setFont("Times-Bold", 18)

    #pdf.drawString(10,750, "ID") 
    #pdf.drawString(110,750, "Nome do Cliente") 
    #pdf.drawString(210,750, "Nome da Peça") 
    #pdf.drawString(310,750, "Data de Entrega") 
    #pdf.drawString(410,750, "Quantidade do Pedido") 

    for i in range(0, len(dadosLidos)):
        y = y + 50
        pdf.drawString(11,750 - y, str(dadosLidos[i][0]))
        pdf.drawString(111,750 - y, str(dadosLidos[i][1]))
        pdf.drawString(211,750 - y, str(dadosLidos[i][2]))
        pdf.drawString(311,750 - y, str(dadosLidos[i][3]))
        pdf.drawString(411,750 - y, str(dadosLidos[i][4]))

    pdf.save()
    print("PDF gerado com sucesso!")

# Botão da segunda tela de excluir itens do banco
def Delete():
    linha = data.tableWidget.currentRow()
    data.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dadosLidos = cursor.fetchall()
    valor_id = dadosLidos[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id=" + str(valor_id))

# Botão da segunda tela de editar itens do banco
def EditarItens():
    editar.show()

    global numero_id

    linha = data.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dadosLidos = cursor.fetchall()
    valor_id = dadosLidos[linha][0]
    cursor.execute("SELECT * FROM cadastro WHERE id=" + str(valor_id))
    produto = cursor.fetchall()

    numero_id = valor_id

    editar.lineEdit.setText(str(produto[0][0]))
    editar.lineEdit_2.setText(str(produto[0][1]))
    editar.lineEdit_3.setText(str(produto[0][2]))
    editar.lineEdit_4.setText(str(produto[0][3]))
    editar.lineEdit_5.setText(str(produto[0][4]))

# Chamando a terceira tela para editar itens e salvar do banco
def salvarDadosEditados():
    #pega o numero do id
    global numero_id
    # valor digitado no lineEdit
    Nome = editar.lineEdit_2.text()
    NomePeça = editar.lineEdit_3.text()
    DataPedido = editar.lineEdit_4.text()
    QuantPedido = editar.lineEdit_5.text()
    # atualizar os dados no banco
    cursor = banco.cursor()
    cursor.execute("UPDATE cadastro SET Nome = '{}', NomePeça = '{}', DataPedido = '{}', QuantPedido = '{}' WHERE id = {}".format(Nome,NomePeça,DataPedido,QuantPedido,numero_id))
    banco.commit()
    #atualizar a janela
    editar.close()
    data.close()
    Data()

app = QtWidgets.QApplication([])

# Primeira tela
form = uic.loadUi("formulario.ui")
# Segunda tela
data = uic.loadUi("banco.ui")
# Terceira tela
editar = uic.loadUi("EditorDados.ui")

# Botão da primeira tela de cadastrar cliente
form.pushButton.clicked.connect(MainForm)
# Botão da primeira tela de acesso ao banco de cadastros
form.pushButton_2.clicked.connect(Data)
# Botão da segunda tela de gerar PDF do banco
data.pushButton.clicked.connect(gerarPDF)
# Botão da segunda tela de excluir itens do banco
data.pushButton_2.clicked.connect(Delete)
# Botão da segunda tela de editar itens no banco
data.pushButton_3.clicked.connect(EditarItens)
# Botão da terceira tela de salvar itens editados do banco
editar.pushButton.clicked.connect(salvarDadosEditados)

form.show()
app.exec()
