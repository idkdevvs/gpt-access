from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MyMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Créer un layout vertical
        self.vLayout = QVBoxLayout()

        # Créer un layout horizontal pour le titre
        self.hLayoutTitle = QHBoxLayout()

        # Créer un autre layout vertical pour les boutons
        self.vLayoutButtons = QVBoxLayout()

        # Créer un label pour le titre
        self.titleLabel = QLabel("Alien Escape: Rocket Quest")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        menuFont = QFont("Arial", 20, QFont.Weight.Bold)
        self.titleLabel.setFont(menuFont)

        # Ajouter le label du titre au layout horizontal
        self.hLayoutTitle.addWidget(self.titleLabel)

        # Création des boutons
        self.stagesButton = QPushButton("Stages")
        self.stagesButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.storyButton = QPushButton("Histoire")
        self.storyButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.unlockedImagesButton = QPushButton("Fragments de carte débloqués")
        self.unlockedImagesButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.exitButton = QPushButton("Quitter")
        self.exitButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        # Ajouter les boutons au layout vertical
        self.vLayoutButtons.addWidget(self.stagesButton)
        self.vLayoutButtons.addWidget(self.storyButton)
        self.vLayoutButtons.addWidget(self.unlockedImagesButton)
        self.vLayoutButtons.addWidget(self.exitButton) 

        # Ajouter le layout horizontal et le layout vertical au layout vertical principal
        self.vLayout.addLayout(self.hLayoutTitle)
        self.vLayout.addLayout(self.vLayoutButtons)

        # Définir le layout vertical principal comme le layout de ce widget
        self.setLayout(self.vLayout)


