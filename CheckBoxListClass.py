from PyQt6 import QtWidgets, QtCore
from Validators import setValidator
from myQTFunctions import getIntFromLineEdit, getFloatFromLineEdit, getValueFromLineEdit
from UIParam import CheckBoxListParam
class CheckBoxListClass:
    def __init__(self, centralwidget):
        self.scrollArea = QtWidgets.QScrollArea(parent=centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 372, 106))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.linearLayoutForScroll = QtWidgets.QVBoxLayout()
        self.linearLayoutForScroll.setContentsMargins(10, 10, 10, 10)
        self.linearLayoutForScroll.setSpacing(7)
        self.linearLayoutForScroll.setObjectName("linearLayoutForScroll")

        self.scrollAreaWidgetContents.setLayout(self.linearLayoutForScroll)

        self.checkBoxList = list()
        self.param = CheckBoxListParam()

    def setNumOfListElements(self, number):
        num = min(number, self.param.maxNumElements)
        listLength = len(self.checkBoxList)

        for i in range(num - listLength):
            self.addListElement()
        for i in range(listLength-1, num-1, -1):
            self.linearLayoutForScroll.removeWidget(self.checkBoxList[i])
            self.checkBoxList[i].deleteLater()
            self.checkBoxList.pop()
    def addListElement(self):
        index = len(self.checkBoxList)
        if (index >= self.param.maxNumElements):
            return

        checkBox = QtWidgets.QCheckBox(parent=self.scrollArea)
        l = tuple([index + self.param.startIndex]*self.param.nameElement.count('%'))
        checkBox.setText(self.param.nameElement % (l))

        self.checkBoxList.append(checkBox)

        self.linearLayoutForScroll.addWidget(checkBox)
    def getList(self):
        numList = []
        for checkBox in self.checkBoxList:
            numList.append(checkBox.isChecked())
        return numList
    def setVisibility(self, visibility):
        self.scrollArea.setVisible(visibility)
    def setParam(self, newParam):
        self.param = newParam
        self.setVisibility(self.param.visibility)
        if (self.param.constNumElements):
            self.setNumOfListElements(self.param.numElements)
