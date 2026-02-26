import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsScene, 
                               QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem)
from PySide6.QtGui import QBrush, QPen, QPainter
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 1. 创建一个场景，并设置其边界 (x, y, width, height)
        #    设置清晰的场景边界有助于视图正确定位和滚动[citation:8]
        self.scene = QGraphicsScene(0, 0, 600, 400)

        # 2. 在场景中添加图形项
        self.add_items()

        # 3. 创建一个视图，并将场景设置进去
        self.view = QGraphicsView(self.scene)
        # 开启抗锯齿，让图形边缘更平滑[citation:1]
        self.view.setRenderHint(QPainter.Antialiasing)
        # 允许通过鼠标拖拽来框选图形项
        self.view.setDragMode(QGraphicsView.RubberBandDrag)

        # 将视图设置为主窗口的中心部件
        self.setCentralWidget(self.view)

        self.setWindowTitle("QGraphicsScene 与 QGraphicsView 示例")
        self.resize(800, 600)

    def add_items(self):
        """向场景中添加一些示例图形项"""

        # --- 方法一：创建图形项对象，然后添加到场景 ---
        # 创建一个矩形图形项 (x, y, width, height)，坐标相对于图形项本身
        rect_item = QGraphicsRectItem(0, 0, 150, 100)
        # 设置图形项在场景中的位置
        rect_item.setPos(50, 30)
        # 设置填充画刷
        rect_item.setBrush(QBrush(Qt.blue))
        # 设置画笔（轮廓线）
        pen = QPen(Qt.cyan)
        pen.setWidth(3)
        rect_item.setPen(pen)
        # 让这个矩形可以被用户拖动[citation:8]
        rect_item.setFlag(QGraphicsRectItem.ItemIsMovable, True)
        # 让这个矩形可以被选中
        rect_item.setFlag(QGraphicsRectItem.ItemIsSelectable, True)
        self.scene.addItem(rect_item)

        # --- 方法二：使用场景的便捷方法创建图形项，并直接获取指针 ---
        # 创建一个椭圆，相当于一个圆 (x, y, width, height)
        ellipse_item = self.scene.addEllipse(0, 0, 100, 100)
        ellipse_item.setPos(250, 50)
        ellipse_item.setBrush(QBrush(Qt.green))
        ellipse_item.setPen(QPen(Qt.darkGreen, 2))
        ellipse_item.setFlag(QGraphicsEllipseItem.ItemIsMovable, True)
        ellipse_item.setFlag(QGraphicsEllipseItem.ItemIsSelectable, True)

        # --- 控制堆叠顺序：通过 Z 值确保椭圆在矩形之上 ---
        ellipse_item.setZValue(1)  # Z值越大，显示在越上层[citation:8]
        rect_item.setZValue(0)

        # 再添加一个无法移动和选中的文本项，作为静态背景元素
        text_item = self.scene.addText("Hello, Graphics View!")
        text_item.setPos(100, 200)
        text_item.setDefaultTextColor(Qt.red)
        # 文本项默认不可移动，这里保持默认设置

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())