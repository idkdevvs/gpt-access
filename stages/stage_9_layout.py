from PyQt6.QtWidgets import QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal


from custom_text_edit import CustomTextEdit
from code_evaluator import CodeEvaluator

class Stage9Layout(QWidget):

    back_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.stageNumber = 9    
        self.stage_answer = "549436287190"

    def init_ui(self):
        # Créer le label d'en-tête du niveau 9
        headerLabel = QLabel("Stage 9")
        headerFont = QFont("Arial", 20, QFont.Weight.Bold)
        headerLabel.setFont(headerFont)

        # Créer le label d'instruction du niveau
        instructionLabel = QLabel("Une fois les 4 images acquises, assemblez les en 1.")
        instructionLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Consigne
        textToDecode = "Dans ce stage, vous devrez, une fois que vous aurez débloqués les 4 images, les assembler en une seule. Une fois cela fait, le code de démarrage du vaisseau vous sera révélé et vous pourrez embarquer. Attention, vous devrez mettre les images dans le bon ordre !"
        textToDecodeLabel = QLabel(textToDecode)
        textToDecodeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        textToDecodeLabel.setWordWrap(True)
        textToDecodeLabel.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)


        # Créer l'éditeur de code
        codeEditorLabel = QLabel("Ecrivez votre solution ici:")
        codeEditorLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        codeEditor = CustomTextEdit()

        # Créer le bouton d'envoi
        submitButton = QPushButton("Soumettre")
        submitButton.clicked.connect(lambda: self.on_code_submitted(codeEditor.toPlainText()))


        # Créer le bouton de retour au menu principal
        self.backButton = QPushButton("Retour à la liste des stages")
        self.backButton.clicked.connect(self.back_button_clicked.emit)

        # Créez le layout principal et ajoutez l'en-tête, l'instruction, l'éditeur de code et le bouton d'envoi
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(headerLabel)
        mainLayout.addWidget(instructionLabel)
        mainLayout.addWidget(textToDecodeLabel)
        mainLayout.addWidget(codeEditorLabel)
        mainLayout.addWidget(codeEditor)
        mainLayout.addWidget(submitButton)
        mainLayout.addWidget(self.backButton)

        # Définir le layout principal pour le Stage1Layout
        self.setLayout(mainLayout)

    def on_code_submitted(self, code):
        # Évaluer le code grâce à CodeEvaluator
        evaluator = CodeEvaluator()
        result = evaluator.evaluate(self.stageNumber, code, self.stage_answer)


        # Afficher une fenêtre avec un message en fonction du résultat de l'évaluation
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Résultat")
        if result == 1:  # Bonne réponse
            msg_box.setText("Félicitations! Vous avez réussi à résoudre cette étape.")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg_box.setText("Désolé, ce n'est pas la bonne réponse. Essayez à nouveau!")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()



