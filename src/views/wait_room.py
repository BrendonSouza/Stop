import pygame
import json
import time
class Wait_room:
    def __init__(self, main,screen):
        self.screen_board = screen
        self.main = main
        self.exit = False
    
        

    def run(self):
        while True:
            self.screen_board.fill((0, 143, 57))
            pygame.display.update()
            self.verify_number_of_players()
            if(self.exit):
                break

    def verify_number_of_players(self):
        if(self.main.client.number_of_players >= 2):
            self.main.tela = "entrar"
            self.exit = True