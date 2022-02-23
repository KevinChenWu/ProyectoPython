import pygame


class BotonSalir:

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para desplegar la imagen del muñeco.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        # Se modifican los parametros del boton salir,
        # tales como el ancho, color, fondo y color de texto

        self.ancho, self.altura = 200, 50
        self.color_boton = (255, 255, 255)
        self.color_texto = (163, 73, 164)
        self.font = self.ajustes.font_menu

        # Se modifica la posicion en el eje Y

        self.rect = pygame.Rect(0, 0, self.ancho, self.altura)
        self.rect.center = self.pantalla_rect.center
        self.rect.y += self.rect.height * 2

        self._boton_salir()

    def _boton_salir(self):
        '''
        Se muestra el mensaje del boton, ademas de centrarlo el mismo.
        '''
        msg = 'Salir'
        self.mensaje = self.font.render(
            msg, True, self.color_texto, self.color_boton
        )
        self.mensaje_rect = self.mensaje.get_rect()
        self.mensaje_rect.center = self.rect.center

    def _dibujar_boton(self):
        '''
        Con  blit se vuelca la imagen en la pantalla.
        '''
        self.pantalla.blit(self.mensaje, self.mensaje_rect)
