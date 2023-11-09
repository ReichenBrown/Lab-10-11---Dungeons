#Authors: Reichen Brown
#Date: 11/9/2023
#Description: Create a program that allows the user to wander through a haunted dungeon maze and fight varying difficulties of monsters that they encounter as they explore.

#from terminal import os
from entity import Entity
from hero import Hero
from map import Map
from beginner_factory import BeginnerFactory
from expert_factory import ExpertFactory
import check_input
import random

def main():
  hero_name = input ("What is your name, traveler? ")
  print("\nDifficulty:\n1. Beginner\n2. Expert\n")
  choice = check_input.get_int_range("Enter Choice: ", 1, 2)
  hero = Hero(hero_name)
  map = Map()
  difficulty = BeginnerFactory() if choice == 1 else ExpertFactory()

  map_num = 1
  choice = 0
  quit = False
  
  while hero.hp > 0 and not quit:
    print(hero)
    print(map.show_map(hero.loc))
    print("1. Go North")
    print("2. Go South")
    print("3. Go East")
    print("4. Go West")
    print("5. Quit")

    choice = 0
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

    #os.system('clear')
    if move == 'o':
      print("You cannot go that way...\n")
      
    elif move == 'm':
      enemy = difficulty.create_random_enemy()
      print(f'You encounter a {enemy.name}\n{enemy}')
      
      while enemy.hp > 0 and hero.hp > 0:
        print(f'1. Attack {enemy.name}')
        print('2. Run Away')
        choice = check_input.get_int_range("Enter choice: ", 1, 2)
        print()
        
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
          print(f'You have slain a {enemy.name}\n')
          map.remove_at_loc(hero.loc)

    elif move == 'n':
      print("There is nothing here...\n")
    elif move == 's':
      print("You wound up at the start of the dungeon!\n")
    elif move == 'i':
      if hero.hp < 25:
        print("You found a Health Potion! You drink it and restore your health.\n")
        hero.heal()
        map.remove_at_loc(hero.loc)
      else:
        print("You found a Health Potion! You are full HP so you leave it in the room.")
    else:
      print("\nCongratulations! You have found the stairs to the next floor of the dungeon.\n")
      map_num += 1
      if map_num == 4:
        map_num = 1
      map.load_map(map_num)
    if hero.hp <= 0:
      print("You died.")
    
main()