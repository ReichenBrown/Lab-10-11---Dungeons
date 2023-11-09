from entity import Entity
import random

class EasyGoblin(Entity):
  def __init__(self):
    super().__init__(name="Goblin", max_hp=random.randint(4,6))

  def attack(self, entity):
    damage = random.randint(2,5)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."