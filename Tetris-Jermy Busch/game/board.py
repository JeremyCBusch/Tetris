from game.tile import Tile
from game.block import Block
from game.piece import Piece
from game.score import Score
import arcade
import time
import random

class Board():# create a large grid as the board
    def __init__(self):
        self.coord_plane = self.create_board()
        self.frames = 0
        self.description = "board"
        self.left_edge = False
        self.right_edge = False
        self.score = Score()
        self.end_game = False
        self.fill_screen = 10
        self.piece = None
        self.load_piece()
         
        



    def create_board(self): # create a board with 50px border
        board = []
        for i in range(0,21):
            for j in range(0,10):
                 #size of block is 40px wide and starting spot is at 70 (50px border, 20px radius)
                position = ((200+(j*25)),(200+(i*25)))
                tile = Tile()
                tile._set_position(position)
                board.append(tile)
        

        
        for i in range(0,10): # the base of the board is regular tiles
            board[i].set_block(1)
            board[i].set_status(0)
            board[i].set_color()

        
        
        return board

    def get_board(self):
        return self.coord_plane

    def draw(self):
        if self.end_game == True:
            # make the "T"
            colors = ["RED","YELLOW","GREEN","PINK","PURPLE"]
            for i in range(0, 10):
                self.coord_plane[170 + i].set_color(random.choice(colors))
                self.coord_plane[160 + i].set_color(random.choice(colors))
            for i in range(3, 16):
                self.coord_plane[(i*10) + 4].set_color(random.choice(colors))
                self.coord_plane[(i*10) + 5].set_color(random.choice(colors))

        for tile in self.coord_plane:
            if tile.get_block() != 0:
                tile.set_block(1)
                tile.draw()
        if self.end_game == True: # when game ends this will draw a block in every tile and print game over
            for i in range(0, self.fill_screen):
                self.coord_plane[i].set_block(0)
                self.coord_plane[i].draw()
                self.score.draw_end()
            if self.fill_screen < 210:
                self.fill_screen += 10
            time.sleep(.00025)

        self.score.draw()
        self.score.t()
        self.score.e()
        self.score.tt()
        self.score.r()
        self.score.i()
        self.score.s()




    def update(self):
        # makes piece move down

        #double frame count, and divide by odd and even to allow for movement, or rotation.
            

        if self.frames % 40 == 39:
            self.piece.position -= 10
            for i in range(0,210):
                if self.coord_plane[i].status == 1:
                    # self.transpose_piece_to_board()
                    self.coord_plane[i - 10].set_block(1)
                    self.coord_plane[i - 10].set_status(1)
                    self.coord_plane[i].set_block(0)
                    self.coord_plane[i].set_status(0)
            self.frames += 1 
                    
        else:
            if self.frames < 40: # Keep things from going infintely else we might make a number too big one day
                self.frames += 1
            else:
                self.frames = 0
                
        
        
        lines_to_delete = []
        for i in range(1,21):
            line_counter = 0
            for j in range(0,10):
                if self.coord_plane[(i*10) + j].get_block() != 0 and self.coord_plane[(i*10) + j].get_status() == 0:
                    line_counter += 1
            if line_counter == 10:
                lines_to_delete.append(i)
        if len(lines_to_delete) > 0:
            for line in lines_to_delete:
                self.score.line_clear()
                for j in range(0,10):
                    self.coord_plane[(line * 10) + j].set_block(0)
                    self.coord_plane[(line * 10) + j].set_status(0)
            for i in range(1,21):
                for j in range(0,10):
                    if self.coord_plane[(i*10) + j].get_block() != 0 and self.coord_plane[(i*10) + j].get_status() == 0:
                        # blocks_to_move.append(((i * 10) + j))
                        self.coord_plane[(i * 10) + j].set_block(0)
                        self.coord_plane[(i * 10) + j].set_status(0)
                        self.coord_plane[((i * 10) - 10) + j].set_block(1)
                        self.coord_plane[((i * 10)- 10) + j].set_status(0)
        # if len(blocks_to_move) > 0:
        #     for block in blocks_to_move:
                


    def move_down_faster(self):
        for i in range(0,210):
            if self.coord_plane[i].get_status() == 1:
                
                self.coord_plane[i-10].set_block(1)
                self.coord_plane[i-10].set_status(1)
                self.coord_plane[i].set_block(0)
                self.coord_plane[i].set_status(0)
                




    def update_left(self):
        
        for i in range(1,21):
            if self.coord_plane[i*10].get_status() == 1:
                self.left_edge = True
            # if self.piece.position % 10 != 0:
        if self.left_edge == False:
            self.piece.position -= 1
            for i in range(0,210):
                if self.coord_plane[i].get_status() == 1 and self.coord_plane[i].get_left() == 1:
                    if i > 10:
                        if self.coord_plane[i-1].get_status() == 0 and self.coord_plane[i-1].get_block() == 1:
                            self.score.ate_block()
                    self.coord_plane[i-1].set_block(self.coord_plane[i].get_block())
                    self.coord_plane[i-1].set_status(1)
                    self.coord_plane[i].set_block(0)
                    self.coord_plane[i].set_status(0)
        self.left_edge = False
                

    def update_right(self):
        # if self.piece.position % 10 != 0:
        
        for i in range(1,21):
            if self.coord_plane[(i*10) + 9].get_status() == 1:
                self.right_edge = True
            # if self.piece.position % 10 != 0:
        if self.right_edge == False:
            list_of_alive = []
            index = 209
            self.piece.position += 1
            while index > 0:
                if self.coord_plane[index].get_status() == 1 and self.coord_plane[index].get_right() == 1:
                    if index < 209 and index > 8:
                        if self.coord_plane[index+1].get_status() == 0 and self.coord_plane[index+1].get_block() == 1:
                            self.score.ate_block()
                    list_of_alive.append(index+1)
                    self.coord_plane[index].set_block(0)
                    self.coord_plane[index].set_status(0)
                index -= 1
            for item in list_of_alive:
                self.coord_plane[item].set_block(1)
                self.coord_plane[item].set_status(1)
        self.right_edge = False
    
    def load_piece(self):
        self.piece = Piece()
        
        x = 0
        y = 0
        board_index = self.piece.position
        piece_index = 0
        piece_grid = self.piece.get_piece() # this is to get the proper rotation
        for i in range(190, 210):
            if self.coord_plane[i].get_status() == 0 and self.coord_plane[i].get_block() == 1:
                self.end_game = True
                
            

        while y < 4:
            x = 0
            while x < 4:
                if piece_grid[piece_index] != 0: # if in the piece grid the certain index is empty or not
                    self.coord_plane[board_index].set_block(piece_grid[piece_index]) # sets the tile value to the value from the piece (1-6)
                    self.coord_plane[board_index].set_status(1) 
                board_index -= 1
                piece_index += 1
                x += 1
            board_index -= 6 # to skip to the next line
            y += 1
  
    def transpose_piece_to_board(self):
        x = 0
        y = 0
        board_index = self.piece.position
        piece_index = 0
        for i in range(0,210):
            if self.coord_plane[i].status == 1:    
                self.coord_plane[i].set_block(0)
                self.coord_plane[i].set_status(0)
        piece_grid = self.piece.get_piece() # this is to get the proper rotation
        while y < 4:
            x = 0
            while x < 4:
                if piece_grid[piece_index] != 0: # if in the piece grid the certain index is empty or not
                    # print(board_index)
                    self.coord_plane[board_index].set_block(piece_grid[piece_index]) # sets the tile value to the value from the piece (1-6)
                    self.coord_plane[board_index].set_status(1) 
                board_index -= 1
                piece_index += 1
                x += 1
            board_index -= 6 # to skip to the next line
            y += 1
  

    
            

        


        
        
          
   
