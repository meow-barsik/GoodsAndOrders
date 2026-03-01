import sys
from abc import ABC, ABCMeta, abstractclassmethod
from re import search
import string
import random
import os

import orderWindow as o
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QIntValidator, QDoubleValidator
from PyQt6.QtWidgets import QDialog, QMessageBox, QWidget, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QPushButton, QFileDialog, QTableWidgetItem
import mysql.connector as mysql
from mysql.connector import cursor

from uipy import card
from uipy.card import Ui_Form
from uipy.auth import Ui_Dialog
from uipy.mainWindow import Ui_MainWindow as Client
from uipy.ManagerWindow import Ui_MainWindow as Manager
from uipy.EditAdd import Ui_Dialog as EditAdd
from uipy.AdminWindow import Ui_MainWindow as Admin


def handle_exception(exc_type, exc_value, exc_traceback):
    sys.__excepthook__(exc_type, exc_value, exc_traceback)

sys.excepthook = handle_exception

def databaseConnect():
    try:
        connect = mysql.connect(host='localhost',
                      user='root',
                      passwd='root',
                      db='boots',
                      port=3306)

        if connect.is_connected():
            return connect

    except mysql.Error as e:
        print(e)

class OrderEditDelite(QDialog):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.editBtn = QPushButton("Изменить")
        self.editBtn.clicked.connect(self.editOrder)
        self.deleteBtn = QPushButton("Удалить")
        self.deleteBtn.clicked.connect(self.deleteOrder)

        self.lay = QVBoxLayout()
        self.lay.addWidget(self.editBtn)
        self.lay.addWidget(self.deleteBtn)
        self.setLayout(self.lay)

    def editOrder(self):
        self.dialog = o.OrderEditWindow(self.data)
        self.dialog.exec()

    def deleteOrder(self):
        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute("DELETE FROM order_compose WHERE idOrder = %s;",
                       (self.data[0],))
        connect.commit()
        cursor.execute("DELETE FROM orders WHERE id = %s;",
                       (self.data[0],))
        connect.commit()
        connect.close()

        self.close()

class Card(QPushButton, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.photoUrl = None

#Метакласс для решение конфликтов в различии метаклассов при наследовании
class CombinedMetaclass(type(QMainWindow), ABCMeta):
    pass

class EditOrDeliteWindow(QDialog):
    def __init__(self, card):
        self.card = card
        super().__init__()
        self.editBtn = QPushButton("Изменить")
        self.deleteBtn = QPushButton("Удалить")
        self.editBtn.clicked.connect(self.openEdit)
        self.deleteBtn.clicked.connect(self.delete)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.editBtn)
        self.layout.addWidget(self.deleteBtn)
        self.setLayout(self.layout)


    def openEdit(self):
        self.editWindow = EditDialog(self.card)
        self.editWindow.exec()

    def delete(self):
        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute("select article from goods WHERE nameGood = %s AND price = %s AND descript = %s",
                       (self.card.name.text(),
                        self.card.price.text(),
                        self.card.description.text()))
        article = cursor.fetchone()
        cursor.execute("select idOrder from order_compose WHERE idGood = %s", (article[0],))
        order = cursor.fetchone()
        if order:
            self.msg_win = QMessageBox()
            self.msg_win.setText("Товар существует в заказе")
            self.msg_win.setIcon(self.msg_win.Icon.Critical)
            self.msg_win.button(self.msg_win.StandardButton.Ok)
            self.msg_win.show()
            connect.close()

        else:
            cursor.execute("DELETE FROM goods where article = %s", (article[0],))
            connect.commit()
            connect.close()

            self.msg_win = QMessageBox()
            self.msg_win.setText("Заказ удален")
            self.msg_win.setIcon(self.msg_win.Icon.Information)
            self.msg_win.button(self.msg_win.StandardButton.Ok)
            self.msg_win.show()
            self.close()

class AddEditTemplate(ABC, QDialog, EditAdd, metaclass=CombinedMetaclass):
    def __init__(self, Card:card = None):
        super().__init__()
        self.card = card
        self.setupUi(self)
        self.goOn.clicked.connect(self.addEditBtn)
        self.changeImage.clicked.connect(self.changeButton)

        validator = QIntValidator(0, 999999)
        self.amount.setValidator(validator)

        validator = QDoubleValidator(0, 999999.0, 2)
        self.price.setValidator(validator)

        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute('select nameManufactor from manufactor')
        manufactors = cursor.fetchall()
        cursor.execute('select nameSupplier from suppliers')
        suppliers = cursor.fetchall()
        connect.close()

        for i in manufactors:
            self.manufactor.addItem(i[0])

        for i in suppliers:
            self.supplierCombo.addItem(i[0])

        self.category.addItem('Мужская обувь')
        self.category.addItem('Женская обувь')

    @abstractclassmethod
    def addEditBtn(self):
        pass

    def changeButton(self):
        newFile, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите новое изображение",
            "",
            "Images(*.png *.jpg *.jpeg *.bmp)"
        )

        if newFile:
            os.remove(self.card.photoUrl)
            self.card.photoUrl = newFile
            filename = os.path.basename(newFile)
            self.photoURL = "C:/Users/Meow_Barsik/PycharmProjects/tovar/src/" + filename
            self.card.photoUrl = self.photoURL
            os.rename(newFile, self.card.photoUrl)
            photo = QPixmap(self.card.photoUrl)
            print(self.card.photoUrl)
            scaledPhoto = photo.scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.photo.setPixmap(scaledPhoto)


