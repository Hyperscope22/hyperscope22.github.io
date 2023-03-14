class colors:
    """
    A library for using colored text for print() statements
    """
  #colors
    okyellow = '\033[1;33m'
    okpink = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  #Aliases
    yellow = okyellow
    red = fail
    blue = okblue
    white = endc
    orange = warning
    warn = warning
    uline = underline
    green = okgreen
    cyan = okcyan
    pink = okpink
    black = white #light mode imagine
    default = white
  #Letters
    y = yellow
    w = white
    p = pink
    b = blue
    c = cyan
    g = green
    o = orange
    r = red
    u = uline
    f = fail
    d = default
    bk = black
class backgrounds:
    """
    Background colors for the print() statement
    """
  #Backgrounds
    black = '\033[40m'
    red = '\033[41m'
    green = '\033[42m'
    orange = '\033[43m'
    blue = '\033[44m'
    purple = '\033[45m'
    cyan = '\033[46m'
    lightgrey = '\033[47m'
    default = '\033[39m'
  #Aliases
    d = default
    bl = black
    r = red
    g = green
    o = orange
    b = blue
    p = purple
    c = cyan
    lg = lightgrey
if __name__ == "__main__":
  print(f"This is a {colors.g}library!{colors.w} Use {colors.b}from pcolors import colors as c{colors.w} to use the colors!")