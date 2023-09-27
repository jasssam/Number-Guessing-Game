from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy


class LevelSelect(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

    def initUI(self):
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 2)
        self.main_layout.setRowStretch(2, 2)
        self.main_layout.setRowStretch(3, 2)
        self.main_layout.setRowStretch(4, 2)
        self.main_layout.setRowStretch(5, 1)
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 3)
        self.main_layout.setColumnStretch(2, 1)

        self.select_label = QLabel("Select level:", self)
        self.select_label.setSizePolicy(size_policy)
        self.select_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.select_label, 1, 1)

        self.easy_button = QPushButton("Easy", self)
        self.easy_button.setSizePolicy(size_policy)
        self.easy_button.setCursor(Qt.PointingHandCursor)
        self.easy_button.clicked.connect(lambda: self.handleSelect(5))
        self.main_layout.addWidget(self.easy_button, 2, 1)

        self.medium_button = QPushButton("Medium", self)
        self.medium_button.setSizePolicy(size_policy)
        self.medium_button.setCursor(Qt.PointingHandCursor)
        self.medium_button.clicked.connect(lambda: self.handleSelect(25))
        self.main_layout.addWidget(self.medium_button, 3, 1)

        self.hard_button = QPushButton("Hard", self)
        self.hard_button.setSizePolicy(size_policy)
        self.hard_button.setCursor(Qt.PointingHandCursor)
        self.hard_button.clicked.connect(lambda: self.handleSelect(125))
        self.main_layout.addWidget(self.hard_button, 4, 1)

        self.setFocus()

    def handleSelect(self, level):
        self.parent.openGame(level)