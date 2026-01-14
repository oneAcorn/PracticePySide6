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

        checkbox = QCheckBox("This is a checkbox")
        """
        Qt.CheckState.Unchecked	Item is unchecked
        Qt.CheckState.PartiallyChecked	Item is partially checked
        Qt.CheckState.Checked	Item is checked
        """
        checkbox.setCheckState(Qt.CheckState.Checked)

        # For tristate: checkbox.setCheckState(Qt.CheckState.PartiallyChecked)
        # Or: checkbox.setTristate(True)
        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()