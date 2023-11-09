from entity import Entity
import random

class Skelton(Entity):
  def __init__(self):
    super().__init__(name="Armored Skelton", max_hp=random.randint(6,10))

  def attack(self, entity):
    damage = random.randint(6,10)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."