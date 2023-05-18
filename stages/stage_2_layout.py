from PyQt6.QtWidgets import QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtCore import pyqtSignal


from custom_text_edit import CustomTextEdit
from code_evaluator import CodeEvaluator

class Stage2Layout(QWidget):

    back_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.stageNumber = 2
        self.stage_answer = "Bloobz a toi camarade, si tu n'es pas originaire de la planete de tes geoliers, tu as surement besoin d'aide. J'ai moi meme ete enferme ici par le passe et j'ai decouvert comment sortir de ce laboratoire humain. Je vais donc t'indiquer les etapes a suivre: tout d'abord, garde en tete que tu vas devoir collecter quatre morceaux d'une carte qui va etre necessaire pour la derniere etape de ton evasion. Maintenant tu devras decrypter un mot de passe numerique pour passer la premiere zone, ensuite tu trouveras un code morse; mais ne t'inquiete pas j'ai laisse une note avec pour t'aider a le decoder. Et enfin tu devras franchir la porte finale avec la carte dont tu auras rassemble les fragments. Et voila, tu seras libre ainsi et ne traine pas avant de te faire capturer de nouveau !"

    def init_ui(self):
        # Créer le label d'en-tête du niveau 2
        headerLabel = QLabel("Stage 2")
        headerFont = QFont("Arial", 20, QFont.Weight.Bold)
        headerLabel.setFont(headerFont)

        # Créer le label d'instruction du niveau 2
        instructionLabel = QLabel("Le message suivant est crypté par un code céasar. Déchiffrez le message.")
        instructionLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Texte à décoder
        textToDecode = "Nxaanl m fau omymdmpq, eu fg z'qe bme adusuzmudq pq xm bxmzqfq pq fqe sqaxuqde, fg me egdqyqzf nqeauz p'mupq. V'mu yau yqyq qfq qzrqdyq uou bmd xq bmeeq qf v'mu pqoaghqdf oayyqzf eadfud pq oq xmnadmfaudq tgymuz. Vq hmue pazo f'uzpucgqd xqe qfmbqe m eguhdq: fagf p'mnadp, smdpq qz fqfq cgq fg hme pqhaud oaxxqofqd cgmfdq yadoqmgj p'gzq omdfq cgu hm qfdq zqoqeemudq bagd xm pqdzuqdq qfmbq pq faz qhmeuaz. Ymuzfqzmzf fg pqhdme pqodkbfqd gz yaf pq bmeeq zgyqducgq bagd bmeeqd xm bdqyuqdq lazq, qzegufq fg fdaghqdme gz oapq yadeq; ymue zq f'uzcguqfq bme v'mu xmueeq gzq zafq mhqo bagd f'mupqd m xq pqoapqd. Qf qzruz fg pqhdme rdmzotud xm badfq ruzmxq mhqo xm omdfq pazf fg mgdme dmeeqynxq xqe rdmsyqzfe. Qf hauxm, fg eqdme xundq muzeu qf zq fdmuzq bme mhmzf pq fq rmudq ombfgdqd pq zaghqmg !"
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



