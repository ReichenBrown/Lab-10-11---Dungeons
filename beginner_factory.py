from enemy_factory import EnemyFactory
from easy_zombie import EasyZombie
from easy_skelton import EasySkelton
from easy_goblin import EasyGoblin
import random

class BeginnerFactory(EnemyFactory):
  def create_random_enemy(self):
    choice = random.randint(1,3)

    if choice == 1:
      return EasyZombie()
    elif choice == 2:
      return EasySkelton()
    else:
      return EasyGoblin()