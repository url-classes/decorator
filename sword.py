from item import Item


class Sword(Item):
    def calculate_damage(self) -> float:
        return self.character.calculate_damage() * 2
