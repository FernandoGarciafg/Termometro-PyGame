import pygame, sys
from pygame.locals import *

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__pantalla = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__pantalla.fill((244, 236, 203))
        
    def __cerrar(self):
        pygame.quit()
        sys.exit()
        
    def comenzar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__cerrar()
                    
            pygame.display.flip()
            
   
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.comenzar()
    

        