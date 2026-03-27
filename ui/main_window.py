from PySide6.QtWidgets import QMainWindow, QStackedWidget
from ui.screens.welcome_screen import WelcomeScreen
from ui.screens.setup_screen import SetupScreen


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AutoZap")
        self.setMinimumSize(1100, 700)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.welcome_screen = WelcomeScreen(self)
        self.setup_screen = SetupScreen(self)

        self.stack.addWidget(self.welcome_screen)
        self.stack.addWidget(self.setup_screen)

    def go_to_setup_screen(self):
        self.stack.setCurrentWidget(self.setup_screen)

    def go_to_next_screen(self):
        print("Ir para a próxima tela depois da explicação")