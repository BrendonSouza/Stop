import pygame
import pygame_textinput 

class Board:
    def run(self):
        while True:
            self.screen_board.fill((148, 0, 211))
           
            events = pygame.event.get()
            coord_x,coord_y = pygame.mouse.get_pos()
            

            pygame.display.update()
            
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if(self.exit):
                break
    
    
    def __init__(self,main,screen):
        self.exit = False
        self.screen_board = screen
        self.screen_main = main

        #colocando campos de input pela tela, vamos ter 9 campos de input
       
    
    