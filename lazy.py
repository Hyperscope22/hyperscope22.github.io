from pcolors import colors as c, backgrounds as b
#example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
#must have color at the end
import random as r
from monsterfight import battle
import time as t
class lazyprewrit:
  def cfunction():
    from pcolors import colors as c, backgrounds as b
#example for colors: print(f"{c.g}{b.c}Hello!{c.d}{b.bl}")
#must have color at the end
    import random as r
    import time as t
    while True:
      con1 = input(f"Type {c.u}Next{c.d} to {c.u}Continue{c.d}: ")
      if con1.casefold() == "next":
        print("Let's Continue...")
        break
      elif con1.casefold() == "continue":
        print(f"Another {b.p}Secret!{c.d} Wow thats pretty cool.")
        print("Good luck finding them")
        break
      else:
        print("???")
      pass