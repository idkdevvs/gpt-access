from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import Qt

class CustomTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Tab:
            # Insérer 4 espaces lorsque l'on appuie sur la touche Tab
            self.insertPlainText(' ' * 4)
        else:
            super().keyPressEvent(event)

