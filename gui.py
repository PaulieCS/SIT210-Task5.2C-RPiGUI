# Write your code here :-)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import RPi.GPIO as GPIO
import time

redLED = 10
yellowLED = 11
greenLED = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)

    layout = QVBoxLayout()

    button1 = QPushButton("Red")
    button2 = QPushButton("Yellow")
    button3 = QPushButton("Green")
    exitButton = QPushButton ("Exit")
    
    button1.clicked.connect(press_red_button)
    button2.clicked.connect(press_yellow_button)
    button3.clicked.connect(press_green_button)
    exitButton.clicked.connect(press_exit_button)

    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addWidget(exitButton)

    window.setLayout(layout)

    window.show()
    app.exec_()

def press_red_button():
    all_buttons_off()
    GPIO.output(redLED, GPIO.HIGH)
    
def press_yellow_button():
    all_buttons_off()
    GPIO.output(yellowLED, GPIO.HIGH)
    
def press_green_button():
    all_buttons_off()
    GPIO.output(greenLED, GPIO.HIGH)
    
def all_buttons_off():
    GPIO.output(redLED, GPIO.LOW)
    GPIO.output(yellowLED, GPIO.LOW)
    GPIO.output(greenLED, GPIO.LOW)
    
def press_exit_button():
    all_buttons_off()
    app.quit()
    
if __name__ == '__main__':
    main()
