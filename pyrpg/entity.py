from typing import Optional
from .attr import Attr

class Entity:
    '''
    Entity is a basic model for every mob, character, enemy or customized creature. It doesn't contains any specific data, but some methods to load and  get data.
    '''

    def __init__(self) -> None:
        self._attrs: dict[str, Attr] = {}

    def get_attr(self, name: str) -> Optional[Attr]:
        '''
        Get the entity's attribute according name.
        Args:
            name(str): the name of the data
        Return:
            The attribute. If the entity doesn't contain the data, it will return None.
        '''
        return self._attrs.get(name)
    
    def set_attr(self, name: str, attr: Optional[Attr]) -> None:
        self._attrs[name] = attr