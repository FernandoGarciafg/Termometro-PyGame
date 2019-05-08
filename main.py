import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.disfraz = pygame.image.load('imagenes/termo1.png')
        
    def convertir(self, grados, aUnidad):
        resultado = 0
        if aUnidad == "f":
            resultado = grados * 9/5 + 32
        elif aUnidad == "c":
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return "{:10.2f}".format(resultado)
        
class Selector():
    __unidad = None
    
    def __init__(self, unidad = "c"):
        self.__disfraces = []
        self.__disfraces.append(pygame.image.load("imagenes/posiF.png"))
        self.__disfraces.append(pygame.image.load("imagenes/posiC.png"))
        
        self.__unidad = unidad
        
    def disfraz(self):# ej de metodo getter
        if self.__unidad == "f":
            return self.__disfraces[0]
        elif self.__unidad == "c":
            return self.__disfraces[1]
        
    def cambiar(self):
        if self.__unidad == "f":
            self.__unidad = "c"
        else:
            self.__unidad = "f"
            
    def unidad(self):
        return self.__unidad
        
class NumeroEntrada():
    __valor = 0
    __strValor = ""
    __posicion = [0, 0]
    __tamaño = [0, 0]
    __contadorPuntos = 0
    
    def __init__(self, valor = 0):
        self.__fuente = pygame.font.SysFont('Arial', 24)
        self.valor(valor)
        """
        try:
            self.__valor = int(valor)
            self.__strValor = str(valor)
        except:
            pass
            """
    
    def en_evento(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValor) < 10 or (event.unicode == "." and self.__contadorPuntos == 0):
                self.__strValor += event.unicode
                self.valor(self.__strValor)
                if event.unicode == ".":
                    self.__contadorPuntos += 1
            elif event.key == K_BACKSPACE:
                if self.__strValor[-1] == ".":
                    self.__contadorPuntos -=1
                self.__strValor = self.__strValor[0:-1]
                self.valor(self.__strValor)
    
    def render(self):
        bloqueTexto = self.__fuente.render(self.__strValor, True, (74, 74, 74))
        rectangulo = bloqueTexto.get_rect()
        rectangulo.left = self.__posicion[0]
        rectangulo.top = self.__posicion[1]
        rectangulo.size = self.__tamaño
        
        #return {
            #'fondo': rectangulo,
            #'texto': bloqueTexto
            #}
        return (rectangulo, bloqueTexto)
        
    def valor(self, valor=None):
        if valor == None:
            return self.__valor
        else:
            valor = str(valor)
            try:
                self.__valor = float(valor)
                self.__strValor = valor
                if "." in self.__strValor:
                    self.__contadorPuntos = 1
                else:
                    self.__contadorPuntos = 0
            except:
                pass
            
    def ancho(self, valor = None):
        if valor == None:
            return self.__tamaño[0]
        else:
            try:
                self.__tamaño[0] = int(valor)
            except:
                pass
            
    def alto(self, valor = None):
        if valor == None:
            return self.__tamaño[1]
        else:
            try:
                self.__tamaño[1] = int(valor)
            except:
                pass
            
    def posicionX(self, valor = None):
        if valor == None:
            return self.__posicion[0]
        else:
            try:
                self.__posicion[0] = int(valor)
            except:
                pass
            
    def posicionY(self, valor = None):
        if valor == None:
            return self.__posicion[1]
        else:
            try:
                self.__posicion[1] = int(valor)
            except:
                pass
            
    def posicion(self, valor = None):
        if valor == None:
            return self.__posicion
        else:
            try:
                posicionX = int(valor[0])
                posicionY = int(valor[1])
                self.__posicion = [int(valor[0]), int(valor[1])]
            except:
                pass
        
    def tamaño(self, valor = None):
        if valor == None:
            return self.__tamaño
        else:
            try:
                ancho = int(valor[0])
                alto = int(valor[1])
                self.__tamaño = [int(valor[0]), int(valor[1])]
            except:
                pass

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__pantalla = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termometro")
        self.__pantalla.fill((244, 236, 203))
        
        self.termometro = Termometro()
        self.entrada = NumeroEntrada(0)
        self.entrada.posicion((106, 58))
        self.entrada.tamaño((133, 28))
        
        self.selector = Selector()
        
    def __cerrar(self):
        pygame.quit()
        sys.exit()
        
    def comenzar(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__cerrar()
                
                self.entrada.en_evento(event)
                #if event.type == KEYDOWN:
                    #if event.unicode in '0123456789':
                        
                    # if event.isdigit()
                if event.type == pygame.MOUSEBUTTONDOWN:    
                    self.selector.cambiar()
                    grados = self.entrada.valor()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.valor(temperatura)
                    
            # repintamos el fondo de pantalla
            self.__pantalla.fill((244, 236, 203))        
            # pintamos el termometro en su posicion
            self.__pantalla.blit(self.termometro.disfraz, (50, 34))
            # pintamos el cuadro de texto
            texto = self.entrada.render() # obtenemos el rectangulo blanco y la foto del texto y lo asignamos a la var texto
            pygame.draw.rect(self.__pantalla, (255, 255, 255), texto[0]) # creamos el rectangulo blanco en su posicion y lo pintamos con sus datos posicion y tamaño
            self.__pantalla.blit(texto[1], self.entrada.posicion()) # pintamos la foto del texto en su posicion
            # pintamos el selector
            self.__pantalla.blit(self.selector.disfraz(), (112, 153))
            
            pygame.display.flip()
            
   
if __name__ == '__main__':
    pygame.font.init()
    app = mainApp()
    app.comenzar()
    

        