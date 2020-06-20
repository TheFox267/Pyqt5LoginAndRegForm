# -*-coding:utf8-*-
import sys
from re import *

from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from sqlscript import SQLighter

learning_moment = ''


def add_data_func():
    """???????? ???????? ? ???? ??????"""
    global learning_moment
    first_name = reg_window.first_name_line_edit.text()
    second_name = reg_window.second_name_line_edit.text()
    password = reg_window.password_line_edit.text()
    mail = reg_window.mail_line_edit.text()
    subject = reg_window.subject_line_edit.text()
    city = reg_window.city_line_edit.text()
    login = reg_window.login_line_edit.text()

    if not first_name == '' and not second_name == '' and not password == '' and not mail == '' and not subject == '' and not learning_moment == '' and not city == '' and not login == '':
        pattern = compile("(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)")
        is_valid = pattern.match(mail)
        if is_valid:
            if not db.reg_mail_unic(mail):
                db.add_people(first_name, second_name, password, mail, subject, learning_moment, city, login)
                print("You successfully registered")
                visible_login_window_func()
            else:
                reg_window.reg_button.setText("This mail is already registered")
        else:
            reg_window.mail_line_edit.setText("Invalid mail")
    else:
        reg_window.reg_button.setText("Fill in all fields")


def exit_func():
    """????? ?? ??????????"""
    sys.exit()


def pupils_set_func():
    """?????????? ?????????? ?????????? ???????? radio button"""
    global learning_moment
    learning_moment = reg_window.pupil_radio_button.text()


def student_set_func():
    """?????????? ?????????? ?????????? ???????? radio button"""
    global learning_moment
    learning_moment = reg_window.student_radio_button.text()


def not_study_set_func():
    """?????????? ?????????? ?????????? ???????? radio button"""
    global learning_moment
    learning_moment = reg_window.not_study_radio_button.text()


def clear_fields_reg_window_func():
    """???????? ????? ?????"""
    global learning_moment
    reg_window.first_name_line_edit.setText('')
    reg_window.second_name_line_edit.setText('')
    reg_window.password_line_edit.setText('')
    reg_window.mail_line_edit.setText('')
    reg_window.subject_line_edit.setText('')
    learning_moment = ''
    reg_window.city_line_edit.setText('')
    reg_window.login_line_edit.setText('')

    for btn in [reg_window.pupil_radio_button, reg_window.student_radio_button, reg_window.not_study_radio_button]:
        btn.setAutoExclusive(False)
        btn.setChecked(False)
        btn.repaint()
        btn.setAutoExclusive(True)


def visible_login_window_func():
    """???????? ???? ?????"""
    # ???, ??? ??????????
    login_window.show()
    # ???, ??? ????????
    main_menu.hide()
    reg_window.hide()


def clear_fields_login_window_func():
    """???????? ???? ?? ???? ??????"""
    login_window.mail_line_edit.setText('')
    login_window.password_line_edit.setText('')


def visible_reg_window_func():
    """???????? ???? ???????????"""
    # ???, ??? ??????????
    reg_window.show()  # ????? ???? ???????????
    # ???, ??? ????????
    login_window.hide()
    main_menu.hide()


def log_in_func():
    """?????? ? ??????? ??????"""
    mail = login_window.mail_line_edit.text()
    password = login_window.password_line_edit.text()
    if not mail == '' and not password == '':
        if db.log_in_people(mail, password):
            visible_app_window()
        else:
            login_window.mail_line_edit.setText('Wrong mail')
            login_window.password_line_edit.setText('Wrong password')
    elif not mail == '':
        login_window.password_line_edit.setText('Enter the password')
    elif not password == '':
        login_window.mail_line_edit.setText('Enter your mail')
    else:

        login_window.mail_line_edit.setText('Enter your mail')
        login_window.password_line_edit.setText('Enter the password')


def change_echo_mode_reg_func(state):
    """???????? ?????? ? ??????"""
    if state == Qt.Checked:
        reg_window.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        reg_window.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)


def change_echo_mode_login_func(state):
    """???????? ?????? ? ??????"""
    if state == Qt.Checked:
        login_window.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        login_window.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)


def visible_app_window():
    """"????? ???? ??????????"""
    login_window.hide()
    app_window.show()


# ????? ?????? ?? ??????? ?????
db = SQLighter('db.db')

# ???????? ??????????
app = QtWidgets.QApplication([])

# ???????? ???? ???????????
reg_window = uic.loadUi("Reg.ui")
# ??????????? ?????? ? ????
reg_window.setWindowIcon(QIcon('sign_up_png.png'))

reg_window.reg_button.clicked.connect(add_data_func)

reg_window.pupil_radio_button.clicked.connect(pupils_set_func)
reg_window.student_radio_button.clicked.connect(student_set_func)
reg_window.not_study_radio_button.clicked.connect(not_study_set_func)

reg_window.exit_button.clicked.connect(exit_func)

reg_window.clear_button.clicked.connect(clear_fields_reg_window_func)

reg_window.log_in_button.clicked.connect(visible_login_window_func)

reg_window.visible_password_check_box.stateChanged.connect(change_echo_mode_reg_func)

# ???????? ???? ??????
login_window = uic.loadUi("Login.ui")

login_window.exit_button.clicked.connect(exit_func)

login_window.clear_button.clicked.connect(clear_fields_login_window_func)

login_window.reg_button.clicked.connect(visible_reg_window_func)

login_window.log_in_button.clicked.connect(log_in_func)

login_window.setWindowIcon(QIcon('log_in_png.png'))

login_window.visible_password_check_box.stateChanged.connect(change_echo_mode_login_func)

# ???????? ???????? ????
main_menu = uic.loadUi("Main_menu.ui")

main_menu.reg_form_button.clicked.connect(visible_reg_window_func)

main_menu.log_in_form_button.clicked.connect(visible_login_window_func)

main_menu.exit_button.clicked.connect(exit_func)

main_menu.show()

# ???????? ???? ??????????
app_window = uic.loadUi("App_Window.ui")

app.exec()

#  Copyright (c) 2020.  Designed TheFox
