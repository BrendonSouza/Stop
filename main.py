import pygame
import time
from src.views.home import Home
from src.views.board import Board
from src.client import Client
from src.views.wait_room import Wait_room
from src.views.board_verify import Verify_board
class Main:
    def setup(self):

        while True:
            self.clock.tick(30)
            if(self.tela == "home"):
                self.home.run()
            elif(self.tela=="entrar"):
                time.sleep(3)
                self.board.run()
            elif(self.tela=="wait_room"):
                self.wait_room.run()
            elif(self.tela=="board_verify"):
                time.sleep(3)
                self.board_verify.run()

    
    def __init__(self):
        pygame.init()   
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Stop XOU")
        self.tela = "home"
        self.client = Client()
        self.home = Home(self,self.screen)
        self.board = Board(self,self.screen,self.client) 
        self.wait_room = Wait_room(self,self.screen)
        self.board_verify = Verify_board(self,self.screen,self.client)
        self.setup()
        

if __name__ == "__main__":
    main = Main()