from entity import Entity
import random

class Zombie(Entity):
  def __init__(self):
    super().__init__(name="Armored Zombie", max_hp=random.randint(8,10))

  def attack(self, entity):
    damage = random.randint(5,12)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."