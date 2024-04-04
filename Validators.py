from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from enum import Enum

class NaturalNumberValidator(QRegularExpressionValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Регулярное выражение для натуральных чисел
        reg_exp = QRegularExpression("[1-9]\\d*")
        self.setRegularExpression(reg_exp)

class ProbabilityNumberValidator(QRegularExpressionValidator):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Регулярное выражение для дробных чисел от 0 до 1
        reg_exp = QRegularExpression("^0(\.\d+)?|1(\.0+)?$")
        self.setRegularExpression(reg_exp)

class TypeValidator (Enum):
    none = 0
    natural = 1

    probaility = 5
def setValidator(lineEdit, validatorType):
    match validatorType:
        case TypeValidator.natural:
            validator = NaturalNumberValidator()
        case TypeValidator.probaility:
            validator = ProbabilityNumberValidator()
        case _:
            print("Validator не выбран!")
            return
    lineEdit.setValidator(validator)

# Пример использования:
# validator = NaturalNumberValidator()
# line_edit = QLineEdit()
# line_edit.setValidator(validator)
