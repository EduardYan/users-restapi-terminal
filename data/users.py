"""
This file have
a list of users
for simulate a date base.
"""

# users allows
users = [
   {'id': None, 'name': 'Fabio', 'age': 9},
   {'id': None, 'name': 'Checo', 'age': 64},
   {'id': None, 'name': 'Ramon', 'age': 34},
   {'id': None, 'name': 'Oscar', 'age': 10},
   {'id': None, 'name': 'Ryan', 'age': 45},
   {'id': None, 'name': 'Pablo', 'age': 24},
   {'id': None, 'name': 'Juan', 'age': 12}
]

# chaging the value of the id for not make manually
for u in range(len(users)):
   users[u]['id'] = u + 1