class EditDialog(AddEditTemplate, QDialog):
    def __init__(self, card: Card):
        super().__init__()
        self.card = card
        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute('select article from goods WHERE nameGood = %s AND price = %s AND descript = %s',
                       (self.card.name.text(),
                        self.card.price.text(),
                        self.card.description.text()))
        self.article = cursor.fetchone()
        cursor.execute(f'select idManufactor from goods WHERE article = "{self.article[0]}"')
        manufactorId = cursor.fetchone()
        connect.close()

        if card.category.text() == 'Мужская обувь':
            self.category.setCurrentIndex(0)
        else:
            self.category.setCurrentIndex(1)

        photo = QPixmap(self.card.photoUrl)
        scaledPhoto = photo.scaled(300, 200, Qt.AspectRatioMode.KeepAspectRatio,
                                   Qt.TransformationMode.SmoothTransformation)

        self.photo.setPixmap(scaledPhoto)
        self.name.setText(card.name.text())
        self.descript.setText(card.description.text())
        self.manufactor.setCurrentIndex(manufactorId[0])
        self.price.setText(card.price.text())
        self.unit.setText(card.unit.text())
        self.amount.setText(card.amount.text())
        self.sale.setText(card.discount.text())


    def addEditBtn(self):
        try:
            connect = databaseConnect()
            cursor = connect.cursor()
            cursor.execute('UPDATE goods SET nameGood=%s, unit=%s, price=%s, '
                           'idSupplier=%s, idManufactor=%s, '
                           'category=%s, discount=%s, amount=%s, descript=%s, photoUrl=%s WHERE article=%s',
                           (self.name.text(), self.unit.text(), self.price.text(), self.supplierCombo.currentIndex()+1,
                            self.manufactor.currentIndex()+1, self.category.currentText(), self.sale.text(),
                            self.amount.text(), self.descript.text(), self.card.photoUrl, self.article[0]))
            connect.commit()
            connect.close()
        except mysql.Error as e:
            print(e)
        self.close()

class AddDialog(AddEditTemplate, QDialog):
    def __init__(self, card: Card = None):
        super().__init__()
        self.photoURL = None

    def addEditBtn(self):

        def getUnicArticle():
            connect = databaseConnect()
            cursor = connect.cursor()
            article = None

            while True:
                characters = string.ascii_uppercase + string.digits
                characters = characters.replace('O', '').replace('0', '').replace('I', '').replace('l', '')
                article_list = random.choices(characters, k=5)
                article = ''.join(article_list)
                cursor.execute('select id from suppliers WHERE nameSupplier = %s', (article,))

                if not(cursor.fetchone()) :
                    break

            connect.close()

            return article

        if not(self.photoURL):
            self.photoURL = 'C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png'
        connect = databaseConnect()
        cursor = connect.cursor()
        artice = getUnicArticle()
        print(artice, self.name.text(), self.unit.text(), self.price.text(), self.supplier.text(),
                            self.manufactor.currentIndex(), self.category.currentText(), self.sale.text(),
                            self.amount.text(), self.descript.text(), self.photoURL)
        cursor.execute('INSERT INTO goods (article, nameGood, unit, price, idSupplier, idManufactor, category, '
                            'discount, amount, descript, photoUrl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (artice, self.name.text(), self.unit.text(), self.price.text(), self.supplierCombo.currentIndex()+1,
                            self.manufactor.currentIndex()+1, self.category.currentText(), self.sale.text(),
                            self.amount.text(), self.descript.text(), self.photoURL))

        connect.commit()
        connect.close()
        self.close()

