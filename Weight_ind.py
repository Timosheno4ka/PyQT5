import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton


class Weight(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(300, 300, 170, 425)
        self.setWindowTitle("Индекс массы тела")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(225, 95)
        self.move(0, 0)

        self.lbl = QLabel('Введите ваш вес, а затем рост', self)
        self.lbl.move(10, 20)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 100)
        # self.num_1.clicked.connect()

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)
        # self.num_1.clicked.connect()

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 210)
        # self.num_1.clicked.connect()

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 210)

        self.contin = QPushButton('Далее', self)
        self.contin.resize(105, 50)
        self.contin.move(60, 265)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(5, 265)
        # self.num_1.clicked.connect()

        self.ravn = QPushButton('Узнать индекс массы тела', self)
        self.ravn.resize(160, 50)
        self.ravn.move(5, 320)

        self.c = QPushButton('Очистить', self)
        self.c.resize(160, 50)
        self.c.move(5, 375)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.contin.clicked.connect(self.contin_1)
        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clear)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def contin_1(self):
        self.operation = 'Далее'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ravno(self):
        self.operand_2 = float(self.label.text())
        if self.operation == 'Далее':
            self.result = (self.operand_1 / (self.operand_2**2))*10000
        self.label.setText(str(self.result))


    def clear(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Weight()
    ex.show()
    sys.exit(app.exec())
