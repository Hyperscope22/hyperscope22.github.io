class weapon:
  def __init__(self,dmg,*,name: str):
    pass   
class player:
  def __init__(self,starthp,*weapon):
    while True:  
      from lazy import lazyprewrit as lpw
      from pcolors import colors as c, backgrounds as b
      from monsterfight import battle as bt
      #example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
      #must have color at the end
      import random as r
      from monsterfight import battle
      import time as t
      from maingame import game as g
      break #imports
    self.health = starthp
    if weapon == None:
      self.weapon = weapon(name = "Fists")
      g.wholefuckingthing.first_pad = 5
      g.wholefuckingthing.second_pad = 12
  def take_damage(self,dmg):
    self.health -= dmg

      