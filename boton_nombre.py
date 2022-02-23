import pygame


class BotonNombre:

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para que el jugador presione el botón para
        introducir el nombre.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        self.ancho, self.altura = 200, 50
        self.color_boton = self.ajustes.rojo
        self.color_texto = self.ajustes.blanco
        self.font = self.ajustes.font_menu

        self.rect = pygame.Rect(0, 0, self.ancho, self.altura)
        self.rect.center = self.pantalla_rect.center
        self.rect.y += self.rect.height * 2

        self._boton_nombre()

    def _boton_nombre(self):
        '''
        Texto dentro del botón.
        '''
        msg = 'Continuar'
        self.mensaje = self.font.render(
            msg, True, self.color_texto, self.color_boton
        )
        self.mensaje_rect = self.mensaje.get_rect()
        self.mensaje_rect.center = self.rect.center

    def _dibujar_boton(self):
        '''
        Se dibuja el botón.
        '''
        pygame.draw.rect(self.pantalla, self.color_boton, self.rect)
        self.pantalla.blit(self.mensaje, self.mensaje_rect)
