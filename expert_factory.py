from enemy_factory import EnemyFactory
from zombie import Zombie
from skelton import Skelton
from goblin import Goblin
import random

class ExpertFactory(EnemyFactory):
  def create_random_enemy(self):
    choice = random.randint(1,3)

    if choice == 1:
      return Zombie()
    elif choice == 2:
      return Skelton()
    else:
      return Goblin()