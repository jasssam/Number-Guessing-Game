from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QSizePolicy, QDesktopWidget


class Hint(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def initUI(self, hint):
        self.setWindowTitle("Hint")

        screen_size = QDesktopWidget().screenGeometry().size()

        dialog_width = screen_size.width() // 4
        dialog_height = screen_size.height() // 4

        dialog_x = (screen_size.width() - dialog_width) // 2
        dialog_y = (screen_size.height() - dialog_height) // 2

        self.setGeometry(dialog_x, dialog_y, dialog_width, dialog_height)

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 2)
        self.main_layout.setRowStretch(2, 2)
        self.main_layout.setRowStretch(3, 1)
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 3)
        self.main_layout.setColumnStretch(2, 1)

        self.hint_label = QLabel(hint, self)
        self.hint_label.setSizePolicy(size_policy)
        self.hint_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.hint_label, 1, 1)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.setSizePolicy(size_policy)
        self.ok_button.clicked.connect(self.close)
        self.main_layout.addWidget(self.ok_button, 2, 1)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.close()