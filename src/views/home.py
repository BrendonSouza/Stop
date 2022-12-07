import pygame
import pygame_textinput 
import json

class Home:
    def run(self):
        while True:
            self.screen_home.fill((148, 0, 211))
            pygame.draw.rect(self.screen_home,"#ffffff",self.retangulo_xou)
            pygame.draw.rect(self.screen_home,"#ffffff",self.botao_entrar,0,10)

            
            self.screen_home.blit(self.text_entrar,self.text_rect)

            self.screen_home.blit(self.text_nome,self.text_nome_rect)
            events = pygame.event.get()
            coord_x,coord_y = pygame.mouse.get_pos()
            
            self.name_input.update(events)
            self.sub_sufarce.blit(self.name_input.surface,(5,3))
            pygame.display.update()
            
            for event in events:
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.verifica_click(self.botao_entrar,coord_x,coord_y)):
                        self.screen_main.tela= "entrar"
                        mensagem = self.name_input.value
                        self.screen_main.client.name = mensagem
                        self.send(mensagem)
                        self.exit = True
                        
                        break

            if(self.exit):
                break

    def verifica_click(self,botao,x,y):
        return botao.collidepoint(x,y)
    
    def send(self,mensagem):
        obj = {
            "length": 2048,
            "data":{
                "type": "send_name",
                "name": mensagem
            }
        }
        self.screen_main.client.envia_mensagem(json.dumps(obj))

    def __init__(self,main,screen):
            self.exit = False
            self.screen_home = screen
            self.screen_main = main
            # text Nome
            self.nome_font = pygame.font.SysFont("Arial", 18)
            self.text_nome = self.nome_font.render("Nome:", True, "#ffffff")
            self.text_nome_rect = self.text_nome.get_rect()
            self.text_nome_rect.center = ((1280*0.173),330)
            self.name_input = pygame_textinput.TextInputVisualizer()
            self.name_input.font_color = "#000000"
            self.name_input.cursor_color = "#000000"
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


    
    
