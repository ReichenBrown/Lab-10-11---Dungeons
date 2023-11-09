from entity import Entity
import random

class Goblin(Entity):
  def __init__(self):
    super().__init__(name="Armored Goblin", max_hp=random.randint(8,12))

  def attack(self, entity):
    damage = random.randint(6,12)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."