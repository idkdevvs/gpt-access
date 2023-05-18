from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal

from game_state import GameState

class StagesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.stage_buttons = {} 
        self.init_ui()
        self.game_state = GameState()
        self.update_stage_buttons()

    

    def init_ui(self):
        # Créer le label de l'en-tête
        self.headerLabel = QLabel("Stages :")

        # Créer une police pour le label de l'en-tête
        headerFont = QFont("Arial", 20, QFont.Weight.Bold)
        self.headerLabel.setFont(headerFont)

        # Créer une QVBoxLayout pour le label de l'en-tête
        headerLayout = QVBoxLayout()
        headerLayout.addWidget(self.headerLabel)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        headerLayout.addItem(spacerItem)


        # Créer un QGridLayout pour afficher les boutons de scène
        stagesLayout = QGridLayout()


        # Ajouter des boutons d'étape à la grille
        for i in range(1, 10):
            stageButton = QPushButton(f'Stage {i}')
            stageButton.setFixedSize(200, 50)
            self.stage_buttons[i] = stageButton
            row = (i - 1) // 3
            col = (i - 1) % 3
            stagesLayout.addWidget(stageButton, row, col)

            # Connecter le bouton à l'étape correspondante à l'aide d'une fonction lambda
            stageButton.clicked.connect(lambda _, stage_number=i: self.emit_stage_signal(stage_number))

        # Ajoute un bouton pour retourner au menu
        self.backButton = QPushButton("Back to main menu")

        # Créer la présentation principale QVBoxLayout et ajouter les présentations d'en-tête et de scène
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(headerLayout)
        mainLayout.addLayout(stagesLayout)
        mainLayout.addStretch(1)
        mainLayout.addWidget(self.backButton)

        # Définir le layout principal comme le layout de ce widget
        self.setLayout(mainLayout)

    # Définir un signal à émettre lorsqu'un bouton de l'étape est cliqué
    stage_signal = pyqtSignal(int)

    def emit_stage_signal(self, stage_number):
        # Émettre le signal d'étape
        self.stage_signal.emit(stage_number)

    def update_stage_buttons(self):
        game_state = GameState()
        for stage_number, button in self.stage_buttons.items():
            if game_state.is_stage_completed(stage_number):
                button.setEnabled(False)
