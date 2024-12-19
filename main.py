from PyQt5.QtWidgets import(QApplication,QWidget,
                            QLabel,QPushButton,
                            QHBoxLayout,QVBoxLayout,QGroupBox)
from PyQt5.QtCore import Qt
app = QApplication([])
window = QWidget()
window.setWindowTitle("Калькулятор")
window.resize(300,500)
window.setStyleSheet("""QWidet {
font-family: "Times New Roman", Times, serif;
font-size: 20px;
background-color: bisque;
 color: #ffc083
 }
                    QPushButton {
    background-color:#ffc0b2;
    border: 3px soild white;
    padding: 5px 40px 5px 40px;
    border-radius: 20px;
                    }
                    QPushButton:hover{
    background-color:white;
    border-radius: 10px;
    }
QGroupBox{background-color:#ffdbc2;
border-radius: 20px;}    
    
    
     """)
btn_0 = QPushButton('0')
#btn_0.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_1 = QPushButton('1')
#btn_1.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_2 = QPushButton('2')
#btn_2.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_3 = QPushButton('3')
#btn_3.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_4 = QPushButton('4')
#btn_4.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_5 = QPushButton('5')
#btn_5.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_6 = QPushButton('6')
#btn_6.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_7 = QPushButton('7')
#btn_7.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_8 = QPushButton('8')
#btn_8.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_9 = QPushButton('9')
#btn_9.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")

btn_eq = QPushButton("=")
#btn_eq.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_clear = QPushButton("C")
#btn_clear.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_back = QPushButton("<-")
#btn_back.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_point = QPushButton(".")
#btn_point.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")

btn_pl = QPushButton("+")
#btn_pl.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_min = QPushButton("-")
#btn_min.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_mul = QPushButton("*")
#btn_mul.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_div = QPushButton("/")
#btn_div.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
btn_korn = QPushButton("√")
#btn_korn.setStyleSheet("background-color: #ffc083;border: 2px soild #b85e3b;padding: 5px 35px 5px 35px;border-radius: 5px;")
result = QLabel("0")
result.setStyleSheet("font-size: 40px;font-weight: blod;")
line1 = QHBoxLayout()
line1.addWidget(btn_eq,alignment=Qt.AlignCenter)
line1.addWidget(btn_back,alignment=Qt.AlignCenter)
line1.addWidget(btn_clear,alignment=Qt.AlignCenter)

line2 = QHBoxLayout()
line2.addWidget(btn_1,alignment=Qt.AlignCenter)
line2.addWidget(btn_2,alignment=Qt.AlignCenter)
line2.addWidget(btn_3,alignment=Qt.AlignCenter)

line3 = QHBoxLayout()
line3.addWidget(btn_4,alignment=Qt.AlignCenter)
line3.addWidget(btn_5,alignment=Qt.AlignCenter)
line3.addWidget(btn_6,alignment=Qt.AlignCenter)

line4 = QHBoxLayout()
line4.addWidget(btn_7,alignment=Qt.AlignCenter)
line4.addWidget(btn_8,alignment=Qt.AlignCenter)
line4.addWidget(btn_9,alignment=Qt.AlignCenter)

line5 = QHBoxLayout()
line5.addWidget(btn_pl,alignment=Qt.AlignCenter)
line5.addWidget(btn_min,alignment=Qt.AlignCenter)
line5.addWidget(btn_mul,alignment=Qt.AlignCenter)

line6 = QHBoxLayout()
line6.addWidget(btn_div,alignment=Qt.AlignCenter)
line6.addWidget(btn_0,alignment=Qt.AlignCenter)
line6.addWidget(btn_korn,alignment=Qt.AlignCenter)

box1 = QGroupBox()
box_line = QHBoxLayout()
box_line.addWidget(result,alignment=Qt.AlignRight)
box1.setLayout(box_line)

box2 = QGroupBox()
box_line2 = QVBoxLayout()
box_line2.addLayout(line1)
box_line2.addLayout(line5)
box_line2.addLayout(line4)
box_line2.addLayout(line3)
box_line2.addLayout(line2)
box_line2.addLayout(line6)
box2.setLayout(box_line2)

main_line = QVBoxLayout()
main_line.addWidget(box1)
main_line.stretch(2)
main_line.addWidget(box2)

def add_symbol():
     button = app.sender()
     text = result.text()
     if text[len(text)-1] in "+-/*√" and button.text() in "+-/*√":
          return
     if text == "0":
          text =""
     result.setText(text+button.text())
btn_0.clicked.connect(add_symbol)
btn_1.clicked.connect(add_symbol)
btn_2.clicked.connect(add_symbol)
btn_3.clicked.connect(add_symbol)
btn_4.clicked.connect(add_symbol)
btn_5.clicked.connect(add_symbol)
btn_6.clicked.connect(add_symbol)
btn_7.clicked.connect(add_symbol)
btn_8.clicked.connect(add_symbol)
btn_9.clicked.connect(add_symbol)
btn_point.clicked.connect(add_symbol)
btn_pl.clicked.connect(add_symbol)
btn_min.clicked.connect(add_symbol)
btn_mul.clicked.connect(add_symbol)
btn_div.clicked.connect(add_symbol)
btn_korn.clicked.connect(add_symbol)

def clear():
     result.setText("0")
btn_clear.clicked.connect(clear)

def back():
     text = result.text()
     text = text[:-1]
     if text =="":
          text="0"
     result.setText(text)
btn_back.clicked.connect(back)




def parseSting(string):
     operatoins= "/*-+√"
     element = ""
     result= []
     for symbol in string:
          if operatoins.find(symbol) !=-1:
               result.append(element)
               result.append(symbol)
               element =""
          else:
               element+=symbol
     result.append(element)
     return result

def calculate(string):
     formula = parseSting(string)
     if formula[0] == "":
          formula[0]="0"
     operatoins = ["/*","-+","√"]
     for cur_operation in operatoins:
          i=0
          while i< len(formula):
               if cur_operation.find(formula[i]) !=-1:
                    operatoin = formula[i]
                    first_number = float(formula[i-1])
                    second_number = float(formula[i+1])
                    if operatoin =="+":
                         result= first_number+second_number
                    if operatoin =="-":
                         result= first_number-second_number
                    if operatoin =="*":
                         result= first_number*second_number
                    if operatoin =="/":
                         result= first_number/second_number
                    if operatoin =="√":
                         result= first_number*second_number**(1/2)
                    del formula[i+1]
                    formula[i]=str(result)
                    del formula[i-1]
                    i =0
               i +=1
     return formula[0]

def equal():
     formula = result.text()
     number = calculate(formula)
     result.setText(str(number))
btn_eq.clicked.connect(equal)
window.setLayout(main_line)
window.show()
app.exec_()