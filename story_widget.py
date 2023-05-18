# widget pyqt6 de base pour l'histoire

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class StoryWidget(QWidget):


    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Création layout vertical
        self.vLayout = QVBoxLayout()

        # Label pour grand titre
        self.titleLabel = QLabel("Histoire")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleFont = QFont("Arial", 20, QFont.Weight.Bold)
        self.titleLabel.setFont(titleFont)

        # Label pour le texte de l'histoire
        self.storyLabel = QLabel("Il s'agit d'un récit qui met en scène un extraterrestre capturé par des scientifiques. Pour parvenir à s'échapper, cet être doit créer du code informatique et récupérer quatre morceaux d'une carte qui lui permettront de rentrer chez lui à bord de son vaisseau spatial. Ces fragments sont dispersés dans quatre des neuf niveaux que le joueur devra traverser pour compléter le jeu. Ainsi, pour achever sa quête, le joueur devra collecter les quatre fragments et les utiliser pour résoudre le neuvième niveau.")
        self.storyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        storyFont = QFont("Arial", 16)
        self.storyLabel.setWordWrap(True)
        self.storyLabel.setFont(storyFont)

        # Bouton pour retourner au menu
        self.backButton = QPushButton("Retour")
        self.backButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.backButton.setFixedWidth(100)
        self.backButton.setFixedHeight(50)

        # Ajouter le label au layout
        self.vLayout.addWidget(self.titleLabel)
        self.vLayout.addWidget(self.storyLabel)
        self.vLayout.addWidget(self.backButton)

        # Aligner le bouton à droite
        self.vLayout.setAlignment(self.backButton, Qt.AlignmentFlag.AlignRight)

        # Ajouter un espace entre les widgets
        self.vLayout.addStretch(1)


        # Définir le layout principal comme le layout de ce widget
        self.setLayout(self.vLayout)

