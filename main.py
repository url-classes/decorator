from knight import Knight
from magician import Magician
from sword import Sword
from shield import Shield

knight = Knight()
knight = Shield(knight)
knight = Sword(knight)

magician = Magician()
magician = Shield(magician)

damage = knight.calculate_damage()
print('Daño del caballero:', damage)

magician.receive_damage(damage)
print('Puntos de vida:', magician.get_life_points())
