from entity import Entity
import random

class EasySkelton(Entity):
  def __init__(self):
    super().__init__(name="Skelton", max_hp=random.randint(3,4))

  def attack(self, entity):
    damage = random.randint(1,4)
    entity.take_damage(damage)
    return f"{self.name} attacks {entity.name} for {damage} damage."