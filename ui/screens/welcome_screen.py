from PySide6.QtCore import Qt
from PySide6.QtGui import QLinearGradient, QPainter, QColor, QBrush, QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFrame,
    QGraphicsDropShadowEffect,
)


class GradientBackground(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0.0, QColor("#030712"))
        gradient.setColorAt(0.35, QColor("#06142B"))
        gradient.setColorAt(0.7, QColor("#0A2342"))
        gradient.setColorAt(1.0, QColor("#07111F"))

        painter.fillRect(self.rect(), QBrush(gradient))


class WelcomeScreen(GradientBackground):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QWidget {
                color: white;
                font-family: 'Segoe UI';
            }

            QFrame#mainCard {
                background-color: rgba(7, 18, 35, 215);
                border: 1px solid rgba(85, 180, 255, 45);
                border-radius: 28px;
            }

            QLabel#titleLabel {
                color: white;
                font-size: 50px;
                font-weight: 800;
            }

            QLabel#accentLabel {
                color: #35C2FF;
                font-size: 50px;
                font-weight: 800;
            }

            QLabel#subtitleLabel {
                color: #D9E7F5;
                font-size: 22px;
                font-weight: 400;
            }

            QPushButton#nextButton {
                background-color: #2EA8F2;
                color: white;
                border: none;
                border-radius: 18px;
                padding: 16px 34px;
                font-size: 18px;
                font-weight: 700;
                min-width: 210px;
            }

            QPushButton#nextButton:hover {
                background-color: #49B8FF;
            }

            QPushButton#nextButton:pressed {
                background-color: #188ED4;
            }
        """)

        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(80, 50, 80, 50)
        outer_layout.setAlignment(Qt.AlignCenter)

        card = QFrame()
        card.setObjectName("mainCard")
        card.setMaximumWidth(820)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 12)
        shadow.setColor(QColor(0, 0, 0, 170))
        card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(65, 60, 65, 60)
        card_layout.setSpacing(18)
        card_layout.setAlignment(Qt.AlignCenter)

        logo_label = QLabel()
        pixmap = QPixmap("ui/assets/logo_autozap.png")

        if not pixmap.isNull():
            logo_label.setPixmap(pixmap.scaledToWidth(420, Qt.SmoothTransformation))
        else:
            logo_label.setText("AutoZap")
            logo_label.setStyleSheet("font-size: 40px; font-weight: 800; color: #53d1ff;")

        logo_label.setAlignment(Qt.AlignCenter)

        title_label = QLabel("Bem-vindo à")
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignCenter)

        accent_label = QLabel("AutoZap!")
        accent_label.setObjectName("accentLabel")
        accent_label.setAlignment(Qt.AlignCenter)

        subtitle_label = QLabel("Estamos felizes em ter você conosco.")
        subtitle_label.setObjectName("subtitleLabel")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setWordWrap(True)

        next_button = QPushButton("Próximo")
        next_button.setObjectName("nextButton")
        next_button.setCursor(Qt.PointingHandCursor)
        next_button.clicked.connect(self.go_next)

        card_layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        card_layout.addSpacing(6)
        card_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        card_layout.addWidget(accent_label, alignment=Qt.AlignCenter)
        card_layout.addSpacing(4)
        card_layout.addWidget(subtitle_label, alignment=Qt.AlignCenter)
        card_layout.addSpacing(18)
        card_layout.addWidget(next_button, alignment=Qt.AlignCenter)

        outer_layout.addWidget(card, alignment=Qt.AlignCenter)

    def go_next(self):
        self.main_window.go_to_setup_screen()