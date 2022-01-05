"""
This is a module
for show of a better form the colors of colorama
module.

Using variabels for use.

"""

from colorama import Fore, Style

STYLE_DEFAULT = Style.DIM

LIST_COLORS = [
  'RED',
  'BLACK',
  'YELLOW',
  'GREEN',
  'BLUE',
  'CYAN',
  'MAGENTA',
  'WHITE',
  'LIGHTBLACK_EX',
  'LIGHTYELLOW_EX',
  'LIGHTWHITE_EX',
  'LIGHTRED_EX',
  'LIGHTBLUE_EX',
  'LIGHTCYAN_EX',
  'LIGHTMAGENTA_EX',
  'LIGHTGREEN_EX'

]

class Color:
  """
  Getting a color
  of colorama module for use.
  Passing the name at class.

  """

  def __init__(self, name):
    if type(name) not in [str]:
      raise TypeError( f'The parameter name {name} is the type --- {type(name)} --- must be a string.' )

    if name not in LIST_COLORS:
      raise TypeError( f"The paremeter name not is a color valid for use. \nColors: {LIST_COLORS}")

    # validating for if not pass none parameter
    if name is None:
      self.name = 'GREEN'

    else:
      self.name = name

  def get_color(self):
    # validations for return the type of color
    if self.name == LIST_COLORS[0]:
      return Fore.RED

    if self.name == LIST_COLORS[1]:
      return Fore.BLACK

    if self.name == LIST_COLORS[2]:
      return Fore.YELLOW

    if self.name == LIST_COLORS[3]:
      return Fore.GREEN

    if self.name == LIST_COLORS[4]:
      return Fore.BLUE

    if self.name == LIST_COLORS[5]:
      return Fore.CYAN

    if self.name == LIST_COLORS[6]:
      return Fore.MAGENTA

    if self.name == LIST_COLORS[7]:
      return Fore.WHITE

    if self.name == LIST_COLORS[8]:
      return Fore.LIGHTBLACK_EX

    if self.name == LIST_COLORS[9]:
      return Fore.LIGHTYELLOW_EX

    if self.name == LIST_COLORS[10]:
      return Fore.LIGHTWHITE_EX

    if self.name == LIST_COLORS[11]:
      return Fore.LIGHTRED_EX

    if self.name == LIST_COLORS[12]:
      return Fore.LIGHTBLUE_EX

    if self.name == LIST_COLORS[13]:
      return Fore.LIGHTCYAN_EX

    if self.name == LIST_COLORS[14]:
      return Fore.LIGHTMAGENTA_EX

    if self.name == LIST_COLORS[15]:
      return Fore.LIGHTGREEN_EX


# colors for use in variables
red = Color('RED')
red = red.get_color()

blue = Color('BLUE')
blue = blue.get_color()

yellow = Color('YELLOW')
yellow = yellow.get_color()

cyan = Color('CYAN')
cyan = cyan.get_color()

green = Color('GREEN')
green = green.get_color()

white = Color('WHITE')
white = white.get_color()

magenta = Color('MAGENTA')
magenta = magenta.get_color()

black = Color('BLACK')
black = black.get_color()

black_s = Color('LIGHTBLACK_EX')
black_s = black_s.get_color()

yellow_s = Color('LIGHTYELLOW_EX')
yellow_s = yellow_s.get_color()

white_s = Color('LIGHTWHITE_EX')
white_s = white_s.get_color()

red_s = Color('LIGHTRED_EX')
red_s = red_s.get_color()

blue_s = Color('LIGHTBLUE_EX')
blue_s = blue_s.get_color()

magenta_s = Color('LIGHTMAGENTA_EX')
magenta_s = magenta_s.get_color()

green_s = Color('LIGHTGREEN_EX')
green_s = green_s.get_color()

cyan_s = Color('LIGHTCYAN_EX')
cyan_s = cyan_s.get_color()
