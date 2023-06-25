from character import Character


class Item(Character):
    def __init__(self, character: Character):
        self.character = character

    def get_life_points(self) -> float:
        return self.character.get_life_points()

    def calculate_damage(self) -> float:
        return self.character.calculate_damage()

    def receive_damage(self, damage: float):
        self.character.receive_damage(damage)
