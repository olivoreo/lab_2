from PyQt6 import QtWidgets, QtCore
from Validators import setValidator
from myQTFunctions import getIntFromLineEdit, getFloatFromLineEdit, getValueFromLineEdit
from UIParam import InputListDataParam
class LineEditListClass:
    def __init__(self, centralwidget):
        self.scrollArea = QtWidgets.QScrollArea(parent=centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 372, 106))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.formLayoutForScroll = QtWidgets.QFormLayout()
        self.formLayoutForScroll.setContentsMargins(10, 10, 10, 10)
        self.formLayoutForScroll.setSpacing(7)
        self.formLayoutForScroll.setObjectName("formLayoutForScroll")

        self.scrollAreaWidgetContents.setLayout(self.formLayoutForScroll)

        self.labelList = list()
        self.lineEditList = list()
        self.param = InputListDataParam()

    def setNumOfListElements(self, number):
        num = min(number, self.param.maxNumElements)
        mListLength = len(self.lineEditList)

        for i in range(num - mListLength):
            self.addListElement()
        for i in range(mListLength-1, num-1, -1):
            self.lineEditList[i].deleteLater()
            self.labelList[i].deleteLater()
            self.formLayoutForScroll.removeRow(i)
            self.labelList.pop()
            self.lineEditList.pop()
    def addListElement(self):
        index = len(self.lineEditList)
        if (index >= self.param.maxNumElements):
            return

        label = QtWidgets.QLabel(parent=self.scrollArea)
        self.setLabelText(label, index)

        lineEdit = QtWidgets.QLineEdit(parent=self.scrollArea)
        setValidator(lineEdit, self.param.validatorTypeElementList)

        self.labelList.append(label)
        self.lineEditList.append(lineEdit)

        self.formLayoutForScroll.setWidget(index, QtWidgets.QFormLayout.ItemRole.LabelRole, label)
        self.formLayoutForScroll.setWidget(index, QtWidgets.QFormLayout.ItemRole.FieldRole, lineEdit)
    def setLabelText(self, label, index):
        l = tuple([index + self.param.startIndex] * self.param.nameElement.count('%'))
        label.setText(self.param.nameElement % (l))
    def updateLabelsText(self):
        for i in range(len(self.lineEditList)):
            self.setLabelText(self.labelList[i], i)

    def getList(self):
        numList = []
        for lineEdit in self.lineEditList:
            numList.append(getValueFromLineEdit(lineEdit, self.param.validatorTypeElementList))
        return numList
    def setVisibility(self, visibility):
        self.scrollArea.setVisible(visibility)
    def setParam(self, newParam):
        self.param = newParam
        self.setVisibility(self.param.visibility)
        print(self.param.visibility)
        self.updateLabelsText()
        if (self.param.constNumElements):
            self.setNumOfListElements(self.param.numElements)
