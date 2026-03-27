from PySide6.QtCore import Qt
from PySide6.QtGui import QLinearGradient, QPainter, QColor, QBrush
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QGraphicsDropShadowEffect,
    QSizePolicy
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


class StepCard(QFrame):
    def __init__(self, number, title, description):
        super().__init__()
        self.setObjectName("stepCard")
        self.setMinimumHeight(170)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 22, 28, 22)
        layout.setSpacing(10)

        number_label = QLabel(f"{number:02d}")
        number_label.setObjectName("numberLabel")

        title_label = QLabel(title)
        title_label.setObjectName("cardTitleLabel")
        title_label.setWordWrap(True)

        desc_label = QLabel(description)
        desc_label.setObjectName("cardDescLabel")
        desc_label.setWordWrap(True)

        layout.addWidget(number_label)
        layout.addWidget(title_label)
        layout.addWidget(desc_label)
        layout.addStretch()


class SetupScreen(GradientBackground):
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
                background-color: rgba(7, 18, 35, 218);
                border: 1px solid rgba(85, 180, 255, 45);
                border-radius: 28px;
            }

            QFrame#stepCard {
                background-color: rgba(12, 30, 56, 235);
                border: 1px solid rgba(95, 190, 255, 28);
                border-radius: 22px;
            }

            QLabel#titleLabel {
                color: white;
                font-size: 40px;
                font-weight: 800;
            }

            QLabel#subtitleLabel {
                color: #D8E5F2;
                font-size: 18px;
                font-weight: 400;
            }

            QLabel#numberLabel {
                color: #39C7FF;
                font-size: 28px;
                font-weight: 800;
            }

            QLabel#cardTitleLabel {
                color: white;
                font-size: 19px;
                font-weight: 700;
            }

            QLabel#cardDescLabel {
                color: #C9D7E6;
                font-size: 15px;
                font-weight: 400;
                line-height: 1.4em;
            }

            QPushButton#nextButton {
                background-color: #2EA8F2;
                color: white;
                border: none;
                border-radius: 18px;
                padding: 16px 34px;
                font-size: 18px;
                font-weight: 700;
                min-width: 220px;
            }

            QPushButton#nextButton:hover {
                background-color: #49B8FF;
            }

            QPushButton#nextButton:pressed {
                background-color: #188ED4;
            }
        """)

        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(60, 35, 60, 35)
        outer_layout.setAlignment(Qt.AlignCenter)

        card = QFrame()
        card.setObjectName("mainCard")
        card.setMaximumWidth(980)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(40)
        shadow.setOffset(0, 12)
        shadow.setColor(QColor(0, 0, 0, 170))
        card.setGraphicsEffect(shadow)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(60, 42, 60, 42)
        card_layout.setSpacing(26)

        title_label = QLabel("Como funciona a AutoZap")
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignCenter)

        subtitle_label = QLabel("Configure tudo em poucos passos e comece a automatizar seu atendimento.")
        subtitle_label.setObjectName("subtitleLabel")
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setWordWrap(True)

        grid = QGridLayout()
        grid.setHorizontalSpacing(20)
        grid.setVerticalSpacing(20)

        card1 = StepCard(
            1,
            "Escolha seu nicho",
            "Configure sua empresa e personalize o atendimento."
        )

        card2 = StepCard(
            2,
            "Ative sua licença",
            "Valide sua AutoZap e desbloqueie o sistema."
        )

        card3 = StepCard(
            3,
            "Conecte seu WhatsApp",
            "Escaneie o QR Code e conecte seu número."
        )

        card4 = StepCard(
            4,
            "Comece a usar",
            "Sua AutoZap estará pronta para atender."
        )

        grid.addWidget(card1, 0, 0)
        grid.addWidget(card2, 0, 1)
        grid.addWidget(card3, 1, 0)
        grid.addWidget(card4, 1, 1)

        next_button = QPushButton("Próximo")
        next_button.setObjectName("nextButton")
        next_button.setCursor(Qt.PointingHandCursor)
        next_button.clicked.connect(self.go_next)

        button_row = QHBoxLayout()
        button_row.setAlignment(Qt.AlignCenter)
        button_row.addWidget(next_button)

        card_layout.addWidget(title_label)
        card_layout.addWidget(subtitle_label)
        card_layout.addSpacing(4)
        card_layout.addLayout(grid)
        card_layout.addSpacing(8)
        card_layout.addLayout(button_row)

        outer_layout.addWidget(card, alignment=Qt.AlignCenter)

    def go_next(self):
        self.main_window.go_to_next_screen()