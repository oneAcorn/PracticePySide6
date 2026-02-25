import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, 
    QPushButton, 
    QDialog, 
    QDialogButtonBox,
    QVBoxLayout,
    QLabel
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)
        dlg = CustomDialog(self)
        dlg.setWindowTitle("HELLO!")
        dlg.exec()
        
class CustomDialog(QDialog):
    def __init__(self, /, parent = ..., f = ..., *, sizeGripEnabled = ..., modal = ...):
        super().__init__(parent, f, sizeGripEnabled=sizeGripEnabled, modal=modal)
        self.setWindowTitle("hello")
        QBtn = (QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.rejected)
        
        layout = QVBoxLayout()
        msg = QLabel("blabla,bla! ... blala?", "is that ok?")
        layout.addWidget(msg)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()