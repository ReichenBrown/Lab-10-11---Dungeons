from entity import Entity
from map import Map
import random
import check_input

class Hero(Entity):
  def __init__(self, name):
    super().__init__(name, max_hp=25)
    self.row = 0
    self.col = 0
    self._loc = [self.row, self.col]
  
  @property
  def loc(self):
    return [self.row, self.col]
    
  def attack(self, entity):
      damage = random.randint(2, 5)
      entity.take_damage(damage)
      return f'{self.name} attacks a {entity.name} for {damage} damage.'

  def go_north(self):
      if self.row > 0:
          self.row -= 1
          return Map()[self.row][self.col]
      return 'o'

  def go_south(self):
      if self.row < len(Map()[self.row])-1:
          self.row += 1
          return Map()[self.row][self.col]
      return 'o'

  def go_east(self):
      if self.col < len(Map()[self.col])-1:
          self.col += 1
          return Map()[self.row][self.col]
      return 'o'

  def go_west(self):
      if self.col > 0:
          self.col -= 1
          return Map()[self.row][self.col]
      return 'o'