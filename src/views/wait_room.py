import pygame
import json
import time
class Wait_room:
    def __init__(self, main,screen):
        self.screen_board = screen
        self.main = main
        self.exit = False
        self.textFont = pygame.font.SysFont("Arial", 18)
        self.botao_iniciar = pygame.Rect(0, 0, 170, 30)
        self.text_iniciar = self.textFont.render("Iniciar Partida", True, "#000000")
        self.botao_iniciar.center = (self.screen_board.get_width()/2, self.screen_board.get_height()*0.75)
        self.text_iniciar_rect = self.text_iniciar.get_rect()
        self.text_iniciar_rect.center = self.botao_iniciar.center


        

    def run(self):
        while True:
            self.screen_board.fill((0, 143, 57))
            events = pygame.event.get()
            text_wait = self.textFont.render("Aguardando Jogadores...", True, "#ffffff") 
            text_wait_rect = text_wait.get_rect()
            text_wait_rect.center = (self.screen_board.get_width()/2, self.screen_board.get_height()*0.25)
            text_qnt_playeres = self.textFont.render("Jogadores Conectados: "+ str(self.main.client.number_of_players), True, "#ffffff")
            text_qnt_playeres_rect = text_qnt_playeres.get_rect()
            text_wait_rect.center = (self.screen_board.get_width()/2, self.screen_board.get_height()*0.25 + 50)
            self.screen_board.blit(text_qnt_playeres, text_qnt_playeres_rect)
            self.screen_board.blit(text_wait, text_wait_rect)
            coord_x, coord_y = pygame.mouse.get_pos()
            for event in events:
                if event.type == pygame.QUIT:
                    print("Saindo...")
                    self.main.client.destroy()
                    exit()
                   
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(self.botao_iniciar.collidepoint(coord_x, coord_y)):
                        self.main.client.envia_mensagem(json.dumps({"data":{ "type": "start_game" }}))

            
            if(self.main.client.start_game):
                self.main.tela = "entrar"
                self.exit = True


            if(self.main.client.number_of_players >= 2):
                pygame.draw.rect(self.screen_board, "#ffffff", self.botao_iniciar)
                self.screen_board.blit(self.text_iniciar, self.text_iniciar_rect)
            if(self.exit):
                break
            pygame.display.flip()

    def verify_number_of_players(self):
        if(self.main.client.number_of_players >= 2):

            pass
            # self.main.tela = "entrar"
            # self.exit = True