from os import terminal_size
from entity import Entity
from hero import Hero
from enemy import Enemy
from map import Map
import check_input
import random

def main():
  hero_name = input ("What is your name, traveler? ")
  hero = Hero(hero_name)
  map = Map()
  
  finished = False
  choice = 0
  quit = False
  
  while hero.hp > 0 and not finished and not quit:
    print(hero)
    print(map.show_map(hero.loc))
    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")
    print("5. Quit\n")
    
    choice = check_input.get_int_range("Enter choice: ", 1, 5)
    if choice == 1:
      map.reveal(hero.loc)
      move = hero.go_north()
    elif choice == 2:
      map.reveal(hero.loc)
      move = hero.go_south()
    elif choice == 3:
      map.reveal(hero.loc)
      move = hero.go_east()
    elif choice == 4:
      map.reveal(hero.loc)
      move = hero.go_west()
    else:
      quit = True
      break
    choice = 0


    if move == 'o':
      print("You cannot go that way...\n")
      
    elif map[hero.loc[0]][hero.loc[1]] == 'm':
      enemy = Enemy()
      print(f'You encounter a {enemy.name}\n{enemy}')
      
      while enemy.hp > 0 and hero.hp > 0:
        print(f'1. Attack {enemy.name}')
        print('2. Run Away')
        choice = check_input.get_int_range("Enter choice: ", 1, 2)

        if choice == 1:
          print(hero.attack(enemy))
        else:
          map.reveal(hero.loc)
          moved = hero.loc
          while moved == hero.loc:
            run_num = random.randint(1,4)
            if run_num == 1:
              hero.go_north()
            elif run_num == 2:
              hero.go_south()
            elif run_num == 3:
              hero.go_east()
            else:
              hero.go_west()
          break
        if enemy.hp > 0:
          print(enemy.attack(hero))
        else:
          print(f'You have slain a {enemy.name}')
          map.remove_at_loc(hero.loc)

    elif map[hero.loc[0]][hero.loc[1]] == 'n':
      print("There is nothing here...\n")
    elif map[hero.loc[0]][hero.loc[1]] == 's':
      print("You wound up at the start of the dungeon!\n")
    elif map[hero.loc[0]][hero.loc[1]] == 'i':
      print("You found a Health Potion! You drink it and restore your health.\n")
      hero.heal()
      map.remove_at_loc(hero.loc)
    else:
      finished = True
      print("Congratulations! You have found the exit.\nGame Over")
    if hero.hp <= 0:
      print("You died.")

main()