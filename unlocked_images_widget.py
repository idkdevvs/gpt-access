from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy, QPushButton, QSpacerItem, QFileDialog, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PIL import Image
# Import de functools car lambda pose problème avec l'index i
from functools import partial

from game_state import GameState
class UnlockedImagesWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.game_state = GameState()
        self.init_ui()

    def init_ui(self):
        # Creation layout vertical
        self.vLayout = QVBoxLayout()
        
        # Label pour grand titre
        self.titleLabel = QLabel("Images débloquées")
        menuFont = QFont("Arial", 20, QFont.Weight.Bold)
        self.titleLabel.setFont(menuFont)

        # Label explicatif
        self.explanationLabel = QLabel("Vous débloquerez des images tout au long des puzzles. Les 4 images, une fois débloquées, vous dévoileront un code secret.")

        # Créé une liste pour stocker les bontons image
        self.imageButtons = []

        # Créé les 4 boutons image et les ajoute à la liste
        for i in range(4):
            button = QPushButton("Image " + str(i + 1))
            button.clicked.connect(partial(self.display_image, i+1))
            button.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
            if not self.game_state.is_image_unlocked(i):
                button.setEnabled(False)
                
            button.setFont(QFont("Arial", 15, QFont.Weight.Bold))
            self.imageButtons.append(button)

        self.downloadImagesButton = QPushButton("Télécharger les images")
        self.downloadImagesButton.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        self.downloadImagesButton.setEnabled(False)
        self.downloadImagesButton.clicked.connect(self.download_images)
        # Bouton pour retourner au menu
        self.backButton = QPushButton("Retour")

        # Ajouter le label au layout
        self.vLayout.addWidget(self.titleLabel)
        self.vLayout.addWidget(self.explanationLabel)

        # Ajoute les boutons d'image au layout
        
        for button in self.imageButtons:
            self.vLayout.addItem(QSpacerItem(10, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
            self.vLayout.addWidget(button)
        # Ajoute le bouton pour télécharger les images
        self.vLayout.addWidget(self.downloadImagesButton)

        self.vLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.vLayout.addWidget(self.backButton)

        # Définir le layout principal
        self.setLayout(self.vLayout)


    def update_game_state(self):
        self.game_state = GameState()
        self.update_buttons()

    def update_buttons(self):
        unlockedImagesCount = 0
        for i in range(len(self.imageButtons)):
            if self.game_state.is_image_unlocked(i+1):
                unlockedImagesCount += 1
                self.imageButtons[i].setEnabled(True)
                self.imageButtons[i].setText(f"Image {i + 1}")
            else:
                self.imageButtons[i].setEnabled(False)
                self.imageButtons[i].setText("Débloquez le fragment avant d'accéder à l'image")

        # verifie si toutes les images sont débloqués et dans ce cas active le bouton de téléchargement
        if unlockedImagesCount == 4:
            self.downloadImagesButton.setEnabled(True)
        else:
            self.downloadImagesButton.setEnabled(False)

    def display_image(self, image_number):
        image = Image.open(f"images/Carte{image_number}.jpg")
        image.show()

    def download_images(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Information")
        msg_box.setText("Un dossier de destination va s'ouvrir. Veuillez choisir un dossier de destination pour les images. Ces 4 images doivent être téléchargées afin de compléter le stage 9.")
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
        cardNames = ["Tokorico", "Tokopiyon", "Tokotoro", "Tokopisco"]
        # Ouvre le fichier
        folder = QFileDialog.getExistingDirectory(self, "Choisissez un dossier de destination pour les images")
        if folder:
            for i in range(4):
                image = Image.open(f"images/Carte{i+1}.jpg")
                image.save(f"{folder}/Carte{cardNames[i]}.jpg")
