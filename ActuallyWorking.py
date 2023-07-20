# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\AditVikramMishra\Documents\trail.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from turtle import color
from PyQt5 import QtCore, QtGui, QtWidgets
from segment_anything import sam_model_registry, SamPredictor
import os
import torch
import time
import cv2
import numpy as np

class Ui_SAMprototype(object):
    IMAGE_SIZE = (1400,789)
    imagePath=""
    folderPath=None
    totalImages=None
    currImage=0
    sam_checkpoint = r"C:\Users\AditVikramMishra\Downloads\sam_vit_h_4b8939.pth" #Enter actual download path
    device="cpu"
    model_type = "default"
    sam = sam_model_registry[model_type](checkpoint = sam_checkpoint)
    img=None
    sam.to(device)
    predictor = SamPredictor(sam)
    best_mask = None
    best_score=0
    def setupUi(self, SAMprototype):
        SAMprototype.setObjectName("SAMprototype")
        SAMprototype.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SAMprototype.sizePolicy().hasHeightForWidth())
        SAMprototype.setSizePolicy(sizePolicy)
        SAMprototype.setMaximumSize(QtCore.QSize(1600, 900))
        self.centralwidget = QtWidgets.QWidget(SAMprototype)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1591, 851))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainContainer = QtWidgets.QHBoxLayout()
        self.mainContainer.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.mainContainer.setObjectName("mainContainer")
        self.btnContainer = QtWidgets.QVBoxLayout()
        self.btnContainer.setObjectName("btnContainer")
        self.prevBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.prevBtn.mousePressEvent = self.prevImage
        self.prevBtn.setObjectName("prevBtn")
        self.btnContainer.addWidget(self.prevBtn)
        self.nextBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.nextBtn.mousePressEvent = self.nextImage
        self.nextBtn.setObjectName("nextBtn")
        self.btnContainer.addWidget(self.nextBtn)
        self.saveBtn = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.saveBtn.setObjectName("saveBtn")
        self.btnContainer.addWidget(self.saveBtn)
        self.mainContainer.addLayout(self.btnContainer)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMinimumSize(QtCore.QSize(1400, 750))
        self.image.setMaximumSize(QtCore.QSize(1400, 800))
        self.image.setScaledContents(True)
        self.image.setPixmap(QtGui.QPixmap(self.imagePath))
        self.image.mousePressEvent = self.getPos
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)
        self.mainContainer.addLayout(self.gridLayout)
        self.boxNamesContainer = QtWidgets.QVBoxLayout()
        self.boxNamesContainer.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.boxNamesContainer.setSpacing(8)
        self.boxNamesContainer.setObjectName("boxNamesContainer")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.boxNamesContainer.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.boxNamesContainer.addWidget(self.label_2)
        self.yCoord = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        self.yCoord.setMinimumSize(QtCore.QSize(0, 200))
        self.yCoord.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.yCoord.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.yCoord.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.yCoord.setObjectName("yCoord")
        self.boxNamesContainer.addWidget(self.yCoord)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.boxNamesContainer.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.boxNamesContainer.addWidget(self.label_3)
        self.xCoord = QtWidgets.QLCDNumber(self.gridLayoutWidget_2)
        self.xCoord.setMinimumSize(QtCore.QSize(0, 200))
        self.xCoord.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.xCoord.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.xCoord.setObjectName("xCoord")
        self.boxNamesContainer.addWidget(self.xCoord)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.boxNamesContainer.addItem(spacerItem2)
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textEdit.setLineWidth(2)
        self.textEdit.setObjectName("textEdit")
        self.boxNamesContainer.addWidget(self.textEdit)
        self.mainContainer.addLayout(self.boxNamesContainer)
        self.verticalLayout_3.addLayout(self.mainContainer)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathLabel.sizePolicy().hasHeightForWidth())
        self.pathLabel.setSizePolicy(sizePolicy)
        self.pathLabel.setMinimumSize(QtCore.QSize(50, 25))
        self.pathLabel.setMaximumSize(QtCore.QSize(122, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pathLabel.setFont(font)
        self.pathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pathLabel.setObjectName("pathLabel")
        self.horizontalLayout.addWidget(self.pathLabel)
        self.pathReader = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathReader.sizePolicy().hasHeightForWidth())
        self.pathReader.setSizePolicy(sizePolicy)
        self.pathReader.setMinimumSize(QtCore.QSize(0, 25))
        self.pathReader.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pathReader.setFrameShape(QtWidgets.QFrame.Box)
        self.pathReader.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.pathReader.setReadOnly(False)
        self.pathReader.setObjectName("pathReader")
        self.horizontalLayout.addWidget(self.pathReader)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.mousePressEvent = self.openFolder
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pathDisplay = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.pathDisplay.setMinimumSize(QtCore.QSize(0, 25))
        self.pathDisplay.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pathDisplay.setFrameShape(QtWidgets.QFrame.Panel)
        self.pathDisplay.setObjectName("pathDisplay")
        self.gridLayout_3.addWidget(self.pathDisplay, 2, 0, 1, 1)
        SAMprototype.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SAMprototype)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        SAMprototype.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SAMprototype)
        self.statusbar.setObjectName("statusbar")
        SAMprototype.setStatusBar(self.statusbar)
        self.actionOpen_Directory = QtWidgets.QAction(SAMprototype)
        self.actionOpen_Directory.setObjectName("actionOpen_Directory")
        self.actionExit = QtWidgets.QAction(SAMprototype)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_Directory)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SAMprototype)
        QtCore.QMetaObject.connectSlotsByName(SAMprototype)

    def retranslateUi(self, SAMprototype):
        _translate = QtCore.QCoreApplication.translate
        SAMprototype.setWindowTitle(_translate("SAMprototype", "MainWindow"))
        self.prevBtn.setText(_translate("SAMprototype", "Prev"))
        self.nextBtn.setText(_translate("SAMprototype", "Next"))
        self.saveBtn.setText(_translate("SAMprototype", "Save"))
        self.label_2.setText(_translate("SAMprototype", "Y Coordinate"))
        self.label_3.setText(_translate("SAMprototype", "X Coordinate"))
        self.pathLabel.setText(_translate("SAMprototype", "Enter Directory path"))
        self.pathReader.setPlaceholderText(_translate("SAMprototype", "Enter File Path of Images Folder"))
        self.pushButton.setText(_translate("SAMprototype", "Open"))
        self.menuFile.setTitle(_translate("SAMprototype", "File"))
        self.actionOpen_Directory.setText(_translate("SAMprototype", "Open Directory"))
        self.actionOpen_Directory.setToolTip(_translate("SAMprototype", "<html><head/><body><p><span style=\" font-weight:600;\">Open Directory</span></p></body></html>"))
        self.actionExit.setText(_translate("SAMprototype", "Exit"))

    def getPos(self , event):
        xCord = event.pos().x()
        yCord = event.pos().y()
        self.xCoord.display(xCord)
        self.yCoord.display(yCord)
        input_point = np.array([[xCord,yCord]])
        input_label = np.array([1])
        masks, scores, logits = self.predictor.predict(point_coords = input_point,
                  point_labels = input_label,
                  multimask_output=False)
        '''
        for _, (mask, score) in enumerate(zip(masks, scores)):
            if score>self.best_score:
                self.best_mask = mask
                self.best_score = score
        '''
        #self.best_mask = masks[0]
        x, y, height, width = self.getBoxCoords(masks[0])
        tempImage = cv2.imread(self.imagePath)
        tempImage = cv2.resize(tempImage, self.IMAGE_SIZE)
        tempImage = cv2.rectangle(tempImage, (x,y), (width, height),(0,0,255), 2)
        cv2.imwrite(self.imagePath, tempImage)
        self.image.setPixmap(QtGui.QPixmap(self.imagePath))
        self.idontknowwhatitdoes()

    def idontknowwhatitdoes(self):
        pass

    def getBoxCoords(self, mask):
        i=0
        flag=1
        #finding height and y
        for colm in mask:
            if True in colm and flag==1:
                height=i
                y=i
                flag=0
            elif True in colm:
                height=i
            i+=1
        i=0
        
        #finding width and x
        flag=1
        rotatedMask = np.rot90(mask,3)
        for colm in rotatedMask:
            if True in colm and flag==1:
                width=i
                x=i
                flag=0
            elif True in colm:
                width=i
            i+=1
        return x, y, height, width


    def openFolder(self, event):
        self.folderPath = self.pathReader.toPlainText()
        if self.folderPath=="":
            self.pathDisplay.setText("Enter Valid path!!!!! ")
        else:
            self.pathDisplay.setText(self.folderPath)
        self.totalImages = os.listdir(self.folderPath)
        self.pathDisplay.append(" "+str(len(self.totalImages)))
        self.currImage=0
        self.imagePath = os.path.join(self.folderPath, self.totalImages[self.currImage])
        self.img = None
        self.setImageToPredictor()
        self.textEdit.clear()
        self.textEdit.setText("-> IMAGE LOADED TO MODEL")
        self.image.setPixmap(QtGui.QPixmap(self.imagePath))
        

    def setImageToPredictor(self):
        self.img = cv2.imread(self.imagePath)
        self.img = cv2.resize(self.img, self.IMAGE_SIZE)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.predictor.set_image(self.img)       
        
    
    def prevImage(self, event):
        if self.currImage==0:
            self.pathDisplay.setText("****Cannot Go back****")
        else:
            self.currImage-=1
            self.imagePath = os.path.join(self.folderPath, self.totalImages[self.currImage])
            self.img = None
            self.setImageToPredictor()
            self.textEdit.clear()
            self.textEdit.setText("-> IMAGE LOADED TO MODEL")
            self.image.setPixmap(QtGui.QPixmap(self.imagePath))
    
    def nextImage(self, event):
        if self.currImage==len(self.totalImages)-1:
            self.pathDisplay.setText("****Cannot Go forward****")
        else:
            self.currImage+=1
            self.imagePath = os.path.join(self.folderPath, self.totalImages[self.currImage])
            self.img = None
            self.setImageToPredictor()
            self.textEdit.clear()
            self.textEdit.setText("-> IMAGE LOADED TO MODEL")
            self.image.setPixmap(QtGui.QPixmap(self.imagePath))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SAMprototype = QtWidgets.QMainWindow()
    ui = Ui_SAMprototype()
    ui.setupUi(SAMprototype)
    SAMprototype.show()
    sys.exit(app.exec_())
