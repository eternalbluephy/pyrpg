from typing import Any, Union

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
        self._name = name
        self._value = value
        self._upper = None
        self._lower = None
        self._int_restrict = True

    def set_name(self, name: str):
        self._name = name

    def set_value(self, value: Any):
        '''
        Set the value to anything. Ignore the type of current value.
        '''
        self._value = value

    def vary_to(self, amount: float):
        self._check_variable()
        amount = self.ensure_int(amount)
        self.set_value(self.ensure_range(amount))

    def vary_by_amount(self, amount: float):
        ret = self.ensure_int(self._value + amount)
        self.vary_to(ret)

    def vary_by_percent(self, percent: float):
        ret = self.ensure_int(self._value * (1 + percent))
        self.vary_to(ret)

    def ensure_int(self, variable: Union[int, float]) -> Union[int, float]:
        '''
        Ensure the value is a integer after varying when the type of legacy value is int.
        '''
        if self.is_int():
            variable = int(variable)
        return variable
    
    def ensure_range(self, value: Union[int, float]) -> Union[int, float]:
        if (self._upper is not None and value > self._upper):
            value = self._upper
        elif (self._lower is not None and value < self._lower):
            value = self._lower
        return value

    def is_variable(self):
        return self.is_int() or self.is_float()
    
    def is_int(self):
        return isinstance(self._value, int)
    
    def is_float(self):
        return isinstance(self._value, float)

    def _check_variable(self):
        if (not self.is_variable()):
            raise TypeError(f"Attribute '{self._name}' is not variable.")
