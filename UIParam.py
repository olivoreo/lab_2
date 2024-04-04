from Validators import TypeValidator


class InputLineDataParam:
    def __init__(self):
        self.lableText = ""  # Строка-пояснение для поля ввода данных
        self.validatorType = TypeValidator.none  # тип вfлидатора для поля ввода данных
        self.visibility = False  # Видимость поля ввода данных
        self.needValue = False #Необоходимость передавать число вычислительной функции
class InputListDataParam:
    def __init__(self):
        self.lableText = "" #Строка-пояснение для списка данных
        self.nameElement = "" #Строка-пояснение для эллементов списка данных (необходимо наличие %d для добавления индекса)
        self.validatorTypeElementList = TypeValidator.none #тип валидатора для элементов сипска

        self.constNumElements = False #количество элементов - постоянное или изменяемое
        self.numOfLineEditListenerList = 0  # Выбор номера поля ввода данных, который будет изменять количество эллементов списке
        self.numElements = 0 #количество элементов в списке, если оно константное (начальное)
        self.startIndex = 0  # число, с которого начинается индексация элементов списка
        self.maxNumElements = 30  #Максимальное колличество элементов

        self.visibility = False  # Видимость списка данных
        self.needValues = False #Необоходимость передавать cписок значений вычислительной функции
class CheckBoxListParam:
    def __init__(self):
        self.lableText = "" #Строка-пояснение для списка флагов
        self.nameElement = "" #Строка-пояснение для эллементов списка данных (необходимо наличие %d для добавления индекса)

        self.constNumElements = False #количество элементов - постоянное или изменяемое
        self.numOfLineEditListenerList = 0  #Выбор номера поля ввода данных, который будет изменять количество эллементов списке
        self.numElements = 0 #количество элементов в списке, если оно константное (начальное)
        self.startIndex = 0  # число, с которого начинается индексация элементов списка
        self.maxNumElements = 30  #Максимальное колличество элементов

        self.visibility = False  # Видимость списка данных
        self.needValues = False #Необоходимость передавать cписок значений вычислительной функции
class PictureParam:
    def __init__(self):
        self.name = "" #имя изображения
        self.extension = "png" #тип расширения изображения
        self.width = -1
    def getPictureName (self):
        return self.name + '.' + self.extension
    def visibility(self):
        if len(self.name) == 0:
            return False
        else:
            return True
class TextParam:
    def __init__(self):
        self.text = ""
        self.visibility = False  # видимость текста
class UiParam:
    def __init__(self):
        self.textTask = TextParam()
        self.pictureTask = PictureParam()

        self.line1 = InputLineDataParam()
        self.line2 = InputLineDataParam()
        self.line3 = InputLineDataParam()

        self.list1 = InputListDataParam()
        self.list2 = InputListDataParam()
        self.checkBoxList = CheckBoxListParam()

        self.pictureResult = PictureParam()

        self.function = None #Формула для вычисления конечно результата

