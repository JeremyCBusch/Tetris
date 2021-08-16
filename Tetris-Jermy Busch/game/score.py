import arcade
import json

class Score():

    def __init__(self):

        self.score = 0
        self.high_scores = []
        self.load_high_score()

    def load_high_score(self):
        with open("game/scores.json") as file:
            words = json.load(file)
            self.high_scores = words

    def update_scores(self):
        if int(self.score) > int(self.high_scores[0]):
            self.high_scores[0] = self.score
        elif int(self.score) > int(self.high_scores[1]):
            self.high_scores[1] = self.score
        elif int(self.score) > int(self.high_scores[2]):
            self.high_scores[2] = self.score
        elif int(self.score) > int(self.high_scores[3]):
            self.high_scores[3] = self.score
        elif int(self.score) > int(self.high_scores[4]):
            self.high_scores[4] = self.score
        else:
            pass
        
        a_file = open("game/scores.json", "w")
        json.dump(self.high_scores, a_file)
        a_file.close()


    def ate_block(self):
        self.score += 1

    def block_placed(self):
        self.score += 10

    def line_clear(self):
        self.score += 100

    def t(self):
        
        t = "T"
        arcade.draw_text(t, 60 , 660 , arcade.color.WHITE, 30, font_name = "GARA")
    def e(self):
        e = "E"
        arcade.draw_text(e, 80 , 660 , arcade.color.RED, 30, font_name = "GARA")
    def tt(self):
        tt = "T"
        arcade.draw_text(tt, 100 , 660 , arcade.color.GREEN, 30, font_name = "GARA")
    def r(self):
        r = "R"
        arcade.draw_text(r, 120 , 660 , arcade.color.BLUE, 30, font_name = "GARA")
    def i(self):
        i = "I"
        arcade.draw_text(i, 140 , 660 , arcade.color.ORANGE, 30, font_name = "GARA")
    def s(self):
        s = "S"
        arcade.draw_text(s, 150 , 660 , arcade.color.WHITE, 30, font_name = "GARA")


    def draw(self):

        score = "Score: " + str(self.score)

        arcade.draw_text(score, 600, 600, arcade.color.WHITE, 15, font_name="GARA")
        
        #high_scores = "High Scores: \n" + self.high_scores[0] + "\n" + self.high_scores[1] + "\n" + self.high_scores[2] + "\n" + self.high_scores[3] + "\n" + self.high_scores[4]
       
        arcade.draw_text("High Scores:", 550, 400, arcade.color.WHITE, 15, font_name="GARA")
        arcade.draw_text(str(self.high_scores[0]), 550, 370, arcade.color.WHITE, 15, font_name="GARA")
        arcade.draw_text(str(self.high_scores[1]), 550, 350, arcade.color.WHITE, 15, font_name="GARA")
        arcade.draw_text(str(self.high_scores[2]), 550, 330, arcade.color.WHITE, 15, font_name="GARA")
        arcade.draw_text(str(self.high_scores[3]), 550, 310, arcade.color.WHITE, 15, font_name="GARA")
        arcade.draw_text(str(self.high_scores[4]), 550, 290, arcade.color.WHITE, 15, font_name="GARA")
            

    def draw_end(self):
        self.update_scores()
        game_over = "GAME OVER"
        arcade.draw_text(game_over, 500, 500, arcade.color.RED, 20, font_name="GARA" )
        thanks_for_playing = "Thanks for Playing!"
        arcade.draw_text(thanks_for_playing, 500, 450, arcade.color.WHITE, 15, font_name="GARA")

        



