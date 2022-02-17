import pygame


class Munneco:
    '''
    Clase para actualizar la imagen del muñeco.
    '''

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para desplegar la imagen del muñeco.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        self.munneco_x = self.ajustes.munneco_tamanno_x
        self.munneco_y = self.ajustes.munneco_tamanno_y

        # Se carga la imagen inicial para el muñeco.
        self.image = pygame.image.load('imagenes/ahorcado_0.png')
        self.image = pygame.transform.scale(
            self.image, (self.munneco_x, self.munneco_y)
        )
        self.rect = self.image.get_rect()

        # Posición del muñeco en la pantalla.
        self.rect.topright = self.pantalla_rect.topright

    def actualizar_munneco(self, cont_fallos):
        '''
        Se actualiza la imagen del munneco con cada fallo.
        '''
        # Hay que mejorarlo para que con cada fallo cambie de imagen.
        # Puede ser con un format, donde se pase al siguiente número de imagen.
        nombre_imagen = 'imagenes/ahorcado_{}.png'.format(cont_fallos)
        self.image = pygame.image.load(nombre_imagen)
        self.image = pygame.transform.scale(
            self.image, (self.munneco_x, self.munneco_y)
        )

    def blitme(self):
        '''
        Dibujar el munneco en pantalla
        '''
        self.pantalla.blit(self.image, self.rect)
