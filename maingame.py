class game:

  def wholefuckingthing(dragon_health, dragon_damage, monster_health, monster_damage,player_health, first_pad, second_pad):
    #imports
    from lazy import lazyprewrit as lpw
    from pcolors import colors as c, backgrounds as b
    #example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
    #must have color at the end
    import random as r
    from monsterfight import battle
    import time as t
    #end of imports; start of variables
    secret_sword = False
    ninja_sword = False
    #end of variables
    while True:
      player_attackdamage = r.randint(first_pad, second_pad)
      print(
        f"{b.b}SCENE:{c.d}{b.d} You enter the cave. There is a fork in the tunnel that splits off into 2 directions: Right and Left. Where do you go?"
      )
      player_choice1 = input("Right or Left: ")
      if player_choice1.casefold() == "right" or player_choice1.casefold() == "r":
        #dragon cave
        print(
          "You walk into a damp cave and hear water dripping somewhere off in the distance. The dark starts to loom. Do you continue?"
        )
        dragoncave_choice1 = input("Continue? ")
        if dragoncave_choice1.casefold(
        ) == "yes" or dragoncave_choice1.casefold(
        ) == "continue" or dragoncave_choice1.casefold() == "yea":
          print(
            "A small light apears in the distance. You head towards it and your eyes start to ajust to the new light. You look around and skeletons of the people that came before, lay on the ground. You see the light comes from a torch on the wall. Do you want to pick it up?"
          )
          torch_choice = input("Will you take it? ")
          if torch_choice.casefold() == "yes":
            print(
              "You pick up the torch. The fire grows bright and illuminates the whole room. You get a better view of the skeletons and see some carried sword with golden handles and others carried chests with gems and gold. You jump to gather the riches but stop when you realize it will only weigh you down. You wonder, 'When does this cave end?' Do you dare continue?"
            )
            dragoncave_choice2 = input("Do you dare: ")
            if dragoncave_choice2.casefold() == "yes":
              print(
                "You walk forward slowly. After a short walk, you hear a snarling sound and a massive cave opens in front of you."
              )
              print(
                "A dragon is laying on the ground in front of you, sleeping.")
              dragonfight_choice1 = input("Do you wish to fight it? ")
              if dragonfight_choice1.casefold() == "yes":
                print(f"{c.g}{b.b}[Dragon fight here]{c.d}{b.d}")
                t.sleep(2)
                print("Uhh...Well...")
                t.sleep(2)
                print("I... kinda.. haven't coded it yet...")
                t.sleep(3)
                print("I should probably add it, right?")
                t.sleep(4)
                dragonfight_choice2 = input("Would you like me to add it? ")
                if dragonfight_choice2.casefold() == "yes":
                  print("Okay, I'll work on it. Give me a sec...")
                  t.sleep(r.randint(2, 4))
                  print(".")
                  t.sleep(r.randint(2, 4))
                  print("..")
                  t.sleep(r.randint(2, 4))
                  print("...")
                  t.sleep(3)
                  print("Okay, it's done. Let's run it.")
                  t.sleep(4)
                  print(
                    "You run at the dragon and it wakes up with a jolt. It bares its teeth and moves towards you."
                  )
                  battle.monster_battle(dragon_health, dragon_damage, "Dragon",player_health, first_pad, second_pad)
                  break
                if dragonfight_choice2.casefold() == "no" or dragonfight_choice2.casefold() == "n":
                  print("Fine then. Bye")
                  break
              if dragonfight_choice1.casefold() == "no" or dragonfight_choice1.casefold() == "n":
                print(
                  "You attempt to sneak past the dragon but the dragon hears your stomping. It lifts up its massive head and eats you."
                )

                break
            if dragoncave_choice2.casefold() == "no" or dragoncave_choice2.casefold() == "n":
              print(
                "You turn around to leave the cave but the ground rumbles and a wall of stone sildes down from the roof, trapping you in the cave. You turn the other way and another wall slides down. You are trapped."
              )
              secret2 = input()
              if secret2.casefold() == "yes" or secret2.casefold() == "continue" or secret2.casefold() == "next" or secret2.casefold() == "y":
                print(
                  f"You found a {b.p}Secret!{c.d} I have no idea how though..."
                )
                print(
                  "A passage opens in the wall to your left, right next to a large skeleton."
                )
                secret2_choice = input("Do you want to go into the room?")
                if secret2_choice.casefold() == "yes":
                  print(
                    "You walk in through the passage. You take a tentative step forward and nothing happens, so you keep on walking. The opening shuts behind you, but your helpful torch allows you to see. You walk into a small room with a large golden chest in the middle."
                  )
                  secret2_choice2 = input("Do you open the chest? ")
                  if secret2_choice2.casefold() == "yes":
                    print(
                      f"You got a second {b.p}Secret!{c.d} All in the same thing. Since I can't give you and in-game one, past this, I will give you a high-five in person if you got this."
                    )
                  if secret2_choice2.casefold() == "no" or secret2_choice2.casefold() == "n":
                    print(
                      "What the fuck! You were so close and you just decided to fucking say NO! What the FUCK! AHHHHHHH! You deserve to die! I'm going to code your death right here. Ready?"
                    )
                    print(
                      "Traps in the walls appear and close in on you. This is the end of the player."
                    )
                if secret2_choice.casefold() == "no" or secret2_choice.casefold() == "n":
                  print("")
              break
          if torch_choice.casefold() == "no" or torch_choice.casefold() == "n":
            print(
              "You continue walking. The light from the torch fades as you walk farther away. Suddenly, you lose all sight, and the darkness consumes you."
            )
            break
        if dragoncave_choice1.casefold() == "no" or dragoncave_choice1.casefold() == "n":
          print(
            " You take a left, even though the only way is straight, and walk through a wall. \n A hallway appears and lights, imbedded in the ceiling, illuminate the whole room. \n The walls are a blank white and the hallway seems to be a never ending tunnel.\n 'Welcome to the Thinking Room,' a voice says overhead. 'This is where I brainstorm my game ideas. My name is James.'"
          )
          thinking_room = input("Do you want to know more? ")
          if thinking_room.casefold() == "yes":
            print(
              f"' You can consider these rooms as the so called Back Rooms,' James says. \n 'This is where I work and it is the hidden part of the game for the developers(currently only me), and given that you are not a developer, you must leave. \n {c.b}break{c.d} 'Welp, now that they're gon- Wait, how are you still here? I closed the loop... It should have ended the game.' \n 'I'm going to try again' \n {c.b}b̷̺͋͊̀̿rea̶͕͚͚̮̅̇̈̽̈́̄̆k{c.d} \n 'I'm̵̜̈́̓͝͝  b̵̞͙̞͙̱͖̱͑̈́̆͗̀̆̊̚͜ͅͅr̵̛͓̫̱͙̙̬̱͇̘̬͌̾̿̆̂͗̓̑̀̊̊ok̵̲̝͍̯̣͇̤̏en̸̜̰̝̒! A̶̧̨̨̳͙̱͙̠̜͓̼͉͔̚͘Ĥ̷̾̾̂͑̂̾͛͐̀́̆͘H̴͙̓Ĥ̷̢̯̱͈͉̾̾̂͑̂̾͛͐̀́̆͘͜H̴͙̓Ḣ̴̹͇͓͉͉̃́̀̒̀̏͠͠͝͝Ḣ̴̹͇͓͉͉̃́̀̒̀̏͠͠͝͝"
            )
          t.sleep(120)
          print(
            "Why are you still here? The game is meant to be broken. You should have left. You just sat here for 2 minutes! For what? Anyways, just close the program."
          )
          t.sleep(45)
          print("What the heck? There is nothing here!")
          t.sleep(30)
          print(
            "You sat here for over 3 minutes for what? You know what, that really isn't that long. You could sit here longer. I don't care"
          )
          t.sleep(45)
          print(
            f"Fine... Take the {b.p}Unnamed Secret{c.d}. I'm not naming it")
      if player_choice1.casefold() == "left" or player_choice1.casefold() == "l":
        #death pit
        print(
          "You walk down a dark cave. Suddenly, you lose all vision and you continue walking blindly. You hear the sound of water splashing in the distance. You think, 'There may be something down this path,'"
        )
        deathpit_choice1 = input("Have you seen enough?  ")
        if deathpit_choice1.casefold() == "no" or deathpit_choice1.casefold() == "n":
          print(
            "You walk and hear a sound to your right. You look over and see some horrendous creature crawl out of the ground. It growls and picks it self up so that it stands in a hunched over stance. Suddenly it runs at you like it wants to kill you. What do you do?"
          )
          t.sleep(1)
          battle.monster_battle(monster_health, monster_damage, "Cave Monster",player_health, first_pad, second_pad)
          break
        if deathpit_choice1.casefold() == "yes":
          print(
            "I need to finish some other code. You may want to restart because nothing will be here for a long time. So just restart the game and pick a different path, I'll see you some where else."
          )
          dpc1_sec_count = 0
          while dpc1_sec_count < 5:
            t.sleep(10)
            print(".")
            t.sleep(10)
            print("..")
            t.sleep(10)
            print("...")
            dpc1_sec_count += 1
            if dpc1_sec_count == 2:
              print("Why are you still here? There is nothing here...")
            if dpc1_sec_count == 4:
              print("There is nothing here exept unfinished code.")
          if dpc1_sec_count == 5:
            print(
              f"Wow, you have been here a while. Most people dont even go down this path. You know what, for your dedication to nothingness, I'll give you the {b.p}Secret of Nothingness{c.d}?"
            )

  #hopefully outside of code
  def afterdragon(player_health, first_pad, second_pad):
    from lazy import lazyprewrit as lpw
    from pcolors import colors as c, backgrounds as b
    #example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
    #must have color at the end
    import random as r
    from monsterfight import battle
    import time as t
    lpw.cfunction()
    if player_health > 0:
      print("Now that the dragon is gone, a chest is revealed. ")
    elif player_health <= 0:
      t.sleep(1)
      print("Thanks for playing my game. Try again soon!")
