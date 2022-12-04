import pygame
import pygame_textinput 

class Home:
    def run(self):
        while True:
            self.screen_home.fill((148, 0, 211))
            pygame.draw.rect(self.screen_home,"#ffffff",self.retangulo_xou)
            pygame.draw.rect(self.screen_home,"#ffffff",self.botao_entrar,0,10)
            pygame.draw.rect(self.screen_home,"#ffffff",self.botao_criar)
            self.screen_home.blit(self.text_entrar,self.text_rect)
            self.screen_home.blit(self.text_criar,self.text_criar_rect)
            events = pygame.event.get()
            coord_x,coord_y = pygame.mouse.get_pos()
            
            self.chat_input.update(events)
            self.sub_sufarce.blit(self.chat_input.surface,(5,3))
            pygame.display.update()
            
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.verifica_click(self.botao_entrar,coord_x,coord_y)):
                        self.screen_main.tela= "entrar"
                        print("clicou em entrar")
                        self.exit = True
                        break
                    elif(self.verifica_click(self.botao_criar,coord_x,coord_y)):
                        print("clicou em criar sala")
                        break
            if(self.exit):
                break

    def verifica_click(self,botao,x,y):
        return botao.collidepoint(x,y)

    def __init__(self,main,screen):
            self.exit = False
            self.screen_home = screen
            self.screen_main = main
            self.chat_input = pygame_textinput.TextInputVisualizer()
            self.chat_input.font_color = "#000000"
            self.chat_input.cursor_color = "#000000"
            self.retangulo_xou = pygame.Rect(0,0,250,30)
            self.retangulo_xou.center = ((1280/4),360)
            self.sub_sufarce = self.screen_home.subsurface(self.retangulo_xou)

            #Botao Entrar
            self.botao_entrar = pygame.Rect(0,0, 250,50)
            self.font_entrar = pygame.font.SysFont("Arial",18)
            self.text_entrar = self.font_entrar.render("Entrar",True,"#000000")
            self.botao_entrar.center = ((1280*0.75),(720/3))
            self.text_rect = self.text_entrar.get_rect()
            self.text_rect.center =self.botao_entrar.center

            #Botao Criar Sala
            self.botao_criar = pygame.Rect(0,0, 250,50)
            self.font_criar = pygame.font.SysFont("Arial",18)
            self.text_criar = self.font_criar.render("Criar Sala",True,"#000000")
            self.botao_criar.center = ((1280*0.75),(720*0.6))
            self.text_criar_rect = self.text_criar.get_rect()
            self.text_criar_rect.center = self.botao_criar.center
    
    
