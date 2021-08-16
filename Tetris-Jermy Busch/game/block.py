import arcade
from game.point import Point
from game import constants
from game.actor import Actor
import arcade

class Block(arcade.Sprite):
    def __init__(self):
        super().__init__("game/blocks/Blue-block.png")
        self._description = 'block' 
        
    def get_description(self):
        return self._description
    
        
