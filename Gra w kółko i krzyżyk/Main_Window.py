from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pyqtgraph as pg
import os
from numpy import *

class App(QMainWindow):  # główne okno
    def __init__(self):
        super().__init__()
        # Definiuje geometrię okna
        self.glowny_dock = Layout()
        self.setCentralWidget(self.glowny_dock)

        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Kółko i Krzyżyk')
        #################################################
        exitProgram = QAction('Exit', self)
        exitProgram.triggered.connect(self.exit_program)
        restartGame = QAction('Restart', self)
        restartGame.triggered.connect(self.restart_Game)
        self.singleGame = QAction('Single Game', self, checkable=True)
        self.singleGame.triggered.connect(self.single_Game)

        # Tworzy obiekt klasy typu menuBar

        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('Menu')  # Dodaje menu File
        fileMenu.addAction(exitProgram)
        fileMenu.addAction(restartGame)
        fileMenu.addAction(self.singleGame)




        self.show()

    def restart_Game(self):
        self.glowny_dock.button1.setText("")
        self.glowny_dock.button2.setText("")
        self.glowny_dock.button3.setText("")
        self.glowny_dock.button4.setText("")
        self.glowny_dock.button5.setText("")
        self.glowny_dock.button6.setText("")
        self.glowny_dock.button7.setText("")
        self.glowny_dock.button8.setText("")
        self.glowny_dock.button9.setText("")
        self.glowny_dock.napis.setText("Ruch X")
        self.glowny_dock.lista.clear()
        self.glowny_dock.lista.append(self.glowny_dock.button1)
        self.glowny_dock.lista.append(self.glowny_dock.button2)
        self.glowny_dock.lista.append(self.glowny_dock.button3)
        self.glowny_dock.lista.append(self.glowny_dock.button4)
        self.glowny_dock.lista.append(self.glowny_dock.button5)
        self.glowny_dock.lista.append(self.glowny_dock.button6)
        self.glowny_dock.lista.append(self.glowny_dock.button7)
        self.glowny_dock.lista.append(self.glowny_dock.button8)
        self.glowny_dock.lista.append(self.glowny_dock.button9)
        self.glowny_dock.single_Game_turn = True

    def single_Game(self):
        a = self.singleGame.isChecked()
        if a == True:
            self.glowny_dock.single_Game_true = True
        else:
            self.glowny_dock.single_Game_true = False


    def exit_program(self):
        print('Kończy działanie aplikacji')
        os._exit(0)


