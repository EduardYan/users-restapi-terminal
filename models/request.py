"""
This module have the class Request
for model a request

"""


class Request:
    """
    Create a request with
    a direction according to id,
    name, or age.
    """

    def __init__(self, data:str) -> None:
        self.data = data
