from pygame.sprite import Sprite


class Letra(Sprite):
    '''
    Clase que forma una de las letras de la palabra a adivinar.
    '''

    def __init__(self, ahorcado, letra):
        '''
        Se inicializa las letras de la palabra y se le da una posición inicial.
        '''
        super().__init__()
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        # Ajustes.
        self.negro = self.ajustes.negro
        self.fondo = self.ajustes.fondo
        self.font = self.ajustes.font_palabra

        # Configuración de la letra.
        self.image = self.font.render(
            str(letra), True, self.negro, self.fondo
        )
        self.rect = self.image.get_rect()

        # Se coloca la letra en la pantalla.
        self.rect.midleft = self.pantalla_rect.midleft

    def blitme(self):
        '''
        Dibujar la letra en la posición actual.
        '''
        self.pantalla.blit(self.image, self.rect)

    def actualizar(self, letra):
        '''
        Actualización del reglón por la letra adivinada en la palabra.
        '''
        self.image = self.font.render(
            str(letra), True, self.negro, self.fondo
        )
