import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QGraphicsView, 
                               QGraphicsScene, QGraphicsRectItem, 
                               QGraphicsEllipseItem, QGraphicsTextItem,
                               QGraphicsLineItem, QVBoxLayout, QWidget,
                               QPushButton, QHBoxLayout)
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPen, QBrush, QColor, QFont


class GraphicsDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGraphicsScene & QGraphicsView 实例")
        self.setGeometry(100, 100, 800, 600)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # ========== 1. 创建场景 (Scene) ==========
        self.scene = QGraphicsScene()
        # 设置场景坐标范围 (x, y, width, height)
        self.scene.setSceneRect(0, 0, 600, 400)
        
        # ========== 2. 创建视图 (View) ==========
        self.view = QGraphicsView(self.scene)
        # 设置渲染提示：抗锯齿
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        # 设置拖拽模式：滚轮缩放，鼠标拖拽
        self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        # 设置背景颜色
        self.view.setBackgroundBrush(QBrush(QColor(240, 240, 240)))
        
        layout.addWidget(self.view)
        
        # ========== 3. 控制按钮 ==========
        btn_layout = QHBoxLayout()
        
        btn_add_rect = QPushButton("添加矩形")
        btn_add_rect.clicked.connect(self.add_rectangle)
        
        btn_add_circle = QPushButton("添加圆形")
        btn_add_circle.clicked.connect(self.add_circle)
        
        btn_add_text = QPushButton("添加文字")
        btn_add_text.clicked.connect(self.add_text)
        
        btn_clear = QPushButton("清空场景")
        btn_clear.clicked.connect(self.clear_scene)
        
        btn_zoom_in = QPushButton("放大")
        btn_zoom_in.clicked.connect(self.zoom_in)
        
        btn_zoom_out = QPushButton("缩小")
        btn_zoom_out.clicked.connect(self.zoom_out)
        
        btn_layout.addWidget(btn_add_rect)
        btn_layout.addWidget(btn_add_circle)
        btn_layout.addWidget(btn_add_text)
        btn_layout.addWidget(btn_clear)
        btn_layout.addWidget(btn_zoom_in)
        btn_layout.addWidget(btn_zoom_out)
        layout.addLayout(btn_layout)
        
        # 初始化添加一些图形
        self.init_scene()
    
    def init_scene(self):
        """初始化场景，添加基础图形"""
        # 添加坐标轴线
        pen = QPen(Qt.GlobalColor.black, 1, Qt.PenStyle.DashLine)
        self.scene.addLine(0, 200, 600, 200, pen)  # X轴
        self.scene.addLine(300, 0, 300, 400, pen)  # Y轴
        
        # 添加中心矩形
        rect = QGraphicsRectItem(QRectF(250, 150, 100, 100))
        rect.setBrush(QBrush(QColor(100, 150, 255)))
        rect.setPen(QPen(Qt.GlobalColor.darkBlue, 2))
        # 设置可移动、可选择
        rect.setFlags(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable |
                     QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable)
        self.scene.addItem(rect)
        
        # 添加说明文字
        text = QGraphicsTextItem("点击按钮添加图形\n拖拽可移动\n滚轮可缩放")
        text.setPos(10, 10)
        text.setFont(QFont("Microsoft YaHei", 12))
        self.scene.addItem(text)
    
    def add_rectangle(self):
        """添加随机矩形"""
        import random
        x = random.randint(50, 500)
        y = random.randint(50, 300)
        
        rect = QGraphicsRectItem(QRectF(x, y, 80, 60))
        color = QColor(random.randint(0, 255), 
                      random.randint(0, 255), 
                      random.randint(0, 255))
        rect.setBrush(QBrush(color))
        rect.setPen(QPen(Qt.GlobalColor.black, 1))
        rect.setFlags(QGraphicsRectItem.GraphicsItemFlag.ItemIsMovable |
                     QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable)
        self.scene.addItem(rect)
    
    def add_circle(self):
        """添加圆形"""
        import random
        x = random.randint(50, 500)
        y = random.randint(50, 300)
        
        ellipse = QGraphicsEllipseItem(QRectF(x, y, 80, 80))
        color = QColor(random.randint(0, 255), 
                      random.randint(0, 255), 
                      random.randint(0, 255))
        ellipse.setBrush(QBrush(color))
        ellipse.setPen(QPen(Qt.GlobalColor.black, 1))
        ellipse.setFlags(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable |
                        QGraphicsEllipseItem.GraphicsItemFlag.ItemIsSelectable)
        self.scene.addItem(ellipse)
    
    def add_text(self):
        """添加文字"""
        import random
        x = random.randint(50, 500)
        y = random.randint(50, 300)
        
        text = QGraphicsTextItem(f"文本 {random.randint(1, 100)}")
        text.setPos(x, y)
        text.setFont(QFont("Microsoft YaHei", 14))
        text.setDefaultTextColor(QColor(random.randint(0, 255), 
                                       random.randint(0, 255), 
                                       random.randint(0, 255)))
        text.setFlags(QGraphicsTextItem.GraphicsItemFlag.ItemIsMovable |
                     QGraphicsTextItem.GraphicsItemFlag.ItemIsSelectable)
        self.scene.addItem(text)
    
    def clear_scene(self):
        """清空场景"""
        self.scene.clear()
        self.init_scene()  # 重新添加坐标轴
    
    def zoom_in(self):
        """放大视图"""
        self.view.scale(1.2, 1.2)
    
    def zoom_out(self):
        """缩小视图"""
        self.view.scale(0.8, 0.8)


if __name__ == "__main__":
    from PySide6.QtGui import QPainter
    app = QApplication(sys.argv)
    window = GraphicsDemo()
    window.show()
    sys.exit(app.exec())