# Абстрактный класс для реализации общих функций для всех окон
class Window(Client, ABC, metaclass=CombinedMetaclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createCards()
        self.pushButton.clicked.connect(self.authBack)

    def authBack(self):
        self.close()
        self.auth = AuthWindow()
        self.auth.show()

    #Функция получения карточек, где query по умолчанию - получение всех карточек
    def createCards(self, query = 'select '
                       'g.category, g.nameGood, g.descript, m.nameManufactor, s.nameSupplier, g.price,'
                       'g.unit, g.amount, g.photoURL, g.discount '
                       'FROM goods g '
                       'JOIN manufactor m ON g.idManufactor = m.id '
                       'JOIN suppliers s ON g.idSupplier = s.id '):
        self.cardsArr = []
        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        connect.close()
        for i in data:
            card = Card()
            card.setFixedSize(789, 240)
            card.name.setText(i[1])
            card.category.setText(i[0])
            card.description.setText(i[2])
            card.manufacturer.setText(i[3])
            card.supplier.setText(i[4])
            card.price.setText(str(i[5]))
            card.unit.setText(i[6])
            card.amount.setText(str(i[7]))

            #Если товаров на складе нет ставится особый цвет
            if i[7] == 0:
                card.amount.setStyleSheet("background-color: rgb(173,216,230);")

            if i[8]:
                card.photoUrl = i[8]
                photo = QPixmap(i[8])
            else:
                card.photoUrl = "C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png"
                photo = QPixmap("C:/Users/Meow_Barsik/PycharmProjects/tovar/src/picture.png")
            label_size = card.photo.size().width()
            scaled_photo = photo.scaled(label_size, label_size,
                                        Qt.AspectRatioMode.KeepAspectRatio,
                                        Qt.TransformationMode.SmoothTransformation)
            card.photo.setPixmap(scaled_photo)

            card.discount.setText(str(i[9]))
            if i[9] > 0:
                card.price.setStyleSheet("text-decoration: line-through; color: red")
                card.priceWithDisc.setText(str(i[5]-(i[5]*i[9]/100)))

                if i[9] >= 15:
                    card.discount.setStyleSheet("background-color: #2E8B57")

            self.cardsArr.append(card)
            card.clicked.connect(lambda checked, c=card: self.openEditDialog(c))

        self.lay = QVBoxLayout()
        for i in self.cardsArr:
            self.lay.addWidget(i)

        self.item = QWidget()
        self.item.setLayout(self.lay)

        self.scrollArea.setWidget(self.item)

    def openEditDialog(self, card):
        pass

#Абстрактный класс для реализации общих функций для персонала (менеджер, администратор)
class PersonalWindow(Window, ABC, metaclass=CombinedMetaclass):
    def __init__(self):
        super().__init__()
        self.setupLogic()
        self.fillComboBox()
        self.loadOrders()

    def updateInfo(self):
        self.loadOrders()
        self.createCards()

    def setupLogic(self):
        self.pushButton.clicked.connect(self.authBack)
        self.searchLN.textChanged.connect(self.onChangeLineEdit)
        self.sortCB.activated.connect(self.searchSortFilter)
        self.filterCB.activated.connect(self.searchSortFilter)

        # Таймер задержки чтоб не на каждое изменения символа производился отбор данных
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.searchSortFilter)

    def onChangeLineEdit(self):
        self.timer.stop()
        self.timer.start(500)

    def fillComboBox(self):
        self.sortCB.addItem("По умолчанию")
        self.sortCB.addItem("По возрастанию")
        self.sortCB.addItem("По убыванию")

        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute('select nameSupplier from suppliers')
        suppliers = cursor.fetchall()
        print(suppliers)
        self.filterCB.addItem("Все поставщики")
        for i in suppliers:
            self.filterCB.addItem(i[0])

    #общая функция для одновременной фильтрации
    def searchSortFilter(self):
        query = """select g.category, g.nameGood, g.descript, m.nameManufactor, s.nameSupplier, g.price,
               g.unit, g.amount, g.photoURL, g.discount 
               FROM goods g 
               JOIN manufactor m ON g.idManufactor = m.id 
               JOIN suppliers s ON g.idSupplier = s.id """
        whereFlag = False

        if self.searchLN.text() != '':
            whereFlag = True

            #Разбиваем строку из LineEdit для поиска и собираем в строку где слова разделены |
            searchArr = '|'.join(self.searchLN.text().split())
            query+=(f"WHERE LOWER(g.category) REGEXP '{searchArr}' "
                    f"OR LOWER(g.nameGood) REGEXP '{searchArr}'"
                    f"OR LOWER(g.descript) REGEXP '{searchArr}'"
                    f"OR LOWER(m.nameManufactor) REGEXP '{searchArr}'"
                    f"OR LOWER(s.nameSupplier) REGEXP '{searchArr}'")

        if self.filterCB.currentText() != 'Все поставщики':
            if whereFlag:
                query+=f" AND s.nameSupplier = '{self.filterCB.currentText()}'"
            else:
                query+=f"WHERE s.nameSupplier = '{self.filterCB.currentText()}'"

        if self.sortCB.currentText() == 'По возрастанию':
            query+=" ORDER BY g.price"
        elif self.sortCB.currentText() == 'По убыванию':
            query+=" ORDER BY g.price DESC"

        self.createCards(query)

    def loadOrders(self):
        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute("select * from orders")
        ordersData = cursor.fetchall()
        self.tableWidget.setRowCount(len(ordersData))
        self.tableWidget.setColumnCount(len(ordersData[0])+1)

        self.tableWidget.setHorizontalHeaderLabels(['ID ЗАКАЗА',
                                                    'ДАТА ЗАКАЗА',
                                                    'ДАТА ДОСТАВКИ',
                                                    'ID ТОЧКИ ВЫДАЧИ',
                                                    'ФИО',
                                                    'СОСТАВ',
                                                    'СТАТУС',
                                                    'КОД ВЫДАЧИ'])

        for i in range(len(ordersData)):
            cursor.execute("Select idGood, amount from order_compose where idOrder = %s ", (ordersData[i][0],))
            orderCompose = cursor.fetchall()

            composeStr = ""
            for part in orderCompose:
                composeStr += f"{part[0]}, {part[1]}; "

            self.tableWidget.setItem(i, 5, QTableWidgetItem(composeStr))

            for j in range(len(ordersData[i])):
                if j == 5:
                    arrIndex = 5
                    j+=2
                    print(str(ordersData[i][arrIndex]))
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(ordersData[i][arrIndex])))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(ordersData[i][j])))

        connect.close()
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.update()

    def openEditDialog(self, card):
        pass

