import pygame
import pygame_textinput


class Board:
    def __init__(self, main, screen):
        self.input_selected = 1
        self.exit = False
        self.screen_board = screen
        self.screen_main = main
        self.letra_sorteada = 'A'


        # Texto inicial
        self.font = pygame.font.SysFont('Arial', 20)
        self.titulo = self.font.render('Palavras com a letra: '+ self.letra_sorteada, True, (0, 0, 0))
        self.titulo_rect = self.titulo.get_rect()
        self.titulo_rect.center = (self.screen_board.get_width() / 2, 50)

        # Botão Stop
        self.stop = pygame.image.load('stop.png')
        self.stop_rect = self.stop.get_rect()
        self.stop_rect.center = (self.screen_board.get_width() / 2, self.screen_board.get_height() - 50)
        self.make_input()
        self.make_input_rectangle()
    def run(self):
        while True:
            self.screen_board.fill((148, 0, 211))

            self.events = pygame.event.get()

            # colocando os campos de input na tela
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_1,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_2,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_3,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_4,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_5,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_6,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_7,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_8,0,10)
            pygame.draw.rect(self.screen_board, (255, 255, 255),
                             self.retangulo_9,0,10)

            
            
            self.screen_board.blit(
                self.input_1.surface,
                (self.retangulo_1.x + 5, self.retangulo_1.y + 5))
            self.screen_board.blit(
                self.input_2.surface,
                (self.retangulo_2.x + 5, self.retangulo_2.y + 5))
            self.screen_board.blit(
                self.input_3.surface,
                (self.retangulo_3.x + 5, self.retangulo_3.y + 5))
            self.screen_board.blit(
                self.input_4.surface,
                (self.retangulo_4.x + 5, self.retangulo_4.y + 5))
            self.screen_board.blit(
                self.input_5.surface,
                (self.retangulo_5.x + 5, self.retangulo_5.y + 5))
            self.screen_board.blit(
                self.input_6.surface,
                (self.retangulo_6.x + 5, self.retangulo_6.y + 5))
            self.screen_board.blit(
                self.input_7.surface,
                (self.retangulo_7.x + 5, self.retangulo_7.y + 5))
            self.screen_board.blit(
                self.input_8.surface,
                (self.retangulo_8.x + 5, self.retangulo_8.y + 5))
            self.screen_board.blit(
                self.input_9.surface,
                (self.retangulo_9.x + 5, self.retangulo_9.y + 5))

            self.screen_board.blit(
                self.label_1, (self.retangulo_1.x, self.retangulo_1.y - 20))
            self.screen_board.blit(
                self.label_2, (self.retangulo_2.x, self.retangulo_2.y - 20))
            self.screen_board.blit(
                self.label_3, (self.retangulo_3.x, self.retangulo_3.y - 20))
            self.screen_board.blit(
                self.label_4, (self.retangulo_4.x, self.retangulo_4.y - 20))
            self.screen_board.blit(
                self.label_5, (self.retangulo_5.x, self.retangulo_5.y - 20))
            self.screen_board.blit(
                self.label_6, (self.retangulo_6.x, self.retangulo_6.y - 20))
            self.screen_board.blit(
                self.label_7, (self.retangulo_7.x, self.retangulo_7.y - 20))
            self.screen_board.blit(
                self.label_8, (self.retangulo_8.x, self.retangulo_8.y - 20))
            self.screen_board.blit(
                self.label_9, (self.retangulo_9.x, self.retangulo_9.y - 20))
            
            self.screen_board.blit(self.titulo,(self.screen_board.get_width()/2 - 100, self.titulo.get_height()/2))
            self.screen_board.blit(self.stop,(self.screen_board.get_width()/2 - 100, self.screen_board.get_height() - 200))
            self.verifica_input_selecionado()

            coord_x, coord_y = pygame.mouse.get_pos()
            # verificando eventos
            for event in self.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.verifica_colisao_input(coord_x, coord_y)
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.update()

    def verifica_input_selecionado(self):
        if (self.input_selected == 1):
            self.input_1.update(self.events)
        elif (self.input_selected == 2):
            self.input_2.update(self.events)
        elif (self.input_selected == 3):
            self.input_3.update(self.events)
        elif (self.input_selected == 4):
            self.input_4.update(self.events)
        elif (self.input_selected == 5):
            self.input_5.update(self.events)
        elif (self.input_selected == 6):
            self.input_6.update(self.events)
        elif (self.input_selected == 7):
            self.input_7.update(self.events)
        elif (self.input_selected == 8):
            self.input_8.update(self.events)
        elif (self.input_selected == 9):
            self.input_9.update(self.events)
        else:
            self.input_1.update(self.events)

    def verifica_colisao_input(self, coord_x, coord_y):
        if self.retangulo_1.collidepoint(coord_x, coord_y):
            self.input_selected = 1
        elif self.retangulo_2.collidepoint(coord_x, coord_y):
            self.input_selected = 2
        elif self.retangulo_3.collidepoint(coord_x, coord_y):
            self.input_selected = 3
        elif self.retangulo_4.collidepoint(coord_x, coord_y):
            self.input_selected = 4
        elif self.retangulo_5.collidepoint(coord_x, coord_y):
            self.input_selected = 5
        elif self.retangulo_6.collidepoint(coord_x, coord_y):
            self.input_selected = 6
        elif self.retangulo_7.collidepoint(coord_x, coord_y):
            self.input_selected = 7
        elif self.retangulo_8.collidepoint(coord_x, coord_y):
            self.input_selected = 8
        elif self.retangulo_9.collidepoint(coord_x, coord_y):
            self.input_selected = 9
        elif self.stop_rect.collidepoint(coord_x, coord_y):
            print("Stop")

    def define_rect(self):
        self.label_1_rect = self.label_1.get_rect()
        self.label_2_rect = self.label_2.get_rect()
        self.label_3_rect = self.label_3.get_rect()
        self.label_4_rect = self.label_4.get_rect()
        self.label_5_rect = self.label_5.get_rect()
        self.label_6_rect = self.label_6.get_rect()
        self.label_7_rect = self.label_7.get_rect()
        self.label_8_rect = self.label_8.get_rect()
        self.label_9_rect = self.label_9.get_rect()

    def make_input_rectangle(self):

        self.input_1_subsurface = self.screen_board.subsurface(
            self.retangulo_1)
        self.input_2_subsurface = self.screen_board.subsurface(
            self.retangulo_2)
        self.input_3_subsurface = self.screen_board.subsurface(
            self.retangulo_3)
        self.input_4_subsurface = self.screen_board.subsurface(
            self.retangulo_4)
        self.input_5_subsurface = self.screen_board.subsurface(
            self.retangulo_5)
        self.input_6_subsurface = self.screen_board.subsurface(
            self.retangulo_6)
        self.input_7_subsurface = self.screen_board.subsurface(
            self.retangulo_7)
        self.input_8_subsurface = self.screen_board.subsurface(
            self.retangulo_8)
        self.input_9_subsurface = self.screen_board.subsurface(
            self.retangulo_9)
    def make_label(self):
        
        self.label_font = pygame.font.SysFont("Arial", 18)
        self.label_1 = self.label_font.render(
            "Profissão", True, (255, 255, 255))
        self.label_2 = self.label_font.render("CEP", True, (255, 255, 255))
        self.label_3 = self.label_font.render("Animal", True, (255, 255, 255))
        self.label_4 = self.label_font.render("Comida", True, (255, 255, 255))
        self.label_5 = self.label_font.render(
            "Filmes e Séries", True, (255, 255, 255))
        self.label_6 = self.label_font.render(
            "Minha Sogra é", True, (255, 255, 255))
        self.label_7 = self.label_font.render("Cores", True, (255, 255, 255))
        self.label_8 = self.label_font.render("Nome", True, (255, 255, 255))
        self.label_9 = self.label_font.render("Famosos", True, (255, 255, 255))

    def make_input(self):       
        self.input_1 = pygame_textinput.TextInputVisualizer()
        self.input_2 = pygame_textinput.TextInputVisualizer()
        self.input_3 = pygame_textinput.TextInputVisualizer()
        self.input_4 = pygame_textinput.TextInputVisualizer()
        self.input_5 = pygame_textinput.TextInputVisualizer()
        self.input_6 = pygame_textinput.TextInputVisualizer()
        self.input_7 = pygame_textinput.TextInputVisualizer()
        self.input_8 = pygame_textinput.TextInputVisualizer()
        self.input_9 = pygame_textinput.TextInputVisualizer()
        self.define_fonte()
        self.retangulo_1 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_2 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_3 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_4 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_5 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_6 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_7 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_8 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_9 = pygame.Rect(0, 0, 170, 30)
        self.make_label()
        self.define_rect()
        # definindo o centro dos retangulos e labels
        self.retangulo_1.center = (
            self.screen_board.get_width()/4, self.screen_board.get_height()/2 - 100)
        self.label_1_rect.center = (
            self.screen_board.get_width() / 4, self.screen_board.get_height()/2 - 110)

        self.retangulo_2.center = (self.screen_board.get_width(
        )*0.5, self.screen_board.get_height()/2 - 100)
        self.label_2_rect.center = (self.screen_board.get_width(
        ) * 0.5, self.screen_board.get_height()/2 - 110)

        self.retangulo_3.center = (self.screen_board.get_width(
        )*0.75, self.screen_board.get_height()/2 - 100)
        self.label_3_rect.center = (self.screen_board.get_width(
        ) * 0.75, self.screen_board.get_height()/2 - 110)

        self.retangulo_4.center = (
            self.screen_board.get_width()/4, self.screen_board.get_height()/2)
        self.label_4_rect.center = (
            self.screen_board.get_width() / 4, self.screen_board.get_height()/2 - 10)

        self.retangulo_5.center = (
            self.screen_board.get_width()*0.5, self.screen_board.get_height()/2)
        self.label_5_rect.center = (self.screen_board.get_width(
        ) * 0.5, self.screen_board.get_height()/2 - 10)

        self.retangulo_6.center = (
            self.screen_board.get_width()*0.75, self.screen_board.get_height()/2)
        self.label_6_rect.center = (self.screen_board.get_width(
        ) * 0.75, self.screen_board.get_height()/2 - 10)

        self.retangulo_7.center = (
            self.screen_board.get_width()/4, self.screen_board.get_height()/2 + 100)
        self.label_7_rect.center = (
            self.screen_board.get_width() / 4, self.screen_board.get_height()/2 + 90)

        self.retangulo_8.center = (self.screen_board.get_width(
        )*0.5, self.screen_board.get_height()/2 + 100)
        self.label_8_rect.center = (self.screen_board.get_width(
        ) * 0.5, self.screen_board.get_height()/2 + 90)

        self.retangulo_9.center = (self.screen_board.get_width(
        )*0.75, self.screen_board.get_height()/2 + 100)
        self.label_9_rect.center = (self.screen_board.get_width(
        ) * 0.75, self.screen_board.get_height()/2 + 90)

    
    def define_fonte(self):
        self.input_font = pygame.font.SysFont('Arial', 15)
        self.input_1.font_color = "#000000"
        self.input_1.cursor_color = "#000000"
        self.input_1.font_object = self.input_font

        self.input_2.font_color = "#000000"
        self.input_2.cursor_color = "#000000"
        self.input_2.font_object = self.input_font

        self.input_3.font_color = "#000000"
        self.input_3.cursor_color = "#000000"
        self.input_3.font_object = self.input_font

        self.input_4.font_color = "#000000"
        self.input_4.cursor_color = "#000000"
        self.input_4.font_object = self.input_font

        self.input_5.font_color = "#000000"
        self.input_5.cursor_color = "#000000"
        self.input_5.font_object = self.input_font

        self.input_6.font_color = "#000000"
        self.input_6.cursor_color = "#000000"
        self.input_6.font_object = self.input_font

        self.input_7.font_color = "#000000"
        self.input_7.cursor_color = "#000000"
        self.input_7.font_object = self.input_font

        self.input_8.font_color = "#000000"
        self.input_8.cursor_color = "#000000"
        self.input_8.font_object = self.input_font

        self.input_9.font_color = "#000000"
        self.input_9.cursor_color = "#000000"
        self.input_9.font_object = self.input_font


