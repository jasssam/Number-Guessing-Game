from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent, QIntValidator
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy, QLineEdit

from game_menu import GameMenu
from hint import Hint


class Game(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    
    def initUI(self, level):
        self.level = level
        self.answer = None

        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.main_layout = QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 4)
        self.main_layout.setRowStretch(2, 1)
        self.main_layout.setRowStretch(3, 4)
        self.main_layout.setRowStretch(4, 1)
        self.main_layout.setRowStretch(5, 4)
        self.main_layout.setRowStretch(6, 1)
        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 18)
        self.main_layout.setColumnStretch(2, 1)

        self.guess_edit = QLineEdit(self)
        self.guess_edit.setPlaceholderText("Enter number")
        self.guess_edit.setSizePolicy(size_policy)
        self.guess_edit.setAlignment(Qt.AlignCenter)
        validator = QIntValidator()
        validator.setBottom(0)
        self.guess_edit.setValidator(validator)
        self.main_layout.addWidget(self.guess_edit, 1, 1)
        
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setSizePolicy(size_policy)
        self.submit_button.setCursor(Qt.PointingHandCursor)
        self.submit_button.clicked.connect(self.handleSubmit)
        self.main_layout.addWidget(self.submit_button, 3, 1)
        
        self.self_details_widget = QWidget(self)
        self.self_details_widget.setSizePolicy(size_policy)
        self.main_layout.addWidget(self.self_details_widget, 5, 1)

        self.self_details_layout = QGridLayout(self.self_details_widget)
        self.self_details_layout.setContentsMargins(0, 0, 0, 0)
        self.self_details_layout.setSpacing(0)
        self.self_details_layout.setRowStretch(0, 1)
        self.self_details_layout.setRowStretch(1, 1)
        self.self_details_layout.setColumnStretch(0, 6)
        self.self_details_layout.setColumnStretch(1, 1)
        self.self_details_layout.setColumnStretch(2, 6)
        self.self_details_layout.setColumnStretch(3, 1)
        self.self_details_layout.setColumnStretch(4, 6)

        self.life_label = QLabel("Life:", self.self_details_widget)
        self.life_label.setSizePolicy(size_policy)
        self.life_label.setAlignment(Qt.AlignCenter)
        self.self_details_layout.addWidget(self.life_label, 0, 0)
        
        self.score_label = QLabel("Score:", self.self_details_widget)
        self.score_label.setSizePolicy(size_policy)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.self_details_layout.addWidget(self.score_label, 0, 2)
        
        self.streak_label = QLabel("Streak:", self.self_details_widget)
        self.streak_label.setSizePolicy(size_policy)
        self.streak_label.setAlignment(Qt.AlignCenter)
        self.self_details_layout.addWidget(self.streak_label, 0, 4)
        
        self.life_edit = QLineEdit(self.self_details_widget)
        self.life_edit.setText("3")
        self.life_edit.setSizePolicy(size_policy)
        self.life_edit.setAlignment(Qt.AlignCenter)
        self.life_edit.setReadOnly(True)
        self.self_details_layout.addWidget(self.life_edit, 1, 0)
        
        self.score_edit = QLineEdit(self.self_details_widget)
        self.score_edit.setText("0")
        self.score_edit.setSizePolicy(size_policy)
        self.score_edit.setAlignment(Qt.AlignCenter)
        self.score_edit.setReadOnly(True)
        self.self_details_layout.addWidget(self.score_edit, 1, 2)
        
        self.streak_edit = QLineEdit(self.self_details_widget)
        self.streak_edit.setText("0")
        self.streak_edit.setSizePolicy(size_policy)
        self.streak_edit.setAlignment(Qt.AlignCenter)
        self.streak_edit.setReadOnly(True)
        self.self_details_layout.addWidget(self.streak_edit, 1, 4)

        self.setFocus()
        
    def handleSubmit(self):
        guess = self.guess_edit.text().strip()

        if guess:
            answer = self.answer
            guess = int(guess)

            if guess == answer:
                score = int(self.score_edit.text())
                new_score = score + 1
                self.score_edit.setText(str(new_score))

                streak = int(self.streak_edit.text())
                new_streak = streak + 1
                self.streak_edit.setText(str(new_streak))

                self.guess_edit.clear()
                self.generateAnswer()
            else:
                life = int(self.life_edit.text())
                new_life = life - 1
                self.life_edit.setText(str(new_life))

                if new_life == 0:
                    self.handleRestart()

                if guess > answer:
                    dialog = Hint(self)
                    dialog.initUI("Lower")
                    dialog.exec_()
                else:
                    dialog = Hint(self)
                    dialog.initUI("Higher")
                    dialog.exec_()

                self.guess_edit.clear()

    def generateAnswer(self):
        self.answer = randint(1, self.level)

    def handleRestart(self):
        self.generateAnswer()
        self.guess_edit.clear()
        self.life_edit.setText("3")
        self.score_edit.setText("0")
        self.streak_edit.setText("0")

    def handleLevelSelect(self):
        self.parent.openLevelSelect()

    def goToMenu(self):
        self.parent.openMenu()

    def showGameMenu(self):
        dialog = GameMenu(self)
        dialog.initUI()
        dialog.exec_()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.showGameMenu()
        elif event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.handleSubmit()