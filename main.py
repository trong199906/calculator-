import PyQt5.QtWidgets as ptw


class MainWindow(ptw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculator')
        self.setLayout(ptw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.find_nums = []

    def keypad(self):
        contanier = ptw.QWidget()
        contanier.setLayout(ptw.QGridLayout())
        self.result_field = ptw.QLineEdit()
        btn_result = ptw.QPushButton('Enter', clicked=self.func_result)
        btn_clear = ptw.QPushButton('Clear', clicked=self.clear_calu)
        btn_9 = ptw.QPushButton('9', clicked=lambda: self.num_press('9'))
        btn_8 = ptw.QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_7 = ptw.QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_6 = ptw.QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_5 = ptw.QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_4 = ptw.QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_3 = ptw.QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_2 = ptw.QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_1 = ptw.QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_0 = ptw.QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_plus = ptw.QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_mins = ptw.QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_mult = ptw.QPushButton('*', clicked=lambda: self.func_press('*'))
        btn_divide = ptw.QPushButton('%', clicked=lambda: self.func_press('%'))
        contanier.layout().addWidget(self.result_field, 0, 0, 1, 4)
        contanier.layout().addWidget(btn_result, 1, 0, 1, 2)
        contanier.layout().addWidget(btn_clear,1, 2, 1, 2)
        contanier.layout().addWidget(btn_9,2,0)
        contanier.layout().addWidget(btn_8, 2, 1)
        contanier.layout().addWidget(btn_7, 2, 2)
        contanier.layout().addWidget(btn_plus, 2, 3)
        contanier.layout().addWidget(btn_6, 3, 0)
        contanier.layout().addWidget(btn_5,3, 1)
        contanier.layout().addWidget(btn_4,3, 2)
        contanier.layout().addWidget(btn_mins, 3,3)
        contanier.layout().addWidget(btn_3, 4,0)
        contanier.layout().addWidget(btn_2, 4,1)
        contanier.layout().addWidget(btn_1, 4,2)
        contanier.layout().addWidget(btn_mult,4,3)
        contanier.layout().addWidget(btn_0, 5,0,1,3)
        contanier.layout().addWidget(btn_divide, 5,3)
        self.layout().addWidget(contanier)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.find_nums:
            self.result_field.setText(''.join(self.find_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.find_nums.append(temp_string)
        self.find_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.find_nums))

    def func_result(self):
        fin_string = ''.join(self.find_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calu(self):
        self.result_field.clear()
        self.temp_nums = []
        self.find_nums = []


if __name__ == "__main__":
    app = ptw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
