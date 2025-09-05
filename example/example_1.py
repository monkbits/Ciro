import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QLabel, QVBoxLayout
)
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap, QPainter


class DragDropList(QListWidget):
    def __init__(self, title, color):
        super().__init__()
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setStyleSheet(f"""
            QListWidget {{
                background-color: {color};
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                color: white;
            }}
            QListWidget::item {{
                padding: 8px;
                margin: 4px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 4px;
            }}
            QListWidget::item:selected {{
                background: rgba(255, 255, 255, 0.3);
            }}
        """)

        # Title above list
        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("font-weight: bold; font-size: 16px; color: white;")

    def widgetWithTitle(self):
        box = QWidget()
        layout = QVBoxLayout(box)
        layout.addWidget(self.title)
        layout.addWidget(self)
        return box

    def startDrag(self, supportedActions):
        """Customize the drag pixmap (floating look)"""
        item = self.currentItem()
        if not item:
            return

        drag = QDrag(self)
        mime = QMimeData()
        mime.setText(item.text())
        drag.setMimeData(mime)

        # Create a pixmap preview
        pixmap = QPixmap(150, 30)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        painter.setPen(Qt.white)
        painter.setBrush(Qt.darkGray)
        painter.drawRoundedRect(0, 0, 150, 30, 6, 6)
        painter.drawText(pixmap.rect(), Qt.AlignCenter, item.text())
        painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(pixmap.rect().center())

        # Execute drag
        if drag.exec_(Qt.MoveAction) == Qt.MoveAction:
            self.takeItem(self.row(item))  # remove from source list

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            self.addItem(QListWidgetItem(event.mimeData().text()))
            event.acceptProposedAction()


app = QApplication(sys.argv)
window = QWidget()
layout = QHBoxLayout(window)

# Three Kanban-style columns
todo = DragDropList("To Do", "#3B82F6")
in_progress = DragDropList("In Progress", "#F59E0B")
done = DragDropList("Done", "#10B981")

# Add initial tasks
for task in ["Buy groceries", "Finish report", "Go to gym", "Read book"]:
    todo.addItem(QListWidgetItem(task))

# Add to layout
layout.addWidget(todo.widgetWithTitle())
layout.addWidget(in_progress.widgetWithTitle())
layout.addWidget(done.widgetWithTitle())

window.setWindowTitle("Kanban Drag & Drop")
window.resize(700, 400)
window.show()

sys.exit(app.exec_())
