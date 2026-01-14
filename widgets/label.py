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
        
        layout = QVBoxLayout()

        label = QLabel("Hello")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        """
        available for horizontal alignment are:
        Qt.AlignmentFlag.AlignLeft	Aligns with the left edge.
        Qt.AlignmentFlag.AlignRight	Aligns with the right edge.
        Qt.AlignmentFlag.AlignHCenter	Centers horizontally in the available space.
        Qt.AlignmentFlag.AlignJustify	Justifies the text in the available space.
        
        The flags available for vertical alignment are:
        Qt.AlignmentFlag.AlignTop	Aligns with the top.
        Qt.AlignmentFlag.AlignBottom	Aligns with the bottom.
        Qt.AlignmentFlag.AlignVCenter	Centers vertically in the available space.

        others:
        Qt.AlignmentFlag.AlignCenter	Centers horizontally and vertically
        """
        label.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        )
        layout.addWidget(label)
        
        label2 = QLabel()
        label2.setPixmap(QPixmap("otje.webp"))
        # label2.setScaledContents(True)
        layout.addWidget(label2)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()