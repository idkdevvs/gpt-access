from PyQt6.QtWidgets import QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout, QWidget, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal

from custom_text_edit import CustomTextEdit
from code_evaluator import CodeEvaluator

class Stage3Layout(QWidget):

    back_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.code_evaluator = CodeEvaluator()
        self.stageNumber = 3
        self.stage_answer = "287"
        self.init_ui()
        
    def init_ui(self):
        save_csv_button = QPushButton("Récupérer les fichier")

        save_csv_button.clicked.connect(self.code_evaluator.save_csv)
        save_csv_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        save_csv_button.setFixedWidth(150)
        save_csv_button.setFixedHeight(50)
 

        # Créer le label d'en-tête du niveau 3
        headerLabel = QLabel("Stage 3")
        headerFont = QFont("Arial", 20, QFont.Weight.Bold)
        headerLabel.setFont(headerFont)

        # Créer le label d'instruction du niveau 3
        instructionLabel = QLabel("Vous trouvez un premier document intitulé Tokotoro qui semble indiquer une image à déchiffrer.")
        instructionLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        instructionLabel.setWordWrap(True)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Consigne
        textToDecode = "Trouvez comment afficher l'image et entrez ce qui est révélé."
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
        mainLayout.addWidget(save_csv_button)
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
            msg_box.setText("Félicitations! Vous avez réussi à résoudre cette étape et avez débloqué un fragment de carte !")
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg_box.setText("Désolé, ce n'est pas la bonne réponse. Essayez à nouveau!")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def reset_code_editor(self, code_editor, default_function):
        # Réinitialiser le contenu de l'éditeur de code à la fonction par défaut
        code_editor.setPlainText(default_function)

