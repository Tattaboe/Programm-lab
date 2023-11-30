import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from Text_annotation_file import creating_annotation
from Copy_dataset import dataset2, creating_annotation2
from Random_number_images import dataset3, creating_annotation3
from Classes_of_iterator import Iterator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.initIterator()
        self.createAction()
        self.createMenuBar()
        self.createToolBar()
        
    def initUI(self):
                
        self.resize(1200,900)
        self.center()
        self.setWindowTitle('Котики и песики')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        cat_btn=QPushButton('Следующий кот',self)
        dog_btn=QPushButton('Следующий пес',self)

        
        self.lbl = QLabel(self)
        
        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(cat_btn)
        hbox.addWidget(dog_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)
        
        cat_btn.clicked.connect(self.nextcat)
        dog_btn.clicked.connect(self.nextdog)

        self.folderpath = ' '
        
        
        self.show()
     
    def initIterator(self):
        self.cat=Iterator('cats','dataset')
        self.dog=Iterator('dogs','dataset')
        
    def nextcat(self):
        lbl_size = self.lbl.size()
        next_image = next(self.cat)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:        
            self.initIterator()
            self.nextcat()
                 
    def nextdog(self):
        lbl_size = self.lbl.size()
        next_image = next(self.dog)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:        
            self.initIterator()
            self.nextdog()
        
        
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    
    def createMenuBar(self):
        
        menuBar = self.menuBar()
        
        self.fileMenu = menuBar.addMenu('&Файлы')
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.changeAction)
        
        self.annotMenu = menuBar.addMenu('&Аннотации')
        self.annotMenu.addAction(self.createAnnotAction)
        
        self.dataMenu=menuBar.addMenu('&Dataset')
        self.dataMenu.addAction(self.createData2Action)
        
    def createToolBar(self):
        fileToolBar=self.addToolBar('Файл')
        fileToolBar.addAction(self.exitAction)
        
        annotToolBar=self.addToolBar('Аннотация')
        annotToolBar.addAction(self.createAnnotAction)
        
    def createAction(self):
        self.exitAction = QAction('&Выход')
        self.exitAction.triggered.connect(qApp.quit)

        self.changeAction = QAction('&Замена dataset')
        self.changeAction.triggered.connect(self.changeDataset)

        self.createAnnotAction = QAction('&Создать аннотацию для текущего набора данных')
        self.createAnnotAction.triggered.connect(self.createAnnotation)

        self.createData2Action = QAction('&Cоздать dataset2')
        self.createData2Action.triggered.connect(self.createDataset2)

        self.createData3Action = QAction('&Создать dataset3')
        self.createData3Action.triggered.connect(self.createDataset3)
        
    def createAnnotation(self):
        if 'dataset2' in str(self.folderpath):
            creating_annotation2()
        elif 'dataset3' in str(self.folderpath):
            creating_annotation3()
        elif 'dataset' in str(self.folderpath):
            creating_annotation()
      
            
    def createDataset2(self):
        dataset2()
        self.dataMenu.addAction(self.createData3Action)
       
        
        
    def createDataset3(self):
        dataset3()
        
        
    def changeDataset(self):
       
        self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(
                self, 'Выберете папку')
        
        
    def closeEvent(self,event):
        event.accept()
        
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())