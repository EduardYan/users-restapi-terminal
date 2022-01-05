"""
This module have some
functions for work
with the request.

"""

from data.users import users
from data.routes import ROUTES
from models.user import User


def findUser(id:int) -> User:
    """
    Return the user object
    found accorgind the id passed
    for parameter.

    """

    for user in users:
        if id == user['id']:
            break

    # user for return
    user = User(user['id'], user['name'], user['age'])
    return user


def getRequest(request):
   """
   Return the data according the request
   passed for parameter.

   In case the request not is valid return a message
   of error.
   """

   # validating for return it
   if request == ROUTES[0]:
      return users

   elif request[6] == '/':
       # find the user for your id
       id = int(request[7])
       user = findUser(id)

       return [
           # object plain for return
           {'id': user.id, 'name': user.name, 'age': user.age}
       ]

   return 'The request not found.'



def clearDisplay() -> None:
  """
  Clear the console or terminal.
  """

  from os import system
  system('clear')