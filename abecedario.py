from pygame.sprite import Sprite


class Abecedario(Sprite):
    '''
    Clase que forma una de las letras del abecedario.
    '''

    def __init__(self, ahorcado, letra):
        '''
        Se inicializa las letras del abecedario y se le da una posición
        inicial.
        '''
        super().__init__()
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        # Ajustes.
        self.negro = self.ajustes.negro
        self.fondo = self.ajustes.fondo
        self.verde = self.ajustes.verde
        self.rojo = self.ajustes.rojo
        self.font = self.ajustes.font_abecedario

        self.image = self.font.render(
            str(letra), True, self.negro, self.fondo
        )
        self.rect = self.image.get_rect()

        # Se coloca la letra en la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.pantalla_rect.bottom - (self.rect.height * 6)

    def blitme(self):
        '''
        Dibujar la letra en la posición actual.
        '''
        self.pantalla.blit(self.image, self.rect)

    def acierto(self, letra):
        '''
        Colorear letra en verde.
        Está en la palabra por adivinar.
        '''
        self.image = self.font.render(
            str(letra), True, self.verde, self.fondo
        )

    def fallo(self, letra):
        '''
        Colorear letra en rojo.
        No está en la palabra por adivinar.
        '''
        self.image = self.font.render(
            str(letra), True, self.rojo, self.fondo
        )
