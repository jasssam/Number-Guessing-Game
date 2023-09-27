from sys import argv, exit

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

from game import Game
from level_select import LevelSelect
from menu import Menu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def initUI(self):
        self.setStyleSheet("""
            * {
                font-size: 20px;
            }
        """)

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.active_pages = None

        self.pages = {
            "menu": Menu(self),
            "level_select": LevelSelect(self),
            "game": Game(self)
        }

        for page in self.pages.values():
            self.stacked_widget.addWidget(page)

        self.showFullScreen()
        self.openMenu()

    def openPage(self, page_name):
        page = self.pages.get(page_name)

        if self.active_pages:
            self.stacked_widget.setCurrentWidget(page)
        else:
            self.stacked_widget.setCurrentWidget(page)
            self.active_pages = page

    def openMenu(self):
        self.openPage("menu")
        self.pages["menu"].initUI()

    def openLevelSelect(self):
        self.openPage("level_select")
        self.pages["level_select"].initUI()

    def openGame(self, level):
        self.openPage("game")
        self.pages["game"].initUI(level)
        self.pages["game"].generateAnswer()

def main():
    app = QApplication(argv)
    window = MainWindow()
    window.initUI()
    exit(app.exec_())

if __name__ == "__main__":
    main()