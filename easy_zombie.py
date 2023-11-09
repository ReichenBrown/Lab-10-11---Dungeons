from entity import Entity
import random

class EasyZombie(Entity):
  def __init__(self):
    super().__init__(name="Zombie", max_hp=random.randint(4,5))

  def attack(self, entity):
    damage = random.randint(1,5)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."