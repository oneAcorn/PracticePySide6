import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDial,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QListWidget,
    QMainWindow,
    QSlider,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])
        
        # Editable combobox
        combobox.setEditable(True)
        """
        QComboBox.InsertPolicy.NoInsert	No insert
        QComboBox.InsertPolicy.InsertAtTop	Insert as first item
        QComboBox.InsertPolicy.InsertAtCurrent	Replace currently selected item
        QComboBox.InsertPolicy.InsertAtBottom	Insert after last item
        QComboBox.InsertPolicy.InsertAfterCurrent	Insert after current item
        QComboBox.InsertPolicy.InsertBeforeCurrent	Insert before current item
        QComboBox.InsertPolicy.InsertAlphabetically	Insert in alphabetical order
        """
        combobox.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        # You can also limit the number of items allowed in the box by using the .setMaxCount() method:
        combobox.setMaxCount(10)
        

        # The default signal from currentIndexChanged sends the index
        combobox.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        combobox.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(combobox)

    def index_changed(self, index):  # index is an int starting from 0
        print(index)

    def text_changed(self, text):  # text is a str
        print(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()