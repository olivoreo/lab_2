from PyQt6.QtGui import QValidator
from PyQt6 import QtCore, QtGui, QtWidgets
from Validators import TypeValidator
def getStateValidator (lineEdit):
    return lineEdit.validator().validate(lineEdit.text(), 0)[0]
def getIntFromLineEdit(lineEdit):
    text = lineEdit.text()
    validator_state = getStateValidator(lineEdit)
    if (text == ""):
        return 0
    elif (validator_state == QValidator.State.Acceptable):
        return int(text)
    return 0
def getFloatFromLineEdit(lineEdit):
    text = lineEdit.text()
    validator_state = getStateValidator(lineEdit)
    if (text == ""):
        return 0
    elif (validator_state == QValidator.State.Acceptable):
        return float(text)
    return 0
def getValueFromLineEdit (lineEdit, typeValidator):
    match (typeValidator):
        case TypeValidator.natural:
            return getIntFromLineEdit(lineEdit)
        case TypeValidator.probaility:
            return getFloatFromLineEdit(lineEdit)
        case _:
            return 0