import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QListWidget, QLineEdit, QListWidgetItem
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(300, 300, 350, 400)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)

        self.todo_list = QListWidget()
        self.todo_list.setFont(QFont("Arial", 12))
        self.todo_list.setStyleSheet("background-color: #2d2d2d; color: white;")
        self.layout.addWidget(self.todo_list)

        self.new_task_input = QLineEdit()
        self.new_task_input.setPlaceholderText("Nueva tarea")
        self.new_task_input.setFont(QFont("Arial", 12))
        self.new_task_input.setStyleSheet("background-color: #333; color: white")
        self.new_task_input.textChanged.connect(self.update_buttons)
        self.layout.addWidget(self.new_task_input)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setSpacing(10)

        self.add_task_button = QPushButton("Agregar")
        self.add_task_button.setStyleSheet("background-color: #4CAF50; color: white")
        self.add_task_button.clicked.connect(self.add_task)
        self.add_task_button.setEnabled(False)
        self.buttons_layout.addWidget(self.add_task_button)

        self.mark_done_button = QPushButton("Marcar como completada")
        self.mark_done_button.setStyleSheet("background-color: #2196F3; color: white")
        self.mark_done_button.clicked.connect(self.mark_task_done)
        self.mark_done_button.setEnabled(False)
        self.buttons_layout.addWidget(self.mark_done_button)

        self.delete_task_button = QPushButton("Eliminar")
        self.delete_task_button.setStyleSheet("background-color: #f44336; color: white")
        self.delete_task_button.clicked.connect(self.delete_task)
        self.delete_task_button.setEnabled(False)
        self.buttons_layout.addWidget(self.delete_task_button)

        self.layout.addLayout(self.buttons_layout)

    def add_task(self):
        task_text = self.new_task_input.text()
        if task_text:
            task_item = QListWidgetItem(task_text)
            task_item.setFont(QFont("Arial", 12))
            self.todo_list.addItem(task_item)
            self.new_task_input.clear()

    def mark_task_done(self):
        for item in self.todo_list.selectedItems():
            if not item.text().endswith(" ✓"):
                item.setText(f"{item.text()} ✓")
                item.setForeground(Qt.gray)
                font = item.font()
                font.setStrikeOut(True)
                item.setFont(font)

    def delete_task(self):
        for item in self.todo_list.selectedItems():
            self.todo_list.takeItem(self.todo_list.row(item))

    def update_buttons(self):
        text = self.new_task_input.text()
        has_selection = bool(self.todo_list.selectedItems())
        self.add_task_button.setEnabled(bool(text))
        self.mark_done_button.setEnabled(has_selection)
        self.delete_task_button.setEnabled(has_selection)


def main():
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()



