class melee:
  def secret_sword(owned: bool):
    from monsterfight import battle as b
    import random as r
    if owned == True:
      ss_damage = r.randint(25,30)
      pass
    elif owned == False:
      pass
  def katana(owned: bool):
    from monsterfight import battle as b
    if owned == True:
      k_damage = r.randint(20,25)
    if owned == False:
      pass