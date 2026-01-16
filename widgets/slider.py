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

        slider = QSlider()
        
        # You can also construct a slider with a vertical or horizontal orientation by passing the orientation in as you create it. 
        # slider = QSlider(Qt.Orientation.Vertical)
        # slider = QSlider(Qt.Orientation.Horizontal)

        slider.setMinimum(-10)
        slider.setMaximum(3)
        # Or: slider.setRange(-10,3)

        """
        The singleStep property of a QSlider only affects keyboard navigation when using arrow keys.
        When we interact with the slider using the mouse, the singleStep is ignored, and the slider can be moved freely.
        """
        slider.setSingleStep(3)

        slider.valueChanged.connect(self.value_changed)
        slider.sliderMoved.connect(self.slider_position)
        slider.sliderPressed.connect(self.slider_pressed)
        slider.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(slider)

    def value_changed(self, value):
        print(value)

    def slider_position(self, position):
        print("position", position)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()