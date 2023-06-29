from abc import ABC, abstractmethod

class Color(ABC):

    @property
    def header(self): ...

    @property
    def ender(self): ...
