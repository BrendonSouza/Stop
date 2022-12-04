import pygame
 
from src.views.home import Home
class Main:
    def setup(self):

        while True:
            self.clock.tick(30)
            if(self.tela == "home"):
                self.home.run()
            elif(self.tela=="entrar"):
                print(self.tela)
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Stop XOU")
        self.tela = "home"
        self.home = Home(self,self.screen)
        self.setup()
        

if __name__ == "__main__":
    main = Main()