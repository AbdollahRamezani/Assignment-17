import math
from functools import partial  # Defult Python
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def num(x):
    main_window.textbox.setText(main_window.textbox.text()+x)
def point(x):
    if "." not in main_window.textbox.text():
         main_window.textbox.setText(main_window.textbox.text()+x)
def clear():
    main_window.textbox.setText("") 

def first_textbox(op):
    global operator
    operator = op

    global a
    a = main_window.textbox.text()
    main_window.textbox.setText("")

def maath(op):
  if op == "sin":
    result = math.sin(float(main_window.textbox.text()))
  elif op == "cos":
    result = math.cos(float(main_window.textbox.text()))  
  elif op == "tan":
    result = math.tan(float(main_window.textbox.text()))    
  elif op == "cot":
    result = 1/math.tan(float(main_window.textbox.text())) 
  elif op == "sqrt":
    result = math.sqrt(float(main_window.textbox.text())) 
  elif op == "log":
    result = math.log(float(main_window.textbox.text()))   
    
  main_window.textbox.setText(str(result))

def result():
    b = main_window.textbox.text()
    if operator == "+":
        c = float(a) + float(b)
    elif operator == "-" :
        c = float(a) - float(b) 
    elif operator == "*" :
        c = float(a) * float(b) 
    elif operator == "/" :
        c = float(a) / float(b)           
    main_window.textbox.setText(str(c))

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

main_window.btn0.clicked.connect(partial(num, "0"))
main_window.btn1.clicked.connect(partial(num, "1"))
main_window.btn2.clicked.connect(partial(num, "2"))
main_window.btn3.clicked.connect(partial(num, "3"))
main_window.btn4.clicked.connect(partial(num, "4"))
main_window.btn5.clicked.connect(partial(num, "5"))
main_window.btn6.clicked.connect(partial(num, "6"))
main_window.btn7.clicked.connect(partial(num, "7"))
main_window.btn8.clicked.connect(partial(num, "8"))
main_window.btn9.clicked.connect(partial(num, "9"))

main_window.sum_btn.clicked.connect(partial(first_textbox, "+"))
main_window.sub_btn.clicked.connect(partial(first_textbox, "-"))
main_window.mul_btn.clicked.connect(partial(first_textbox, "*"))
main_window.div_btn.clicked.connect(partial(first_textbox, "/"))
main_window.sin_btn.clicked.connect(partial(maath, "sin"))
main_window.cos_btn.clicked.connect(partial(maath, "cos"))
main_window.tan_btn.clicked.connect(partial(maath, "tan"))
main_window.cot_btn.clicked.connect(partial(maath, "cot"))
main_window.sqrt_btn.clicked.connect(partial(maath, "sqrt"))
main_window.log_btn.clicked.connect(partial(maath, "log"))

main_window.point_btn.clicked.connect(partial(point, "."))
main_window.c_btn.clicked.connect(clear)

main_window.equal_btn.clicked.connect(result)

app.exec()