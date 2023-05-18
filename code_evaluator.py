import io
import sys
import shutil

# importe qfiledialogue de pyqt6
from PyQt6.QtWidgets import QFileDialog

from game_state import GameState

class CodeEvaluator:
    def __init__(self):
        self.game_state = GameState()

    def evaluate(self, stage_number, user_answer, stage_answer):
        self.stage_answer = stage_answer

        threshold = 0.9
        if self.are_similar(user_answer, self.stage_answer, threshold):
            self.game_state.complete_stage(stage_number)

            # débloque les images d'un niveau spécifique
            if stage_number == 3:
                self.game_state.unlock_image(3)
            elif stage_number == 5:
                self.game_state.unlock_image(4)
            elif stage_number == 7:
                self.game_state.unlock_image(1)
            elif stage_number == 8:
                self.game_state.unlock_image(2)

            return 1
        else:
            return 0
        

    # Ces fonctions calculent la similarité entre deux chaînes de caractères (En l'occurence, elles comparent la réponse de l'utilisateur avec la réponse attendue).

    def levenshtein_distance(self, str1, str2):
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        distances = range(len(str1) + 1)
        for index2, char2 in enumerate(str2):
            new_distances = [index2+1]
            for index1, char1 in enumerate(str1):
                if char1 == char2:
                    new_distances.append(distances[index1])
                else:
                    new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
            distances = new_distances
        return distances[-1]

    def levenshtein_similarity(self, str1, str2):
        distance = self.levenshtein_distance(str1.lower(), str2.lower())
        max_len = max(len(str1), len(str2))
        similarity = 1 - distance / max_len
        return similarity

    def are_similar(self, str1, str2, threshold):
        similarity = self.levenshtein_similarity(str1, str2)
        print(similarity)
        return similarity >= threshold


    def save_csv(self):
        folder = QFileDialog.getExistingDirectory(None, "Choisisez un dossier de destination")

        if folder:
            file_names = ["Tokorico", "Tokopiyon", "Tokotoro", "Tokopisco"]
            source_folder = "./csv_files"

            for file_name in file_names:
                source_file = f"{source_folder}/{file_name}.csv"
                destination_path = f"{folder}/{file_name}.csv"
                shutil.copy(source_file, destination_path)
