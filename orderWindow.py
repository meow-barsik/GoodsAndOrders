from datetime import date
import mysql

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QLineEdit, QDialog

from main import databaseConnect
from uipy.orderAdd import Ui_Dialog as orderAdd
from uipy.orderEdit import Ui_Dialog as orderEdit

class OrderEditWindow(QDialog, orderEdit):
    def __init__(self, orderData = None):
        super().__init__()
        self.setupUi(self)
        self.articulEditList = []
        self.amountEditList = []
        self.idOrder = orderData[0]
        self.articles = []

        dateList = orderData[1].split('-')
        self.dateOrder.setDate(QDate(int(dateList[0]), int(dateList[1]), int(dateList[2])))
        dateList = orderData[2].split('-')
        self.dateGive.setDate(QDate(int(dateList[0]), int(dateList[1]), int(dateList[2])))
        print(dateList[0], dateList[1], dateList[2])
        orderCompose = orderData[5].split(';')
        orderCompose = [item.strip() for item in orderCompose if item.strip()]
        for i in range(len(orderCompose)):
            orderPart = orderCompose[i].split(', ')
            self.articles.append(orderPart[0])

            LineEdit = QLineEdit()
            LineEdit.setText(orderPart[0])
            self.articulEditList.append(LineEdit)
            self.articulLay.addWidget(self.articulEditList[i])

            LineEdit = QLineEdit()
            LineEdit.setText(orderPart[1])
            self.amountEditList.append(LineEdit)
            self.amountLay.addWidget(self.amountEditList[i])

        self.statusCombo.addItems(['Доставлено', 'Недоставлено'])
        self.statusCombo.setCurrentText(orderData[6])

        connect = databaseConnect()
        cursor = connect.cursor()
        cursor.execute("SELECT address from pickup_points WHERE id=%s", (self.idOrder,))
        addressInfo = cursor.fetchone()
        connect.close()
        self.address.setText(addressInfo[0])

        self.editBtn.clicked.connect(self.editConfirm)

    def editConfirm(self):
        connect = databaseConnect()
        cursor = connect.cursor()
        try:
            for i in range(len(self.articulEditList)):
                cursor.execute("UPDATE order_compose SET idGood = %s, amount = %s WHERE idOrder = %s AND idGood = %s",
                               (self.articulEditList[i].text(), self.amountEditList[i].text(), self.idOrder, self.articles[i]))
            cursor.execute("UPDATE orders SET dateOrder = %s, dateDelivery = %s, orderStatus = %s WHERE id = %s",
                           (f'{self.dateOrder.date().year()}-{self.dateOrder.date().month()}-{self.dateOrder.date().day()}',
                            f'{self.dateGive.date().year()}-{self.dateGive.date().month()}-{self.dateGive.date().day()}',
                            self.statusCombo.currentText(),
                            self.idOrder))

            cursor.execute("UPDATE pickup_points SET address = %s WHERE id = (SELECT idPoint FROM orders WHERE id = %s)",
                           (self.address.text(), self.idOrder))

            connect.commit()
            connect.close()
        except mysql.connector.Error as error:
            print(error)
            pass

        self.close()

class OrderAddWindow(QDialog, orderAdd):
    def __init__(self):
        super().__init__()

        self.articles = []
        self.amount = []

        self.setupUi(self)
        self.statusCombo.addItems(['Доставлено', 'Недоставлено'])
        self.addGoodOrder.clicked.connect(self.addGood)
        self.editBtn.clicked.connect(self.editConfirm)

    def addGood(self):
        lineEdit = QLineEdit()
        self.articles.append(lineEdit)
        self.articulLay.addWidget(self.articles[len(self.articles)-1])

        lineEdit = QLineEdit()
        self.amount.append(lineEdit)
        self.amountLay.addWidget(self.amount[len(self.articles)-1])

    def editConfirm(self):
        connect = databaseConnect()
        cursor = connect.cursor()

        cursor.execute("INSERT INTO pickup_points (address) VALUES (%s)",
                       (self.address.text(),))
        connect.commit()
        cursor.execute("SELECT id from pickup_points WHERE address=%s",
                       (self.address.text(),))
        idPoint = cursor.fetchone()

        cursor.execute("INSERT INTO orders (dateOrder, dateDelivery, idPoint, orderStatus) VALUES (%s, %s, %s, %s);",
                       (f'{self.dateOrder.date().year()}-{self.dateOrder.date().month()}-{self.dateOrder.date().day()}',
                        f'{self.dateGive.date().year()}-{self.dateGive.date().month()}-{self.dateGive.date().day()}',
                        idPoint[0],
                        self.statusCombo.currentText()))
        connect.commit()
        cursor.execute("SELECT id from orders WHERE dateOrder=%s AND dateDelivery=%s AND idPoint=%s AND orderStatus=%s;",
                       (f'{self.dateOrder.date().year()}-{self.dateOrder.date().month()}-{self.dateOrder.date().day()}',
                        f'{self.dateGive.date().year()}-{self.dateGive.date().month()}-{self.dateGive.date().day()}',
                        idPoint[0],
                        self.statusCombo.currentText()))
        idOrder = cursor.fetchone()

        for i in range(len(self.articles)):
            cursor.execute('INSERT INTO order_compose (idOrder, idGood, amount) VALUES (%s, %s, %s)',
                           (idOrder[0], self.articles[i].text(), self.amount[i].text()))

        connect.commit()
        connect.close()
        self.close()

