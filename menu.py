from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy

class Menu(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def initUI(self):
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 12)
        self.main_layout.setRowStretch(2, 8)
        self.main_layout.setRowStretch(3, 1)
        self.main_layout.setRowStretch(4, 8)
        self.main_layout.setRowStretch(5, 1)
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 3)
        self.main_layout.setColumnStretch(2, 1)

        self.title_label = QLabel("Guess the Number!", self)
        self.title_label.setSizePolicy(size_policy)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label, 1, 1)
        
        self.start_button = QPushButton("Start", self)
        self.start_button.setSizePolicy(size_policy)
        self.start_button.setCursor(Qt.PointingHandCursor)
        self.start_button.clicked.connect(self.handleStart)
        self.main_layout.addWidget(self.start_button, 2, 1)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setSizePolicy(size_policy)
        self.exit_button.setCursor(Qt.PointingHandCursor)
        self.exit_button.clicked.connect(QApplication.quit)
        self.main_layout.addWidget(self.exit_button, 4, 1)

        self.setFocus()

    def handleStart(self):
        self.parent.openLevelSelect()
