from UIParam import UiParam
from Validators import TypeValidator
import probabilityFunctions

def paramList():
    paramList = []
    paramList.append(initializationParam0()) #текст задачи, картинка задачи, список дробных чисел, формула вычисления
    paramList.append(initializationParam1()) #текст задачи, картинка задачи, 3 чсиал || список дробных чисел, формула вычисления
    paramList.append(initializationParam2()) #2 списка: 1-вероятность гипотезы, 2-список-вероятность события при гипотезе. общее количество элементов, формула вычисления
    paramList.append(initializationParam3()) #всё тоже самое что и формула полной вер. + добавить checkButton для каждой гипотезы.
    return paramList
def initializationParam0():
    param = UiParam()
    param.list1.lableText = "Вероятности эллементов:"
    param.list1.nameElement = "q%d"
    param.list1.validatorTypeElementList = TypeValidator.probaility
    param.list1.constNumElements = True
    param.list1.startIndex = 1
    param.list1.numElements = 6
    param.list1.visibility = True
    param.list1.needValues = True

    param.pictureTask.name = "Task 1"
    param.pictureTask.extension = "png"
    param.pictureTask.width = 600

    param.pictureResult.name = "Task 2_Formula"
    param.pictureResult.extension = "png"

    param.function = lambda values: probabilityFunctions.task1_lab2(values.list1)
    return param

def initializationParam1():
    param = UiParam()

    param.list1.lableText = "Вероятности попадания стрелков:"
    param.list1.nameElement = "p%d"
    param.list1.validatorTypeElementList = TypeValidator.probaility
    param.list1.constNumElements = True
    param.list1.startIndex = 1
    param.list1.numElements = 5
    param.list1.visibility = True
    param.list1.needValues = True

    param.pictureTask.name = "Task 2"
    param.pictureTask.extension = "png"
    param.pictureTask.width = 600

    param.pictureResult.name = "Task2_Solution"
    param.pictureResult.extension = "png"

    param.function = lambda values: probabilityFunctions.Task2_Lab2(values.list1)
    return param

def initializationParam2():
    param = UiParam()

    param.line1.lableText = "Количество эллементов:"
    param.line1.validatorTypeElementList = TypeValidator.natural
    param.line1.validatorType = TypeValidator.natural
    param.line1.visibility = True

    param.list1.lableText = "Вероятности гипотез:"
    param.list1.nameElement = "P(H%d)"
    param.list1.startIndex = 0
    param.list1.numOfLineEditListenerList = 1
    param.list1.validatorTypeElementList = TypeValidator.probaility
    param.list1.visibility = True
    param.list1.needValues = True

    param.list2.lableText = "Вероятности событий А:"
    param.list2.nameElement = "P(A|H%d)"
    param.list2.startIndex = 0
    param.list2.numOfLineEditListenerList = 1
    param.list2.validatorTypeElementList = TypeValidator.probaility
    param.list2.visibility = True
    param.list2.needValues = True

    param.pictureResult.name = "Формула полной вероятности"
    param.pictureResult.extension = "jpg"

    param.function = lambda values: probabilityFunctions.totalProbability(values.list1, values.list2)
    return param

def initializationParam3():
    param = UiParam()

    param.line1.lableText = "Количество эллементов:"
    param.line1.validatorTypeElementList = TypeValidator.natural
    param.line1.validatorType = TypeValidator.natural
    param.line1.visibility = True

    param.list1.lableText = "Вероятности гипотез:"
    param.list1.nameElement = "P(H%d)"
    param.list1.startIndex = 0
    param.list1.numOfLineEditListenerList = 1
    param.list1.validatorTypeElementList = TypeValidator.probaility
    param.list1.visibility = True
    param.list1.needValues = True

    param.list2.lableText = "Вероятности событий А:"
    param.list2.nameElement = "P(A%d|H%d)"
    param.list2.startIndex = 0
    param.list2.numOfLineEditListenerList = 1
    param.list2.validatorTypeElementList = TypeValidator.probaility
    param.list2.visibility = True
    param.list2.needValues = True

    param.checkBoxList.lableText = "Необходимый результат:"
    param.checkBoxList.nameElement = "P(H%d)"
    param.checkBoxList.startIndex = 0
    param.checkBoxList.numOfLineEditListenerList = 1
    param.checkBoxList.visibility = True
    param.checkBoxList.needValues = True

    param.pictureResult.name = "Формула Байеса"
    param.pictureResult.extension = "jpg"

    param.function = lambda values: probabilityFunctions.convertResultBayes(
        probabilityFunctions.formulaBayes(values.list1, values.list2, values.list3),
        "P(H%d|A) = ",
        0
    )
    return param