from abc import ABC, abstractmethod

class Color(ABC):

    @property
    @abstractmethod
    def header(self) -> str:
        '''
        The header of the ANSI color code.
        '''
        pass

    @property
    @abstractmethod
    def end(self):
        '''
        The end of the ANSI color code.
        '''
