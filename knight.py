from character import Character


class Knight(Character):
    def __init__(self):
        self.life_points = 100
        self.attack = 50
        self.defense = 10

    def get_life_points(self) -> float:
        return self.life_points

    def calculate_damage(self) -> float:
        return self.attack

    def receive_damage(self, damage: float):
        self.life_points = max(0.0, self.life_points - damage * (1 / self.defense))
