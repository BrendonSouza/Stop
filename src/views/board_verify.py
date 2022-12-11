import pygame
import pygame_textinput
import json




class Verify_board:
    def __init__(self, main, screen, client):
        self.screen_board = screen
        self.main = main
        self.exit = False
        self.client = client
        self.end = False
        self.responsesForValidate = {}
        self.invalid_responses = {}
        self.color_rect1 = (255, 255, 255)
        self.color_rect2 = (255, 255, 255)
        self.color_rect3 = (255, 255, 255)
        self.color_rect4 = (255, 255, 255)
        self.color_rect5 = (255, 255, 255)
        self.color_rect6 = (255, 255, 255)
        self.color_rect7 = (255, 255, 255)
        self.color_rect8 = (255, 255, 255)
        self.color_rect9 = (255, 255, 255)

        self.define_rect_and_subsurfaces()

    def define_rect_and_subsurfaces(self):
        self.retangulo_1 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_2 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_3 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_4 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_5 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_6 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_7 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_8 = pygame.Rect(0, 0, 170, 30)
        self.retangulo_9 = pygame.Rect(0, 0, 170, 30)

        
        self.retangulo_1.center = (
            self.screen_board.get_width()/4, self.screen_board.get_height()/2 - 100)
       

        self.retangulo_2.center = (self.screen_board.get_width(
        )*0.5, self.screen_board.get_height()/2 - 100)
        
        self.retangulo_3.center = (self.screen_board.get_width(
        )*0.75, self.screen_board.get_height()/2 - 100)
        
        self.retangulo_4.center = (
            self.screen_board.get_width()/4, self.screen_board.get_height()/2)
       
        self.retangulo_5.center = (
            self.screen_board.get_width()*0.5, self.screen_board.get_height()/2)
        self.retangulo_6.center = (
            self.screen_board.get_width()*0.75, self.screen_board.get_height()/2)
        
        self.retangulo_7.center = (
            self.screen_board.get_width()/4, self.screen_board.get_height()/2 + 100)
       
        self.retangulo_8.center = (self.screen_board.get_width(
        )*0.5, self.screen_board.get_height()/2 + 100)
        self.retangulo_9.center = (self.screen_board.get_width(
        )*0.75, self.screen_board.get_height()/2 + 100)

        self.textFont = pygame.font.SysFont("Arial", 15)

    def run(self):
        self.responsesForValidate = self.client.responsesForValidate
        while True:
           
            self.screen_board.fill((148, 0, 211))
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    print("Saindo...")
                    self.client.destroy()
                    exit()
            if(not self.end):
            # itera no dictionario de respostas
                
                i=-1
                keys = list(self.responsesForValidate.keys())
                for value in self.responsesForValidate.values(): 
                    self.screen_board.fill((148, 0, 211))
                    i+=1
                    text_Title = self.textFont.render(keys[i], True, "#ffffff")
                    text_Title_rect = text_Title.get_rect()
                    text_Title_rect.center = (self.screen_board.get_width()/2, 75)
                    self.screen_board.blit(text_Title, text_Title_rect)
                    pygame.display.update()
                    # inicia um clock aqui e faz um while o clock for != 15
                    clock = pygame.time.Clock()
                    pygame.time.set_timer(pygame.USEREVENT, 1000)
                    counter = 5
                    changeContent = True
                    self.reset_rect_color()
                    while changeContent:
                        pygame.draw.rect(self.screen_board, self.color_rect1, self.retangulo_1)
                        pygame.draw.rect(self.screen_board, self.color_rect2, self.retangulo_2)
                        text_1 = self.textFont.render(value[0], True, "#000000")     
                        text_1_rect = text_1.get_rect()
                        text_1_rect.center = self.retangulo_1.center
                        text_2 = self.textFont.render(value[1], True, "#000000")
                        text_2_rect = text_2.get_rect()
                        text_2_rect.center = self.retangulo_2.center
                        self.screen_board.blit(text_1, text_1_rect)
                        self.screen_board.blit(text_2, text_2_rect)
                        if(self.client.number_of_players >= 3):
                            pygame.draw.rect(self.screen_board, self.color_rect3, self.retangulo_3)
                            text_3 = self.textFont.render(value[2], True, "#000000")
                            text_3_rect = text_3.get_rect()
                            text_3_rect.center = self.retangulo_3.center
                            self.screen_board.blit(text_3, text_3_rect)
                        if(self.client.number_of_players >= 4):
                            pygame.draw.rect(self.screen_board, self.color_rect4, self.retangulo_4)
                            text_4 = self.textFont.render(value[3], True, "#000000")
                            text_4_rect = text_4.get_rect()
                            text_4_rect.center = self.retangulo_4.center
                            self.screen_board.blit(text_4, text_4_rect)
                        if(self.client.number_of_players >= 5):
                            pygame.draw.rect(self.screen_board, self.color_rect5, self.retangulo_5)
                            text_5 = self.textFont.render(value[4], True, "#000000")
                            text_5_rect = text_5.get_rect()
                            text_5_rect.center = self.retangulo_5.center
                            self.screen_board.blit(text_5, text_5_rect)
                        if(self.client.number_of_players >= 6):
                            pygame.draw.rect(self.screen_board, self.color_rect6, self.retangulo_6)
                            text_6 = self.textFont.render(value[5], True, "#000000")
                            text_6_rect = text_6.get_rect()
                            text_6_rect.center = self.retangulo_6.center
                            self.screen_board.blit(text_6, text_6_rect)
                        if(self.client.number_of_players >= 7):
                            pygame.draw.rect(self.screen_board, self.color_rect7, self.retangulo_7)
                            text_7 = self.textFont.render(value[6], True, "#000000")
                            text_7_rect = text_7.get_rect()
                            text_7_rect.center = self.retangulo_7.center
                            self.screen_board.blit(text_7, text_7_rect)
                        if(self.client.number_of_players >= 8):
                            pygame.draw.rect(self.screen_board, self.color_rect8, self.retangulo_8)
                            text_8 = self.textFont.render(value[7], True, "#000000")
                            text_8_rect = text_8.get_rect()
                            text_8_rect.center = self.retangulo_8.center
                            self.screen_board.blit(text_8, text_8_rect)
                        if(self.client.number_of_players == 9):
                            pygame.draw.rect(self.screen_board, self.color_rect9, self.retangulo_9)
                            text_9 = self.textFont.render(value[8], True, "#000000")
                            text_9_rect = text_9.get_rect()
                            text_9_rect.center = self.retangulo_9.center
                            self.screen_board.blit(text_9, text_9_rect)
                        self.events = pygame.event.get()
                        coord_x, coord_y = pygame.mouse.get_pos()
                        for event in self.events:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                self.verify_click_in_input(coord_x,coord_y,keys[i],value)
                            if(event.type == pygame.USEREVENT):
                                counter -= 1
                                print(counter)
                                if(counter<=0):
                                    changeContent = False
                                    break
                        clock.tick(60)
                        pygame.display.update()
                self.end = True
                response = {
                    "data":{
                        "type":"invalid_responses",
                        "responses": self.invalid_responses
                    }
                }
                self.client.envia_mensagem(json.dumps(response))
            
               
            text_end = self.textFont.render("FIM DO JOGO", True, "#ffffff") 
            text_end_rect = text_end.get_rect()
            text_end_rect.center = (self.screen_board.get_width()/2, self.screen_board.get_height()*0.25)
            self.screen_board.blit(text_end, text_end_rect)

            
            if(len(self.client.ranking) ==0):
                text_await_server = self.textFont.render("Aguardando cálculo do ranking...", True, "#ffffff") 
                text_await_server_rect = text_await_server.get_rect()
                text_await_server_rect.center = (self.screen_board.get_width()/2, self.screen_board.get_height()/2+100)
                self.screen_board.blit(text_await_server, text_await_server_rect)
                pygame.display.flip()
            else:
                text_ranking = self.textFont.render("Ranking: ", True, "#ffffff")
                text_ranking_rect = text_ranking.get_rect()
                text_ranking_rect.center = (self.screen_board.get_width()/2, self.screen_board.get_height()/2+100)
                self.screen_board.blit(text_ranking, text_ranking_rect)
                i=0
                for player in self.client.ranking:
                    i+=1
                    text_ranking = self.textFont.render(str(i)+" - "+ player["name"] + "  --------  " + str(player["score"]), True, "#ffffff")
                    text_ranking_rect = text_ranking.get_rect()
                    text_ranking_rect.center = (self.screen_board.get_width()/2, self.screen_board.get_height()/2+100+i*20)
                    self.screen_board.blit(text_ranking, text_ranking_rect)
                                    
                

            pygame.display.update()
    
    def reset_rect_color(self):
        self.color_rect1 = (255, 255, 255)
        self.color_rect2 = (255, 255, 255)
        self.color_rect3 = (255, 255, 255)
        self.color_rect4 = (255, 255, 255)
        self.color_rect5 = (255, 255, 255)
        self.color_rect6 = (255, 255, 255)
        self.color_rect7 = (255, 255, 255)
        self.color_rect8 = (255, 255, 255)
        self.color_rect9 = (255, 255, 255)
        
    def verify_click_in_input(self,coord_x,coord_y,key,value):
        if self.retangulo_1.collidepoint(coord_x, coord_y):
            #change color background to yellow
            self.color_rect1 = (255,255,0)
            self.add_response(key,value[0])
        elif self.retangulo_2.collidepoint(coord_x, coord_y):
            self.color_rect2 = (255,255,0)
            self.add_response(key,value[1])
        elif self.retangulo_3.collidepoint(coord_x, coord_y):
            self.color_rect3 = (255,255,0)
            self.add_response(key,value[2])
        elif self.retangulo_4.collidepoint(coord_x, coord_y):
            self.color_rect4 = (255,255,0)
            self.add_response(key,value[3])
        elif self.retangulo_5.collidepoint(coord_x, coord_y):
            self.color_rect5 = (255,255,0)
            self.add_response(key,value[4])
        elif self.retangulo_6.collidepoint(coord_x, coord_y):
            self.color_rect6 = (255,255,0)
            self.add_response(key,value[5])
        elif self.retangulo_7.collidepoint(coord_x, coord_y):
            self.color_rect7 = (255,255,0)
            self.add_response(key,value[6])
        elif self.retangulo_8.collidepoint(coord_x, coord_y):
            self.color_rect8 = (255,255,0)
            self.add_response(key,value[7])
        elif self.retangulo_9.collidepoint(coord_x, coord_y):
            self.color_rect9 = (255,255,0)
            self.add_response(key,value[8])
            
            

    def add_response(self, key, value):
        if key in self.invalid_responses.keys():
            self.invalid_responses[key].append(value)
        else:
            self.invalid_responses[key] = [value]
    

