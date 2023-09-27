from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton, QSizePolicy, QDesktopWidget


class GameMenu(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def initUI(self):
        self.setWindowTitle("Game Menu")

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
        self.main_layout.setRowStretch(3, 2)
        self.main_layout.setRowStretch(4, 2)
        self.main_layout.setRowStretch(5, 1)
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 3)
        self.main_layout.setColumnStretch(2, 1)

        self.game_menu_label = QLabel("Game Menu", self)
        self.game_menu_label.setSizePolicy(size_policy)
        self.game_menu_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.game_menu_label, 1, 1)
        
        self.restart_button = QPushButton("Restart", self)
        self.restart_button.setSizePolicy(size_policy)
        self.restart_button.setCursor(Qt.PointingHandCursor)
        self.restart_button.clicked.connect(self.handleRestart)
        self.main_layout.addWidget(self.restart_button, 2, 1)
        
        self.change_level_button = QPushButton("Change level", self)
        self.change_level_button.setSizePolicy(size_policy)
        self.change_level_button.setCursor(Qt.PointingHandCursor)
        self.change_level_button.clicked.connect(self.handleLevelSelect)
        self.main_layout.addWidget(self.change_level_button, 3, 1)
        
        self.back_menu = QPushButton("Back to menu", self)
        self.back_menu.setSizePolicy(size_policy)
        self.back_menu.setCursor(Qt.PointingHandCursor)
        self.back_menu.clicked.connect(self.handleGoToMenu)
        self.main_layout.addWidget(self.back_menu, 4, 1)

        self.setFocus()

    def handleRestart(self):
        self.parent.handleRestart()
        self.close()

    def handleLevelSelect(self):
        self.parent.handleLevelSelect()
        self.close()

    def handleGoToMenu(self):
        self.parent.goToMenu()
        self.close()

    def keyPressEvent(self, event: QKeyEvent):
        pass