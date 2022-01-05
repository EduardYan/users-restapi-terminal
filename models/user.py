"""
This module have the class User
for model a user

"""


class User:
    """
    Model of user for return
    in the request.
    """

    def __init__(self, id:str, name:str, age:str) -> None:
        # initials values
        self.id = id
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'This is a user with name {self.name} and age {self.age}.'
