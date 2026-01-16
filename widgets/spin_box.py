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

        spinbox = QSpinBox()
        # Or: doublespinbox = QDoubleSpinBox()

        spinbox.setMinimum(-10)
        spinbox.setMaximum(3)
        # Or: spinbox.setRange(-10, 3)

        spinbox.setPrefix("$")
        spinbox.setSuffix("c")
        spinbox.setSingleStep(3)  # Or setSingleStep(3.0) for QDoubleSpinBox
        spinbox.valueChanged.connect(self.value_changed)
        spinbox.textChanged.connect(self.value_changed_str)
        
        # readonly
        # spinbox.lineEdit().setReadOnly(True)

        self.setCentralWidget(spinbox)

    def value_changed(self, value):
        print(value)

    def value_changed_str(self, str_value):
        print(str_value)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()