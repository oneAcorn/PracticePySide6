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

        self.lineedit = QLineEdit()
        self.lineedit.setMaxLength(10)
        self.lineedit.setPlaceholderText("Enter your text")

        # self.lineedit.setReadOnly(True) # uncomment this to make readonly

        self.lineedit.returnPressed.connect(self.return_pressed)
        self.lineedit.selectionChanged.connect(self.selection_changed)
        
        """
        There are also two edit signals, one for when the text in the box has been edited and one for when it has been changed.
        The distinction here is between user edits and programmatic changes. The textEdited signal is only sent when the user edits text.
        """
        self.lineedit.textChanged.connect(self.text_changed)
        self.lineedit.textEdited.connect(self.text_edited)
        
        """
        Additionally, it is possible to perform input validation using an input mask to define which characters are supported and where.
        This can be applied to the field as follows:
        self.lineedit.setInputMask('000.000.000.000;_')
        The above would allow a series of 3-digit numbers separated with periods, and could therefore be used to validate IPv4 addresses.
        """

        self.setCentralWidget(self.lineedit)

    def return_pressed(self):
        print("Return pressed!")
        self.lineedit.setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.lineedit.selectedText())

    def text_changed(self, text):
        print("Text changed...")
        print(text)

    def text_edited(self, text):
        print("Text edited...")
        print(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()