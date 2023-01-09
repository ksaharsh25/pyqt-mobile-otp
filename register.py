# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QRegExp, QRegularExpression,pyqtSlot
import mysql.connector as mc
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLineEdit,QPushButton,QDialog,QMessageBox
from PyQt5.QtGui import QValidator,QRegExpValidator

class Ui_Form1(object):
    def __init__(self):
        super(Ui_Form1, self).__init__() 
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 540)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setGeometry(QtCore.QRect(-10, -30, 751, 571))
        self.centralwidget.setObjectName("centralwidget")
        self.bgwidget = QtWidgets.QWidget(self.centralwidget)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 771, 680))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(self.bgwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 291, 71))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.loginbutton = QtWidgets.QPushButton(self.bgwidget)
        self.loginbutton.setGeometry(QtCore.QRect(220, 510, 341, 51))
        self.loginbutton.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.loginbutton.setObjectName("loginbutton")
        self.email = QtWidgets.QLineEdit(self.bgwidget)
        self.email.setGeometry(QtCore.QRect(60, 290, 671, 41))
        self.email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.email.setObjectName("email")
        self.label_3 = QtWidgets.QLabel(self.bgwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.error = QtWidgets.QLabel(self.bgwidget)
        self.error.setGeometry(QtCore.QRect(440, 456, 341, 20))
        self.error.setStyleSheet("font: 12pt \"MS Shell Dlg 2\"; color:red;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.Password = QtWidgets.QLineEdit(self.bgwidget)
        self.Password.setGeometry(QtCore.QRect(60, 370, 671, 41))
        self.Password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Password.setObjectName("Password")
        self.label_4 = QtWidgets.QLabel(self.bgwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 350, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.bgwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 440, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.Password_2 = QtWidgets.QLineEdit(self.bgwidget)
        self.Password_2.setGeometry(QtCore.QRect(60, 460, 671, 41))
        self.Password_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.Password_2.setObjectName("Password_2")
        self.label_6 = QtWidgets.QLabel(self.bgwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 90, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.email_2 = QtWidgets.QLineEdit(self.bgwidget)
        self.email_2.setGeometry(QtCore.QRect(60, 110, 671, 41))
        self.email_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.email_2.setObjectName("email_2")
        self.label_7 = QtWidgets.QLabel(self.bgwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 180, 91, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.email_3 = QtWidgets.QLineEdit(self.bgwidget)
        self.email_3.setGeometry(QtCore.QRect(60, 200, 671, 41))
        self.email_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.email_3.setObjectName("email_3")
        self.lab = QtWidgets.QLabel(self.bgwidget)
        self.lab.setGeometry(QtCore.QRect(60, 180, 151, 21))
        self.lab.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab.setText("")
        self.lab.setObjectName("lab")
        self.lab_3 = QtWidgets.QLabel(self.bgwidget)
        self.lab_3.setGeometry(QtCore.QRect(60, 340, 151, 21))
        self.lab_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab_3.setText("")
        self.lab_3.setObjectName("lab_3")
        self.lab_4 = QtWidgets.QLabel(self.bgwidget)
        self.lab_4.setGeometry(QtCore.QRect(60, 430, 151, 21))
        self.lab_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab_4.setText("")
        self.lab_4.setObjectName("lab_4")
        self.lab_5 = QtWidgets.QLabel(self.bgwidget)
        self.lab_5.setGeometry(QtCore.QRect(60, 520, 151, 21))
        self.lab_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.lab_5.setText("")
        self.lab_5.setObjectName("lab_5")
        self.label_2 = QtWidgets.QLabel(self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 91, 16))
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.bgwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 250, 101, 16))
        self.label_8.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.bgwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 330, 91, 16))
        self.label_9.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.bgwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 420, 91, 16))
        self.label_10.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.bgwidget)
        self.label_11.setGeometry(QtCore.QRect(60, 510, 91, 16))
        self.label_11.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(-10, -30, 760, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setGeometry(QtCore.QRect(-10, 20, 3, 18))
        self.statusbar.setObjectName("statusbar")
        
        # self.bgwidget.setVisible(False)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loginbutton.clicked.connect(self.insert)
        
        
 
        reg_ex = QRegExp("[0-9]{,10}")
        input_validator = QRegExpValidator(reg_ex, self.email_3)
        self.email_3.setValidator(input_validator)
                    
        reg_e = QRegExp("[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$")
        i = QRegExpValidator(reg_e, self.email)
        self.email.setValidator(i)      


        reg_ex = QRegExp("[a-zA-Z]+[ ]+[a-zA-Z]\w{10,20}$")
        input = QRegExpValidator(reg_ex, self.email_2)
        self.email_2.setValidator(input)
        
    def insert(self):
        
        try:
                db=mc.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="login"    
                )
                mycursor=db.cursor()
                name=self.email_2.text()   
                mobile=self.email_3.text()
                email=self.email.text()
                Password=self.Password.text()
                Password_2=self.Password_2.text()
                # self.email_error_message = 'The value should be an email.'
                # self.email_regex = QRegularExpression
                query="INSERT INTO login_db (name,mobile,email,Password,Password_2) VALUES (%s,%s,%s,%s,%s)"
                value=(name,mobile,email,Password,Password_2)
                mycursor.execute(query,value)
                # user=mycursor.fetchall()
                db.commit()
               

                if (len(name) and len(mobile) and len(email) and len(Password) and len(Password_2))==0:
                        self.email_3.setPlaceholderText('Please Mobile number')
                        self.email_2.setPlaceholderText('Please Enter name')
                        self.email.setPlaceholderText('Please Enter email')
                        self.Password.setPlaceholderText("Please enter Password")
                        self.Password_2.setPlaceholderText("Please enter Confirm Password")
                        self.loginbutton.clicked.connect(Form.close)
                        
                elif len(name)==0:
                        self.email_2.setPlaceholderText('Please Enter name')
                        # self.loginbutton.clicked.connect(Form.close) 
                        
                       
                elif len(mobile)==0:
                        self.email_3.setPlaceholderText('Please Mobile number')
                        
                elif len(email)==0:
                        self.email.setPlaceholderText('Please enter email id')

                elif len(Password)==0:
                        self.Password.setPlaceholderText('Please enter Password') 
                elif len(Password_2)==0:
                        self.Password_2.setPlaceholderText('Please enter Confirm Password')  
                        
                else:
                        from log import Ui_Form
                        self.window=QtWidgets.QMainWindow()
                        self.ui=Ui_Form()
                        self.ui.setupUi(self.window)
                        self.window.show() 
                        self.loginbutton.clicked.connect(self.close_window)
                                       
                      
                        


                # elif len(mobile)==0:
                #         self.label_8.setText("Empty input") 
                #         message_box=QMessageBox()
                #         message_box.warning(None,"Error","Enter details")
                          


                # elif len(email)==0:
                #         self.label_9.setText("Empty input") 
                #         message_box=QMessageBox()
                #         message_box.warning(None,"Error","Enter details")
                          

                # elif len(Password)==0:
                #         self.label_10.setText("Empty input") 
                #         message_box=QMessageBox()
                #         message_box.warning(None,"Error","Enter details")
                          

                # elif len(Password_2)==0:
                #         self.label_11.setText("Empty input") 
                #         message_box=QMessageBox()
                #         message_box.warning(None,"Error","Enter details")
                                                 
                           
        except mc.Error as e:
                print("Error")
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Register Page"))
        self.loginbutton.setText(_translate("Form", "Sign Up"))
        self.label_3.setText(_translate("Form", "Email Id"))
        self.label_4.setText(_translate("Form", "Password"))
        self.label_5.setText(_translate("Form", "Confirm Password"))
        self.label_6.setText(_translate("Form", "Name"))
        self.label_7.setText(_translate("Form", "Mobile number"))
    def close_window(window: QWidget):
        window.close()  

if __name__ == "__main__":
        
        import sys
        app=QtWidgets.QApplication(sys.argv)
        Form=QtWidgets.QMainWindow()
        ui1= Ui_Form1()
        ui1.setupUi(Form)
        Form.show()
        
        sys.exit(app.exec_())         
