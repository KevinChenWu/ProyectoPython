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
        PUNTOS = 'Puntos: {}'.format(self.puntos)
        self.puntaje = self.font.render(
            PUNTOS, True, self.negro, self.fondo
        )
        self.puntaje_rect = self.puntaje.get_rect()
        self.puntaje_rect.topleft = self.pantalla_rect.topleft
        self.puntaje_rect.x += self.puntaje_rect.height
        self.puntaje_rect.y += self.puntaje_rect.height

    def _aumentar_puntuacion(self, tamanno):
        '''
        Se aumenta la puntuación de acuerdo al tamaño de la palabra.
        '''
        if tamanno == 'cortas':
            print('Dificultad: fácil')
            self.puntos += 25
        elif tamanno == 'medianas':
            print('Dificultad: media')
            self.puntos += 50
        elif tamanno == 'largas':
            print('Dificultad: difícil')
            self.puntos += 100
        self._actualizar_puntos()

    def _puntuacion_final(self):
        '''
        Se obtiene la puntuación final y se reinician los puntos a cero.
        '''
        puntos_altos = open('highscore.txt', 'r+')
        highscore = puntos_altos.read().split('\n')
        highscore = highscore[:-1]
        self.highscore = [int(numero) for numero in highscore]
        for i in range(5):
            if self.puntos > self.highscore[i]:
                self.highscore.insert(i, self.puntos)
                self.highscore.pop()
                break
        highscore = [str(num) for num in self.highscore]
        highscore.append('')
        highscore = '\n'.join(highscore)
        puntos_altos.seek(0)
        puntos_altos.write(highscore)
        puntos_altos.truncate()
        puntos_altos.close()
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

    def _actualizar_puntos(self):
        '''
        Actualizar los puntos.
        '''
        PUNTOS = 'Puntos: {}'.format(self.puntos)
        self.puntaje = self.font.render(
            PUNTOS, True, self.negro, self.fondo
        )

    def blit_puntos(self):
        '''
        Dibujar los puntos en pantalla.
        '''
        self.pantalla.blit(self.puntaje, self.puntaje_rect)
