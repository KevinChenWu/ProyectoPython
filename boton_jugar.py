import pygame


class BotonJugar:

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para desplegar la imagen del muñeco.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        self.ancho, self.altura = 200, 50
        self.color_boton = (255, 0, 0)
        self.color_texto = (255, 255, 255)
        self.font = self.ajustes.font_menu

        self.rect = pygame.Rect(0, 0, self.ancho, self.altura)
        self.rect.center = self.pantalla_rect.center

        self._boton_jugar()

    def _boton_jugar(self):
        msg = 'Jugar'
        self.mensaje = self.font.render(
            msg, True, self.color_texto, self.color_boton
        )
        self.mensaje_rect = self.mensaje.get_rect()
        self.mensaje_rect.center = self.rect.center

    def _dibujar_boton(self):
        # Dibujar el botón
        self.pantalla.blit(self.mensaje, self.mensaje_rect)