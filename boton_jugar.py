#Se importan las librerias necesarias

import pygame


class BotonJugar:

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para desplegar la imagen del muñeco.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()
        '''
        Se modifican parametros del boton, como el color del color_texto
        ancho, color de fondo
        '''
        self.ancho, self.altura = 200, 50
        self.color_boton = (255, 255, 255)
        self.color_texto = (163, 73, 164)
        self.font = self.ajustes.font_menu
        '''
        Se modifica la posicion en el eje Y
        '''
        self.rect = pygame.Rect(0, 0, self.ancho, self.altura)
        self.rect.center = self.pantalla_rect.center
        self.rect.y -= self.rect.height * 2

        self._boton_jugar()

         '''
         Aca se define el mensaje a mostrar en dicho boton
         '''
    def _boton_jugar(self):
        msg = 'Jugar'
        self.mensaje = self.font.render(
            msg, True, self.color_texto, self.color_boton
        )
        self.mensaje_rect = self.mensaje.get_rect()
        self.mensaje_rect.center = self.rect.center
       '''
       Con blit se dibuja el boton en la pantalla
       '''
    def _dibujar_boton(self):
        # Dibujar el botón
        self.pantalla.blit(self.mensaje, self.mensaje_rect)
