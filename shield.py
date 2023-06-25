from item import Item


class Shield(Item):
    def receive_damage(self, damage: float):
        self.character.receive_damage(damage / 2)
