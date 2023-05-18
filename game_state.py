import json
import os

class GameState:
    def __init__(self):
        self.filename = "game_state.json"
        self.completed_stages, self.unlocked_images = self.load_game_state()

    def load_game_state(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                content = file.read()
                if content:
                    data = json.loads(content)
                    completed_stages = set(data.get("completed_stages", []))
                    unlocked_images = set(data.get("unlocked_images", []))
                    return completed_stages, unlocked_images
                else:
                    return set(), set()
        else:
            return set(), set()


    def save_game_state(self):
        game_state_data = {
            "completed_stages": list(self.completed_stages),
            "unlocked_images": list(self.unlocked_images)
        }
        with open(self.filename, "w") as file:
            json.dump(game_state_data, file)

    def complete_stage(self, stage_number):
        self.completed_stages.add(stage_number)
        self.save_game_state()

    def is_stage_completed(self, stage_number):
        return stage_number in self.completed_stages

    def unlock_image(self, image_number):
        self.unlocked_images.add(image_number)
        self.save_game_state()

    def is_image_unlocked(self, image_number):
        return image_number in self.unlocked_images
