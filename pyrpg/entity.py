from abc import ABC, abstractmethod
from json import load
from typing import Any

class Entity(ABC):
    '''
    Entity is a basic model for every mob, character, enemy or customized creature. It doesn't contains any specific data, but some methods to load and  get data.
    '''

    def get_data(self, name: str) -> Any:
        '''
        Get the entity's data according name.
        Args:
            name(str): the name of the data
        Return:
            The value of the data. If the entity doesn't contain the data, it will return None.
        '''
        return self.__dict__.get(name)
