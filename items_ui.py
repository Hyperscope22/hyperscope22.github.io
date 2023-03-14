from maingame import game as g
from pcolors import colors as c, backgrounds as b
#variables to remove errores
monsterhealth = 1
ss_damage = 1
monsterhealth2 = monsterhealth
monster_name = "Demo"
if g.wholefuckingthing.secret_sword == True and g.wholefuckingthing.ninja_sword == False:
  print(
    f"Items: \n {c.u}1{c.d}. {c.u}Sword{c.d} \n {c.u}2{c.d}. {c.u}???{c.d}")
  items_ss = input("Item: ")
  if items_ss.casefold() == "1" or items_ss.casefold() == "sword":
    if useitems_chance <= ss_sword
    print("You pull out your sword and stab the creauture.")
      monsterhealth -= ss_damage
  if items_ss.casefold() == "2" or items_ss.casefold() == "???":
    if monsterhealth == monsterhealth2:
      print(
        f"{c.o}You pull a crowbar out of your ass and beat the shit out of the",
        monster_name, f".{c.d}")
      monsterhealth = monsterhealth - 80
      if monsterhealth > 0:
        print("The crowbar disappears from your hand and the fight continues.")
      if monsterhealth <= 0:
        break  #shut up error line
    elif monsterhealth < monsterhealth2:
      print(
        "You reach into the air but nothing happens. What did you expect to happen? Did you think you would pull a crowbar out your butt?"
      )

if g.wholefuckingthing.secret_sword == False and g.wholefuckingthing.ninja_sword == True: