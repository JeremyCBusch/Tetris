from game.board import Board
from game.constants import MAX_X
from game.constants import MAX_Y
from game import point
import random
from game import constants
from game.action import Action
from game.point import Point
import sys
class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def crash(self, board_list):
        for i in range(0,210):
            
            if board_list[i - 10].block_type != 0 and board_list[i].get_status() == 1:
               # board_list[i - 10].texture = "game/blocks/red-block.png"
                if board_list[i - 10].status == 0:
                    return True
    
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        board = cast["board"][0]
        
        # for i in range(0, 210):
        #     position = board.coord_plane[i]._get_position()
        #     if position[0] > 380 and board.coord_plane[i].get_status() == 1:

        #         for k in range(0, 210):
        #             board.coord_plane[k].set_right(0)


        #     if position[0] <= 100 and board.coord_plane[i].get_status() == 1:

        #         for z in range(0, 210):
        #             board.coord_plane[z].set_left(0)

        # position= block._get_position()
        # if position[1] < 20:
        #     piece._set_change_x(0)
        #     piece._set_change_y(0)
        # if position[0] <= 20:
        #     piece._set_change_x(0)
        # elif position[0] >= 480:
        #     piece._set_change_x(0)

        if self.crash(board.get_board()):
            for Q in range(0,210):
                        board.coord_plane[Q].set_status(0)
            if not board.end_game: 
                board.load_piece()
            board.score.block_placed()


