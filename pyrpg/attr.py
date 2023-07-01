from typing import Any

class Attr:

    def __init__(self, name: str, value: Any = None) -> None:
        '''
        Create a attribute with a value.
        Args:
            name(str): The name of the attribute.
            value(Any): The value of the attribute, can be any type. Specifically, when the type is int or float, you can set the upper and the lower of the value. Default to None.
        '''
        self.name = name
        self.value = value
        self.upper = None
        self.lower = None

    def set_name(self, name: str):
        self.name = name
