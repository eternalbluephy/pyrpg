from typing import Any

class Attr:

    def __init__(self, name: str, value: Any = None) -> None:
        '''
        Create a attribute with a value.
        Args:
            name(str): The name of the attribute.
            value(Any): The value of the attribute, can be any type.
                Specifically, when the type is int or float, you can set 
                the upper and the lower of the value. Default to None.
        '''
        self.name = name
        self.value = value
        self.upper = None
        self.lower = None

    def set_name(self, name: str):
        self.name = name

    def set_value(self, value: Any):
        self.value = value

    def vary_to(self, amount: float):
        self._check_variable()
        if (self.upper is not None and amount > self.upper):
            amount = self.upper
        elif (self.lower is not None and amount < self.lower):
            amount = self.lower
        self.set_value(amount)

    def vary_by_amount(self, amount: float):
        self._check_variable()
        ret = self.value + amount
        self.set_value(ret)

    def vary_by_percent(self, percent: float):
        self._check_variable()
        ret = self.value * (1 + percent)
        self.set_value(ret)

    def is_variable(self):
        return isinstance(self.value, int) or isinstance(self.value, float)

    def _check_variable(self):
        if (not self.is_variable()):
            raise TypeError(f"Attribute '{self.name}' is not variable.")