class AuthClientWindow(Window, QMainWindow, metaclass=CombinedMetaclass):
    def __init__(self):
        super().__init__()

class UnAuthClientWindow(Window, QMainWindow, metaclass=CombinedMetaclass):
    def __init__(self):
        super().__init__()

class ManagerWindow(Manager, PersonalWindow, QMainWindow, metaclass=CombinedMetaclass):
    def __init__(self):
        super().__init__()

class AdminWindow(Admin, PersonalWindow, QMainWindow, metaclass=CombinedMetaclass):
    def __init__(self):
        super().__init__()
        self.addGood.clicked.connect(self.openAddDialog)
        self.tableWidget.cellClicked.connect(self.editOrDeleteOrder)
        self.addOrder.clicked.connect(self.openOrderAddDialog)

    def openOrderAddDialog(self):
        self.dialog = o.OrderAddWindow()
        self.dialog.exec()
        self.updateInfo()
    
    def editOrDeleteOrder(self):
        rowCount = self.tableWidget.currentRow()
        columnCount = self.tableWidget.columnCount()
        data = []
        for i in range(columnCount):
            data.append(self.tableWidget.item(rowCount, i).text())

        self.dialog = OrderEditDelite(data)
        self.dialog.exec()
        self.updateInfo()
    
    def openEditDialog(self, card):
        self.dialog = EditOrDeliteWindow(card)
        self.dialog.exec()
        self.updateInfo()
    def openAddDialog(self):
        self.dialog = AddDialog(card)
        self.dialog.exec()
        self.updateInfo()

class AuthWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.enterBtn.clicked.connect(self.auth)
        self.guestBtn.clicked.connect(self.unAuth)
        self.login.setText("94d5ous@gmail.com")
        self.password.setText("uzWC67")
        self.show()

    def unAuth(self):
        self.window = UnAuthClientWindow()
        self.window.role.setText("Неавторизованный пользователь")
        self.close()
        self.window.show()

    def auth(self):
        login = self.login.text()
        password = self.password.text()

        if login == "" or password == "":
            self.showMsg("Заполните все поля")
        else:
            self.userInfo = self.userGet(login, password)

        match self.userInfo[1]:
            case 1:
                self.window = AdminWindow()
                self.window.role.setText("Администратор")
            case 2:
                self.window = ManagerWindow()
                self.window.role.setText("Менеджер")
            case 3:
                self.window = AuthClientWindow()
                self.window.role.setText("Клиент")
        self.close()
        self.window.secondName.setText(self.userInfo[2])
        self.window.name.setText(self.userInfo[3])
        self.window.patronymic.setText(self.userInfo[4])
        self.window.show()


    def showMsg(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        msg.show()

    def userGet(self, login, password):
        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute(f"select * from users where login = %s", (login,))
        user = cursor.fetchone()

        if user:
            print(user)
            if password == user[6]:
                return user
            else:
                self.showMsg("Неверный пароль")
                connect.close()
                return None
        else:
            self.showMsg("Пользователя не существует")
            connect.close()
            return None



if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = AuthWindow()
    sys.exit(app.exec())