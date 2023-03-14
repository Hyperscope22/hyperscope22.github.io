from lazy import lazyprewrit as lpw
from pcolors import colors as c, backgrounds as b
from monsterfight import battle as bt
from game import player as p
#example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
#must have color at the end
import random as r
from monsterfight import battle
import time as t
from maingame import game as g
print("Welcome to The Cave.")
print(f"{c.r}Tip:{c.d} If something in a phrase is underlined, it may be a keyword...")
secretsword_owned = False
while True:
  game_choice = input(f"Type {c.u}Start{c.d} to begin: ")
  if game_choice.casefold() == "start":
    print(f"What difficulty do you want? \n {c.u}1{c.d}. {c.u}Easy{c.d}-Higher Player Health & Lower Dragon Health \n {c.u}2{c.d}. {c.u}Normal{c.d}-Normal Stuff \n {c.u}3{c.d}. {c.u}Hard{c.d}-Low Player Health and High Monster Damage \n {c.u}4{c.d}. {c.u}Custom{c.d}")
    #normal DD = 20
    #normal DH = 200
    difficulty = input("Difficulty: ")
    if difficulty.casefold() == "1" or difficulty.casefold() == "easy":
      player = p(120)
      g.wholefuckingthing(180,20,65,10,120,10,20)
      break
    if difficulty.casefold() == "2" or difficulty.casefold() == "normal":
      player = p(100)
      g.wholefuckingthing(200,20,80,10,100,10,20)
      break
    if difficulty.casefold() == "3" or difficulty.casefold() == "hard":
      player = p(80)
      g.wholefuckingthing(200,30,100,15,80,10,20)
      break
    if difficulty == "4" or difficulty.casefold() == "custom":
      dragon_health = int(input("Dragon Health(Reg=200): "))
      dragon_damage = int(input("Dragon Damage(Reg=20): "))
      monster_health = int(input("Monster Health(Reg=80): "))
      monster_damage = int(input("Monster Damage(Reg=10): "))
      player_health = int(input("Player Health(Reg=100): "))
      player = p(player_health)
      g.wholefuckingthing(dragon_health,dragon_damage,monster_health,monster_damage,10,20)
      break
  if game_choice.casefold() == "no":
    print("Well... I dont know what to do with you.")
    secret = input("")
    if secret.casefold() == "secret":
      print(f"You found a {b.p}Secret!{c.d} Since I can't give you and in-game one, past this, I will give you a high-five in person if you got this.")
      break
print("THE END")