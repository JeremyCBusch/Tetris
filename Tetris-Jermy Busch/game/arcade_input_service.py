import sys
from game.point import Point

import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []
    
    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = -1
        if arcade.key.LEFT in self._keys:
            x = 1
        elif arcade.key.RIGHT in self._keys:
            x = -1
        if arcade.key.DOWN in self._keys: # speeds up the block
            y = -3

        velocity = (x, y)
        return velocity
        
        
    def should_rotate_left(self):
        return arcade.key.D in self._keys

    def should_rotate_right(self):
        return arcade.key.A in self._keys
