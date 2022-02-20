class Stats:
    '''
    Hace rastreo de las estadísticas del juego.
    '''

    def __init__(self, ahorcado):
        '''
        Se inicializan las estadísticas.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()
        self.font = self.ajustes.font_score
        self.negro = self.ajustes.negro
        self.fondo = self.ajustes.fondo

        # Puntos actuales.
        self.puntos = 0

    def _aumentar_puntuacion(self, tamanno):
        '''
        Se aumenta la puntuación de acuerdo al tamaño de la palabra.
        '''
        if tamanno == 'cortas':
            print('Dificultad: fácil')
            self.puntos += 1
        elif tamanno == 'medianas':
            print('Dificultad: media')
            self.puntos += 2
        elif tamanno == 'largas':
            print('Dificultad: difícil')
            self.puntos += 3

    def _puntuacion_final(self):
        '''
        Se obtiene la puntuación final y se reinician los puntos a cero.
        '''
        print('Puntuación final:', self.puntos)
        self.puntos = 0

    def _scoreboard(self):
        '''
        Ajustes para dibujar el scoreboard.
        '''
        # Ir al menu.
        ESC = 'Presione Esc para devolverse al menu'
        self.volver_menu = self.font.render(
            ESC, True, self.negro, self.fondo
        )
        self.volver_menu_rect = self.volver_menu.get_rect()
        self.volver_menu_rect.bottomleft = self.pantalla_rect.bottomleft
        # Moverlo hacia la derecha.
        self.volver_menu_rect.x += self.volver_menu_rect.height
        # Comenzar de nuevo el juego.
        SPACE = 'Presione Space para volver a jugar'
        self.volver_juego = self.font.render(
            SPACE, True, self.negro, self.fondo
        )
        self.volver_juego_rect = self.volver_juego.get_rect()
        self.volver_juego_rect.bottomright = self.pantalla_rect.bottomright
        # Moverlo hacia la derecha.
        self.volver_juego_rect.x -= self.volver_juego_rect.height

    def blitme(self):
        '''
        Dibujar objetos en pantalla.
        '''
        self._scoreboard()
        self.pantalla.blit(self.volver_menu, self.volver_menu_rect)
        self.pantalla.blit(self.volver_juego, self.volver_juego_rect)
