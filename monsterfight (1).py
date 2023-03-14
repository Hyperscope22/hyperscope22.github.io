class battle:
  def monster_battle(monsterhealth,monster_attackdamage,monster_name: str,player_health,first_pad,second_pad):
    import time as t
    player_health2 = player_health
    monster100 = monsterhealth
    monster80 = 0.8 * monsterhealth
    monster60 = 0.6 * monsterhealth
    monster40 = 0.4 * monsterhealth
    monster20 = 0.2 * monsterhealth
    monster0 = 0 * monsterhealth
    monster60cc = 25
    monster40cc = 50
    monster80cc = 5
    monster20cc = 75
    monster0cc = 90
    sssword_chance = 40
    ns_chance = 45
    from pcolors import colors as c, backgrounds as b
    #example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
    from maingame import game as g
    from weapons import melee as m
    import random as r
    from game import player as p
    monster_caught = False
    monsterhealth2 = monsterhealth
    monstermove_counter = 0
    while monsterhealth > 0 and player_health > 0 and monster_caught == False:
    #monster fight
      monstercv = r.randint(1,100)
      useitems_chance = r.randint(1,100)
      player_attackdamage = r.randint(first_pad,second_pad)
      t.sleep(1)
      print(f"{b.b}BATTLE:{c.d}{b.d}")
      print("Player Health: ", player_health)
      print("Enemy Health: ",monsterhealth)
      deathpit_choice2 = input(f"{c.u}Attack{c.d}, {c.u}Capture{c.d}, or {c.u}Items{c.d}: ")
      if deathpit_choice2.casefold() == "attack":
        print("You swing at the monster and it loses some health")
        monstermove_counter += 1
        monsterhealth -= player_attackdamage
      if deathpit_choice2.casefold() == "capture":
        monstermove_counter += 1
        if monsterhealth > monster80 and monsterhealth <= monster100:
          if monstercv <= monster80cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice")
            t.sleep(2)
            print("Three times! You caught a", monster_name+"!")
            monster_caught = True
          if monstercv > monster80cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice.")
            t.sleep(2)
            print("But then the ball explodes and the monster pops out.")
        if monsterhealth > monster60 and monsterhealth <= monster80:
          if monstercv <= monster60cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice")
            t.sleep(2)
            print("Three times! You caught a", monster_name+"!")
            monster_caught = True
          if monstercv > monster60cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice.")
            t.sleep(2)
            print("But then the ball explodes and the monster pops out.")
        if monsterhealth > monster40 and monsterhealth <= monster60:
          if monstercv <= monster40cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice")
            t.sleep(2)
            print("Three times! You caught a", monster_name+"!")
            monster_caught = True
          if monstercv > monster40cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice.")
            t.sleep(2)
            print("But then the ball explodes and the monster pops out.")
        if monsterhealth > monster20 and monsterhealth <= monster40:
          if monstercv <= monster20cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice")
            t.sleep(2)
            print("Three times! You caught a", monster_name+"!")
            monster_caught = True
          if monstercv > monster20cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice.")
            t.sleep(2)
            print("But then the ball explodes and the monster pops out.")
        if monsterhealth > monster0 and monsterhealth <= monster20:
          if monstercv <= monster0cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice")
            t.sleep(2)
            print("Three times! You caught a", monster_name+"!")
            monster_caught = True
          if monstercv > monster0cc:
            print("You throw a Jameball at the monster and it is absorbed inside. The ball shakes once.")
            t.sleep(2)
            print("Twice.")
            t.sleep(2)
            print("But then the ball explodes and the monster pops out.")
      if deathpit_choice2.casefold() == "items":
        monstermove_counter += 1
        if monsterhealth == monsterhealth2:
          print(f"{c.o}You pull a crowbar out of your ass and beat the shit out of the", monster_name,f".{c.d}")
          monsterhealth = monsterhealth-80
          if monsterhealth > 0:
            print("The crowbar disappears from your hand and the fight continues.")
          if monsterhealth <= 0:
            break
        elif monsterhealth < monsterhealth2:
          print("You reach into the air but nothing happens. What did you expect to happen? Did you think you would pull a crowbar out your butt?")
      if deathpit_choice2.casefold() == "devmode":
        dev_input = input("Dev: ")
        if dev_input == "RESET":
          monsterhealth = monsterhealth2
          print(monsterhealth)
          player_health = player_health2
          pass
        if dev_input == "EXIT":
          break
        if dev_input == "DAMAGE+":
          first_pad += 5
          second_pad += 5
          print(player_attackdamage)
        if dev_input == "DAMAGE-":
          first_pad -= 5
          second_pad -= 5
        if dev_input == "HARD":
          monster_attackdamage = monster_attackdamage + 10
        if dev_input == "EASY":
          monster_attackdamage -= 5
        if dev_input == "STATS":
          print(" Monster Health: ", str(monsterhealth), "\n", "Monster Attack Damage:", str(monster_attackdamage), "\n", "Player Attack Damage Range:", first_pad,"-",second_pad, "\n", "Player Health:", str(player.health))
      if monstermove_counter >= r.randint(1,5):
        t.sleep(2)
        print(f"{c.g}The",monster_name,f"swings at you and scratches you badly.{c.d}")
        player_health -= monster_attackdamage
        monstermove_counter = 0
    #outside of fight
    if monster_caught == True and player_health > 0:
      print("A",monster_name, "was added to your Jamedeck.") 
    if monster_caught == False and player_health > 0:
      print("That was an awesome fight! Good job taking that monster down!")
    if player_health <= 0:
      t.sleep(1)
      print("You died...")
      pass