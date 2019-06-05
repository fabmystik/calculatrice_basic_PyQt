# -*- coding: utf-8 -*-

# ********************************************************
#
# Created by: Fabrice YARAKOU (fabmystik)
#
# Email: yarakoufabrice1@gmail.com
#
# ********************************************************

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

# fonction pour générer l'interface utilisateur avec PyQt5
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 277)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.calc = QtWidgets.QPushButton(self.centralWidget)
        self.calc.setGeometry(QtCore.QRect(190, 160, 151, 27))
        self.calc.setObjectName("calc")
        self.a = QtWidgets.QLineEdit(self.centralWidget)
        self.a.setGeometry(QtCore.QRect(40, 30, 91, 51))
        self.a.setObjectName("a")
        self.b = QtWidgets.QLineEdit(self.centralWidget)
        self.b.setGeometry(QtCore.QRect(280, 30, 91, 51))
        self.b.setObjectName("b")
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 40, 111, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(390, 40, 21, 41))
        self.label.setObjectName("label")
        self.resultat = QtWidgets.QLabel(self.centralWidget)
        self.resultat.setGeometry(QtCore.QRect(430, 40, 121, 41))
        self.resultat.setText("")
        self.resultat.setObjectName("resultat")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 567, 24))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

# connection du boutton calculé à la fonction calculer()
        self.calc.clicked.connect(self.calculer)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# fonction pour la modification du nom et du contenu de certains widget 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Basic calculator by fabmystik"))
        self.calc.setText(_translate("MainWindow", "Calculé"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Sélectionner"))
        self.comboBox.setItemText(1, _translate("MainWindow", "+"))
        self.comboBox.setItemText(2, _translate("MainWindow", "-"))
        self.comboBox.setItemText(3, _translate("MainWindow", "*"))
        self.comboBox.setItemText(4, _translate("MainWindow", "/"))
        self.label.setText(_translate("MainWindow", "="))

# calculer() est la fonction qui permet de faire les calcules
    def calculer(self, MainWindow):
        a = int(self.a.text())
        b = int(self.b.text())
        resultat = str(a+b)

        if str(self.comboBox.currentText())=="+":
           resultat = str(a+b)
           print(self.resultat.setText(resultat))

        if str(self.comboBox.currentText())=="-":
           resultat = str(a-b)
           print(self.resultat.setText(resultat))

        if str(self.comboBox.currentText())=="*":
           resultat = str(a*b)
           print(self.resultat.setText(resultat))

        if str(self.comboBox.currentText())=="/":
           resultat = str(a/b)
           print(self.resultat.setText(resultat))

# execution du code
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

