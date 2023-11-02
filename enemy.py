from entity import Entity
import random

class Enemy(Entity):
  def __init__(self):
    names = ['Goblin', 'Vampire', 'Ghoul', 'Skelton', 'Zombie', 'Spider', 'Enderman', 'Creeper', 'Pillager']
    self._name = names[random.randint(0, len(names)-1)]
    self._max_hp = random.randint(4, 8)
    self._hp = self._max_hp

  def attack(self, entity):
    damage = random.randint(1,4)
    entity.take_damage(damage)

    return f"{self._name} attack a {entity._name} for {damage} damage."