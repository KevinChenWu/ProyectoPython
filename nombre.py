import pygame


class Nombre:

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para desplegar la imagen del muñeco.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        self.ancho, self.altura = 200, 50
        self.color_fondo = (230, 230, 230)
        self.color_texto = (0, 0, 0)
        self.color_blanco = (255, 255, 255)

        self.rect = pygame.Rect(0, 0, self.ancho, self.altura)
        self.rect.center = self.pantalla_rect.center

        texto = ahorcado.texto_usuario

        self._rect_nombre(texto)
        self._introducir()
        self._ganaste()
        self._perdiste()

    def _rect_nombre(self, texto_usuario):
        font = self.ajustes.font_nombre
        self.texto = font.render(
            texto_usuario, True, self.color_texto, self.color_fondo
        )
        self.texto_rect = self.texto.get_rect()
        self.texto_rect.center = self.rect.center
        # Rectángulo para texto
        self.input_rect = pygame.Rect(0, 0, 200, 60)
        self.input_rect.center = self.rect.center

    def _introducir(self):
        texto = 'Introduzca su nombre:'
        font = self.ajustes.font_nombre
        self.intro = font.render(
            texto, True, self.color_texto, self.ajustes.blanco
        )
        self.intro_rect = self.intro.get_rect()
        self.intro_rect.center = self.pantalla_rect.center
        # Moverlo hacia la arriba.
        self.intro_rect.y -= self.intro_rect.height * 1.5

    def _perdiste(self):
        texto = 'Perdiste'
        font = self.ajustes.font_titulo
        self.perdiste = font.render(
            texto, True, self.ajustes.rojo, self.ajustes.blanco
        )
        self.perdiste_rect = self.perdiste.get_rect()
        self.perdiste_rect.center = self.pantalla_rect.center
        # Moverlo hacia la arriba.
        self.perdiste_rect.y -= self.perdiste_rect.height * 3

    def _ganaste(self):
        texto = 'Ganaste'
        font = self.ajustes.font_titulo
        self.ganaste = font.render(
            texto, True, self.ajustes.verde, self.ajustes.blanco
        )
        self.ganaste_rect = self.ganaste.get_rect()
        self.ganaste_rect.center = self.pantalla_rect.center
        # Moverlo hacia la arriba.
        self.ganaste_rect.y -= self.ganaste_rect.height * 3

    def _dibujar_texto(self, ganaste):
        # Dibujar Rectángulo
        pygame.draw.rect(self.pantalla, self.color_fondo, self.input_rect)
        # Dibujar el botón
        self.pantalla.blit(self.texto, self.texto_rect)
        self.pantalla.blit(self.intro, self.intro_rect)
        if ganaste:
            self.pantalla.blit(self.ganaste, self.ganaste_rect)
        else:
            self.pantalla.blit(self.perdiste, self.perdiste_rect)
