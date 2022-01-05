"""
This is the principal
file for execute the restapi in the
terminal.
"""

from colors.colors import (
    blue,
    yellow,
    red_s,
    cyan_s,
    red,
    green,
    white_s,
    blue_s,
    white
)

from colorama import init
from data.users import users
from data.commands import COMMANDS
from data.constants import EXIT
from messages.initials import INITIAL_MESSAGE
from data.routes import ROUTES
from models.request import Request
from utils.helpers import getRequest, clearDisplay


if __name__ == '__main__':
   init(autoreset = True)

   # showing initial message
   print( blue + INITIAL_MESSAGE)

   # principal loop
   while True:
      request = input(yellow + 'Request url > ')

      if request == EXIT:
         break

      elif request == "?commands" or request == "?co":
        print('All commands start with ? sign.')

        for c in range(len(COMMANDS)):
          print()
          # showing alls the commands
          print("Command: " + blue_s + f'- {COMMANDS[c]["command"]} -     ' + white + "Action: " + blue_s + f'{COMMANDS[c]["action"]}' )

      elif request == "?routes":
         print(green + "Routes for do the requests.\n")

         # showing the routes for do the requests
         for r in ROUTES:
            print( green + f'Route: {r}')

      elif request == 'c' or request == 'c ':
        clearDisplay()


      else:
         request = Request(request)
         try:
            request = getRequest(request.data)

            print(cyan_s + '=====================================')

            if request == "The request not found.":

              print(red + request)

            else:
              print( red_s + 'Founds')
                # showing the data of the request
              for data in request:
                print(red_s + str(data))

              print(cyan_s + '=====================================')

         except IndexError:
            print('Some problem with the request. Verify the request.')


   print(green + '\nExited:}')
