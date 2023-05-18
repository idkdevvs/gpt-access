from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget

from menu_widget import MyMenuWidget
from stages_widget import StagesWidget
from stage_widget import StageWidget
from story_widget import StoryWidget
from unlocked_images_widget import UnlockedImagesWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Définition du titre et de la taille de la fenêtre
        self.setWindowTitle('Alien Escape: Rocket Quest')
        self.setGeometry(100, 100, 800, 600)

        # Créer une interface pour les widgets personnalisés
        self.myMenuWidget = MyMenuWidget()
        self.stagesWidget = StagesWidget()
        self.storyWidget = StoryWidget()
        self.stageWidget = StageWidget()
        self.unlockedImagesWidget = UnlockedImagesWidget()

        # Mise en place d'un widget empilé pour gérer les différentes vues (menu, étapes, et étape individuelle)
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.myMenuWidget)
        self.stackedWidget.addWidget(self.stagesWidget)
        self.stackedWidget.addWidget(self.storyWidget)
        self.stackedWidget.addWidget(self.stageWidget)
        self.stackedWidget.addWidget(self.unlockedImagesWidget)

        # Définir le widget empilé comme widget central
        self.setCentralWidget(self.stackedWidget)

        # Connecter les boutons retour aux vues appropriées
        self.storyWidget.backButton.clicked.connect(self.show_main_menu)
        self.stageWidget.back_to_stages_list.connect(self.show_stages_list)
        self.stagesWidget.backButton.clicked.connect(self.show_main_menu)
        self.unlockedImagesWidget.backButton.clicked.connect(self.show_main_menu)


        # Connecter les signaux et les slots pour passer d'une vue à l'autre
        self.myMenuWidget.stagesButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.stagesWidget))
        self.stagesWidget.stage_signal.connect(self.show_stage_widget)
        self.myMenuWidget.storyButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.storyWidget))
        self.myMenuWidget.unlockedImagesButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.unlockedImagesWidget))
        self.myMenuWidget.unlockedImagesButton.clicked.connect(self.unlockedImagesWidget.update_game_state)
        self.myMenuWidget.exitButton.clicked.connect(self.close)

    def show_stage_widget(self, stage_number):
        # Charger la disposition d'étape appropriée pour le numéro d'étape donné
        self.stageWidget.load_stage_layout(stage_number)
        # Définir le widget de la scène comme widget courant dans le widge empilét
        self.stackedWidget.setCurrentWidget(self.stageWidget)

    def show_stages_list(self):
        # Appeler la méthode update_stage_buttons pour mettre à jour les boutons de scène
        self.stagesWidget.update_stage_buttons()

        self.stackedWidget.setCurrentWidget(self.stagesWidget)

    def show_main_menu(self):
        self.stackedWidget.setCurrentWidget(self.myMenuWidget)