class Layout(QWidget):

    def __init__(self):
        super().__init__()
        self.graphWidget = pg.PlotWidget()

        self.layout1 = QGridLayout(self)
        self.layout2 = QGridLayout(self)

        self.rozmiar = QSize(60,60)

        self.button1 = QPushButton("", self)
        self.button2 = QPushButton("", self)
        self.button3 = QPushButton("", self)
        self.button4 = QPushButton('', self)
        self.button5 = QPushButton('', self)
        self.button6 = QPushButton('', self)
        self.button7 = QPushButton('', self)
        self.button8 = QPushButton('', self)
        self.button9 = QPushButton('', self)

        self.button1.setMinimumSize(40, 40)
        self.button1.setMaximumSize(40, 40)
        self.button2.setMinimumSize(40, 40)
        self.button2.setMaximumSize(40, 40)
        self.button3.setMinimumSize(40, 40)
        self.button3.setMaximumSize(40, 40)
        self.button4.setMinimumSize(40, 40)
        self.button4.setMaximumSize(40, 40)
        self.button5.setMinimumSize(40, 40)
        self.button5.setMaximumSize(40, 40)
        self.button6.setMinimumSize(40, 40)
        self.button6.setMaximumSize(40, 40)
        self.button7.setMinimumSize(40, 40)
        self.button7.setMaximumSize(40, 40)
        self.button8.setMinimumSize(40, 40)
        self.button8.setMaximumSize(40, 40)
        self.button9.setMinimumSize(40, 40)
        self.button9.setMaximumSize(40, 40)

        self.layout1.addWidget(self.button1, 0,0)
        self.layout1.addWidget(self.button2, 0,1)
        self.layout1.addWidget(self.button3, 0,2)

        self.layout1.addWidget(self.button4, 1,0)
        self.layout1.addWidget(self.button5, 1,1)
        self.layout1.addWidget(self.button6, 1,2)

        self.layout1.addWidget(self.button7, 2,0)
        self.layout1.addWidget(self.button8, 2,1)
        self.layout1.addWidget(self.button9, 2,2)


        self.napis = QLabel("Ruch X", self)
        self.layout2.addWidget(self.napis, 0,0)


        self.group1 = QGroupBox(self)
        self.group1.setLayout(self.layout1)

        self.group2 = QGroupBox(self)
        self.group2.setLayout(self.layout2)

        self.layout = QGridLayout(self)
        self.layout.addWidget(self.group1, 0, 0)
        self.layout.addWidget(self.group2, 1, 0)

        self.setLayout(self.layout)
        self.button1.clicked.connect(self.button_1)
        self.button2.clicked.connect(self.button_2)
        self.button3.clicked.connect(self.button_3)
        self.button4.clicked.connect(self.button_4)
        self.button5.clicked.connect(self.button_5)
        self.button6.clicked.connect(self.button_6)
        self.button7.clicked.connect(self.button_7)
        self.button8.clicked.connect(self.button_8)
        self.button9.clicked.connect(self.button_9)

        self.lista = [self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9]
        self.single_Game_true = False
        self.single_Game_turn = True


        self.show()



    def DialogBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Nie możesz tu nacisnąć")
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def Win_X(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Wygrał X")
        msg.setWindowTitle("Win")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def Brak_Win(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Remis")
        msg.setWindowTitle("Remis")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def Win_O(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Wygrało o")
        msg.setWindowTitle("Win")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def button_1(self):
        a = self.button1.text()
        if a=="x":
            print ("Nie możesz tu nacisnąć")
            self.DialogBox()
        if  a=="o":
            print ("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            self.Dwoch_Graczy(1, self.button1)

    def button_2(self):
        a = self.button2.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(2, self.button2)

    def button_3(self):
        a = self.button3.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(3, self.button3)

    def button_4(self):
        a = self.button4.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(4, self.button4)

    def button_5(self):
        a = self.button5.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(5, self.button5)

    def button_6(self):
        a = self.button6.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(6, self.button6)

    def button_7(self):
        a = self.button7.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(7, self.button7)

    def button_8(self):
        a = self.button8.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(8, self.button8)

    def button_9(self):
        a = self.button9.text()
        if a == "x":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a == "o":
            print("Nie możesz tu nacisnąć")
            self.DialogBox()
        if a=="":
            print ("klikaj dalej")
            self.Dwoch_Graczy(9, self.button9)


    def single_Game(self):
        w = random.choice(self.lista)
        w.click()



    def Dwoch_Graczy(self,y, guzik):
        c = self.napis.text()
        if c == "Ruch X" :
            b = "x"
            if y ==1:
                self.button1.setText(b)
            if y ==2:
                self.button2.setText(b)
            if y ==3:
                self.button3.setText(b)
            if y ==4:
                self.button4.setText(b)
            if y ==5:
                self.button5.setText(b)
            if y ==6:
                self.button6.setText(b)
            if y ==7:
                self.button7.setText(b)
            if y ==8:
                self.button8.setText(b)
            if y ==9:
                self.button9.setText(b)

            self.napis.setText("Ruch o")

        if c == "Ruch o" :
            b = "o"
            if y ==1:
                self.button1.setText(b)
            if y ==2:
                self.button2.setText(b)
            if y ==3:
                self.button3.setText(b)
            if y ==4:
                self.button4.setText(b)
            if y ==5:
                self.button5.setText(b)
            if y ==6:
                self.button6.setText(b)
            if y ==7:
                self.button7.setText(b)
            if y ==8:
                self.button8.setText(b)
            if y ==9:
                self.button9.setText(b)

            self.napis.setText("Ruch X")

        a = self.Wygrana()
        if not a:
            b = self.Remis()

        self.lista.remove(guzik)

        if self.single_Game_true and not a and not b and self.single_Game_turn:
            self.single_Game_turn = False
            self.single_Game()
        else:
            self.single_Game_turn = True

    def Wygrana(self):
        I = self.button1.text()
        II = self.button2.text()
        III = self.button3.text()
        IV = self.button4.text()
        V = self.button5.text()
        VI = self.button6.text()
        VII = self.button7.text()
        VIII = self.button8.text()
        IX = self.button9.text()

        q = "xxx"
        if I+II+III ==q or IV+V+VI == q or VII+VIII+IX == q or I+IV+VII == q or II+V+VIII == q or III+VI+IX == q or III+V+VII == q or I+V+IX == q :
            self.napis.setText("Wygrał X")
            self.Win_X()
            return True

        q = "ooo"
        if I+II+III ==q or IV+V+VI == q or VII+VIII+IX == q or I+IV+VII == q or II+V+VIII == q or III+VI+IX == q or III+V+VII == q or I+V+IX == q :
            self.napis.setText("Wygrało O")
            self.Win_O()
            return True

    def Remis(self):

        I = self.button1.text()
        II = self.button2.text()
        III = self.button3.text()
        IV = self.button4.text()
        V = self.button5.text()
        VI = self.button6.text()
        VII = self.button7.text()
        VIII = self.button8.text()
        IX = self.button9.text()
        if I !="" and II !="" and III !="" and IV !="" and V !="" and VI !="" and VII !="" and VIII !="" and IX !="" :
            self.napis.setText("Remis")
            self.Brak_Win()
            return True