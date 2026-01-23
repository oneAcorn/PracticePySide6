from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)
        
        button_action = QAction("Your button", self)
        button_action.setStatusTip("this is your button")
        button_action.triggered.connect(self.toolbar_button_clicked)
        toolbar.addAction(button_action)
        
        checkable_action = QAction("Checkable button", self)
        checkable_action.setStatusTip("this is Checkable")
        checkable_action.setCheckable(True)
        checkable_action.triggered.connect(self.toolbar_check_btn_clicked)
        toolbar.addAction(checkable_action)
        
        self.setStatusBar(QStatusBar(self))
    
    def toolbar_button_clicked(self, s: bool):
        """_summary_

        Args:
            s (bool): Why is the signal always false? The signal passed indicates whether the button is checked,
            and since our button is not checkable — just clickable — it is always false.
        """
        print("click", s)

    def toolbar_check_btn_clicked(self, s: bool):
        print("checkable", s)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()