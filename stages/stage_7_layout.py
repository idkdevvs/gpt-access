from PyQt6.QtWidgets import QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout, QWidget, QMessageBox, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal


from custom_text_edit import CustomTextEdit
from code_evaluator import CodeEvaluator

class Stage7Layout(QWidget):

    back_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.stageNumber = 7
        self.stage_answer = "549"
        self.code_evaluator = CodeEvaluator()
        self.init_ui()

    def init_ui(self):
        save_csv_button = QPushButton("Récupérer les fichier")


        save_csv_button.clicked.connect(self.code_evaluator.save_csv)
        save_csv_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        save_csv_button.setFixedWidth(150)
        save_csv_button.setFixedHeight(50)
    
        # Créer le label d'en-tête du niveau 7
        headerLabel = QLabel("Stage 7")
        headerFont = QFont("Arial", 20, QFont.Weight.Bold)
        headerLabel.setFont(headerFont)

        # Créer le label d'instruction du niveau 7
        instructionLabel = QLabel("Voilà un 3e morceau de carte intitulé Tokorico qui devant vous qui attends d'être déchiffré.")
        instructionLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Consigne
        textToDecode = "Entrez le code révélé par l'image."
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
            msg_box.setText("Félicitations! Vous avez réussi à résoudre cette étapeet avez débloqué un fragment de carte !")
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

