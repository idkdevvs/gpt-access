from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QStackedWidget, QLabel, QMessageBox
from PyQt6.QtCore import pyqtSignal

from stages.stage_1_layout import Stage1Layout
from stages.stage_2_layout import Stage2Layout
from stages.stage_3_layout import Stage3Layout
from stages.stage_4_layout import Stage4Layout
from stages.stage_5_layout import Stage5Layout
from stages.stage_6_layout import Stage6Layout
from stages.stage_7_layout import Stage7Layout
from stages.stage_8_layout import Stage8Layout
from stages.stage_9_layout import Stage9Layout

class StageWidget(QWidget):
    back_to_stages_list = pyqtSignal()

    def __init__(self):
        super().__init__()

    def load_stage_layout(self, stage_number):
        # Dictionnaire des numéros des niveaux à leurs classes layout correspondantes
        stage_layout_classes = {
            1: Stage1Layout,
            2: Stage2Layout,
            3: Stage3Layout,
            4: Stage4Layout,
            5: Stage5Layout,
            6: Stage6Layout,
            7: Stage7Layout,
            8: Stage8Layout,
            9: Stage9Layout
        }

        # Instancier le layout
        stage_layout_class = stage_layout_classes.get(stage_number)
        if stage_layout_class is not None:
            stage_layout = stage_layout_class()
            stage_layout.backButton.clicked.connect(self.back_button_clicked)

            # Defini le layout
            layout = stage_layout.layout()
            self.setLayout(layout)
        else:
            QMessageBox.warning(self, "Erreur", f"Stage {stage_number} inexistant.")

    def back_button_clicked(self):
        # Supprime le layout actuel et le widget s'il y en a
        if self.layout() is not None:
            while self.layout().count():
                item = self.layout().takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
            self.layout().deleteLater()

        self.back_to_stages_list.emit()
