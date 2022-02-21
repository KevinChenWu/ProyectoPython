import pygame


class Ajustes:
    '''
    Clase donde se define los ajustes del juego ahorcado.
    '''
    def __init__(self):
        '''
        Se inicializa los ajustes del juego.
        '''
        # Colores.
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)
        self.gris_claro = (230, 230, 230)
        self.verde = (0, 255, 0)
        self.rojo = (255, 0, 0)
        self.fondo = self.blanco  # Color utilizdo para el fondo.

        # Configuración de la pantalla
        self.pantalla_ancho = 1200
        self.pantalla_altura = 570
        self.bg_color = self.fondo  # Color del fondo.

        # Configuración de las letras.
        self.font_abecedario = pygame.font.Font(None, 50)
        self.font_palabra = pygame.font.Font(None, 50)
        self.font_menu = pygame.font.Font(None, 50)
        self.font_score = pygame.font.Font(None, 30)
        self.font_titulo = pygame.font.Font(None, 70)

        # Abecedario.
        self.abecedario_completo = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q',
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        # Configuración de la imagen del muñeco.
        self.munneco_tamanno_x = 287
        self.munneco_tamanno_y = 300
