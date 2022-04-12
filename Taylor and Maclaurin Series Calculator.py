# importing libraries
import sys
import math
import sympy as sy
import numpy as np
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from sympy.functions import sin,cos
import matplotlib.pyplot as plt


plt.style.use('seaborn-poster')


class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Taylor and Maclaurin Series approximation ")
  
        # width of window
        self.w_width = 1000
  
        # height of window
        self.w_height = 800
  
        # setting geometry
        self.setGeometry(100, 100, self.w_width, self.w_height)
        
        self.setStyleSheet(
                            "background: #161219;" 
                          ) # setiting background color. In the kovichki you can write the css code
  
        grid = QGridLayout() # initializing grid layout
        self.setLayout(grid) # applying grid in window object
        # calling method
        
        self.UiComponents()
  
        # showing all the widgets
        self.show()
        
    # method for components
    def UiComponents(self):
  
        # creating head label
        head = QLabel("Taylor and Maclaurin Series Calculator", self)
        head.setStyleSheet(
                        "color: white;" +
                        "font-size: 45px;" 
            
        
        )
  
        head.setWordWrap(True)
  
        # setting geometry to the head
        head.setGeometry(190, 25, 550, 100)
        
        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)
  
        global mac_info
        global f
            
        self.n = QLineEdit(self)
        self.n.setStyleSheet(
                        "background: white;"
        )
        self.n.move(650, 150)
        self.n.resize(200, 32)
        
        self.x = QLineEdit(self)
        self.x.setStyleSheet(
                        "background: white;"
        )

        self.x.move(400, 150)
        self.x.resize(200, 32)
        
        self.func = QLineEdit(self)
        self.func.setStyleSheet(
                            "background: white;"
        )

        self.func.move(150, 150)
        self.func.resize(200, 32)
  
        mac_info = QLabel(self)
        # setting geometry
        mac_info.setGeometry(40, 380, 900, 350)
  
        # setting alignment
        mac_info.setAlignment(Qt.AlignCenter)
        mac_info.setStyleSheet(
                    "color: white;" +
                    "font-size: 25px;"
            
        )
        
        # creating a label
        n = QLabel(" n ", self)
  
        # setting geometry
        n.setGeometry(610, 145, 30, 35)
  
        # setting alignment
        n.setAlignment(Qt.AlignCenter)
        n.setStyleSheet(
                    "color: white;" +
                    "font-size: 25px;"
            
        )
  
  
        # creating a label
        x = QLabel(" c ", self)
        
        x.setStyleSheet(
                    "color: white;" +
                    "font-size: 25px;"

        )
  
        # setting geometry
        x.setGeometry(370, 145, 20, 35)
  
        # setting alignment
        x.setAlignment(Qt.AlignCenter)
  
        # creating a label
        func = QLabel("f(x)", self)
        func.setStyleSheet(
                    "color: white;" +
                    "font-size: 25px;"
            
        )
  
        # setting geometry
        func.setGeometry(60, 145, 90, 35)
  
        # setting alignment
        func.setAlignment(Qt.AlignCenter)
  
       
  
        # creating a button to calculate taylor polynomial
        tay_calc_button = QPushButton("Taylor Polynomial", self)
        tay_calc_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        tay_calc_button.setStyleSheet(
                                "*{border: 5px solid '#BC006C';" +
                                "border-radius: 45px;" +
                                "color: 'white';" +
                                "font-size: 20px;}" +
                                "*:hover{background: '#BC006C';}"           
        ) # setting border style
  
        # setting geometry to the push button
        tay_calc_button.setGeometry(50, 300, 200, 40)
  
        # adding action to the button
        tay_calc_button.clicked.connect(self.tay_calculate)
        
        # creating a button to calculate maclaurin polynomial
        mac_calc_button = QPushButton("Maclaurin Polynomial", self)
        mac_calc_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        mac_calc_button.setStyleSheet( 
                                "*{border: 5px solid '#BC006C';" +
                                "border-radius: 45px;" +
                                "color: 'white';" +
                                "font-size: 20px;}" +
                                "*:hover{background: '#BC006C';}"           
        ) # setting border style
  
        # setting geometry to the push button
        mac_calc_button.setGeometry(275, 300, 200, 40)
  
        # adding action to the button
        mac_calc_button.clicked.connect(self.mac_calculate)
        
        # creating a button to calculate maclaurin polynomial
        qr = QPushButton("More information", self)
        qr.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        qr.setStyleSheet(
                        "*{border: 5px solid '#BC006C';" +
                        "border-radius: 45px;" +
                        "color: 'white';" +
                        "font-size: 20px;}" +
                        "*:hover{background: '#BC006C';}"            
        ) # setting border style
  
        # setting geometry to the push button
        qr.setGeometry(500, 300, 200, 40)
  
        # adding action to the button
        qr.clicked.connect(self.qr_window)
        
        exit_but = QPushButton("Exit", self)
        exit_but.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        exit_but.setStyleSheet(
            "*{border: 5px solid '#BC006C';" +
            "border-radius: 45px;" +
            "color: 'white';" +
            "font-size: 20px;}" +
            "*:hover{background: '#BC006C';}"          
        ) # setting border style
  
        # setting geometry to the push button
        exit_but.setGeometry(725, 300, 200, 40)
  
        # adding action to the button
        exit_but.clicked.connect(self.close_window)
  
        # creating a label to show result
        self.result = QLabel(self)
  
        # setting properties to result label
        self.result.setAlignment(Qt.AlignCenter)
  
        # setting geometry
        self.result.setGeometry(90, 210, 800, 60)
  
        # making it multi line
        self.result.setWordWrap(True)
  
        # setting stylesheet
        # adding border and background
        self.result.setStyleSheet("QLabel"
                                  "{"
                                  "border : 3px solid black;"
                                  "background : white;"
                                  "}")
  
        # setting font
        self.result.setFont(QFont('Arial', 11))
        
        
    
    # creating function for calculating the taylor series
    def tay_calculate(self):
        
        
        pixmap = QPixmap('tay_info.jpg')
        mac_info.setPixmap(pixmap)
        
        plt.style.use("ggplot")

        # Define the variable and the function to approximate
        x = sy.Symbol('x')
        f = sin(x)

        # Factorial function
        def factorial(n):
            if n <= 0:
                return 1
            else:
                return n*factorial(n-1)
        c = int(self.x.text())
        n = int(self.n.text())

        # Taylor approximation at x0 of the function 'function'
        def taylor(function,c,n):
            i = 0
            p = 0
            while i <= n:
                p = p + (function.diff(x,i).subs(x,c))/(factorial(i))*(x-c)**i
                i += 1
            return p
        tay_calc = taylor(sin(x), c, n)
        self.result.setText(str(tay_calc))
        print(tay_calc)

        # Plot results
        def plot():
            x_lims = [-5,5]
            x1 = np.linspace(x_lims[0],x_lims[1],800)
            y1 = []
            # Approximate up until 10 starting from 1 and using steps of 2
            for j in range(1,10,2):
                func = taylor(f,0,j)
                print('Taylor expansion at n='+str(j),func)
                for k in x1:
                    y1.append(func.subs(x,k))
                plt.plot(x1,y1,label='order '+str(j))
                y1 = []
            # Plot the function to approximate (sine, in this case)
            plt.plot(x1,np.sin(x1),label='function')
            plt.xlim(x_lims)
            plt.ylim([-5,5])
            plt.xlabel('x')
            plt.ylabel('y')
            plt.legend()
            plt.grid(True)
            plt.title('Taylor series approximation')
            plt.show()

        plot()

    # creating function to close the window
    def close_window(self):
        self.close()
        
    # creating function to calculate maclaurin series    
    def mac_calculate(self):
        pixmap = QPixmap('mac_info.jpg')
        mac_info.setPixmap(pixmap)
        
        def myexp(x):
                e=0
                for i in range(0,100): #Sum the first 100 terms of the series
                    e=e+(x**i)/math.factorial(i)
                return e
        print(myexp(3))
        
        def fact(n):
            if n==0:
                return 1
            else:
                f=1
                for i in range(1, n+1):
                    f=f*1
                return f
        
        x = int(self.n.text())
        n = int(self.x.text())
        
        def calc():
            sum = 0
            sign = 1
            for i in range(n):
                sum = sign*(x**(2*i))/fact(2*i)
                sign = int((-1)*sign)
            return sum 
        m = calc()
        print(m)
        self.result.setText(str(m))
  
    # creating function to show the qr code for more information abot the series
    def qr_window(self):
        
        pixmap = QPixmap('mac_tay_info.png')
        mac_info.setPixmap(pixmap)
        
        
          
        

# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())



