import os
import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QFileSystemModel
from design import Ui_MainWindow
from PyQt5.QtWidgets import *
import Text_annotation_file,Copy_dataset,Random_number_images,function_next,Classes_of_iterator
from Classes_of_iterator import Iterator
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

     

        self.ui.pushButton.clicked.connect(self.click_pushButton)
        self.ui.pushButton_2.clicked.connect(self.click_pushButton_2)
        self.ui.action_3.triggered.connect(qApp.quit)
    
    def initIterator(self):
        self.cats=Iterator('cats','dataset')
        self.dogs=Iterator('dogs','dataset')
        
    def click_pushButton(self):
        path = next(self.cats)
        self.resize_image(path)

    def click_pushButton_2(self):
        path = next(self.dogs)
        self.resize_image(path)    

    def resize_image(self, path):
        pixmap = QPixmap(path)
        if pixmap.width() > pixmap.height():
            pixmap = pixmap.scaledToWidth(self.ui.image.width())
        else:
            pixmap = pixmap.scaledToHeight(self.ui.image.height())
        self.ui.image.setPixmap(pixmap)

    
 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())