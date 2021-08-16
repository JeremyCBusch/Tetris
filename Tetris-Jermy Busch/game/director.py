from time import sleep
import arcade
from game import constants
from game.actor import Actor
from game.point import Point
from game.board import Board


class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script, input_service):
        """Initialize the game
        """
        super().__init__(constants.MAX_X, constants.MAX_Y, "Glitchy Tetris")
        self.background_music = arcade.Sound("game/sounds/4-min-sound.wav")
        self._cast = cast
        self._script = script
        self._input_service = input_service

    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.background_music.play(1,0, True)

    def on_update(self, delta_time):
        self._cue_action("update")

    def on_draw(self):
        self._cue_action("output")

    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")

    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)