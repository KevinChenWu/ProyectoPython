class TableroPuntos:
    def __init__(self, ahorcado):
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        self._titulo()
        self._puntos()
        self._top1()
        self._top2()
        self._top3()
        self._top4()
        self._top5()

    def _titulo(self):
        self.ancho, self.altura = 200, 25
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 255)
        self.font = self.ajustes.font_titulo

        texto = 'Tabla de puntos'
        self.titulo = self.font.render(
            texto, True, self.color_texto, self.color_fondo
        )
        self.titulo_rect = self.titulo.get_rect()
        self.titulo_rect.midtop = self.pantalla_rect.midtop
        # Moverlo hacia la abajo.
        self.titulo_rect.y += self.titulo_rect.height * 2

    def _puntos(self):
        puntos_altos = open('highscore.txt', 'r')
        highscore = puntos_altos.read().split('\n')
        highscore = highscore[:-1]
        puntos_altos.close()
        self.highscore = highscore

        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        puntos = 'Puntos'
        self.puntos = self.font.render(
            puntos, True, self.color_texto, self.color_fondo
        )
        self.puntos_rect = self.puntos.get_rect()
        self.puntos_rect.topright = self.titulo_rect.bottomright
        # Moverlo hacia la abajo.
        self.puntos_rect.x -= self.puntos_rect.width / 2
        self.puntos_rect.y += self.puntos_rect.height

    def _top1(self):
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        texto1 = self.highscore[0]
        self.top1 = self.font.render(
            texto1, True, self.color_texto, self.color_fondo
        )
        self.top1_rect = self.top1.get_rect()
        self.top1_rect.topright = self.puntos_rect.topright
        # Moverlo hacia la abajo.
        self.top1_rect.y += self.top1_rect.height * 2

    def _top2(self):
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        texto2 = self.highscore[1]
        self.top2 = self.font.render(
            texto2, True, self.color_texto, self.color_fondo
        )
        self.top2_rect = self.top2.get_rect()
        self.top2_rect.topright = self.top1_rect.topright
        # Moverlo hacia la abajo.
        self.top2_rect.y += self.top2_rect.height * 2

    def _top3(self):
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        texto3 = self.highscore[2]
        self.top3 = self.font.render(
            texto3, True, self.color_texto, self.color_fondo
        )
        self.top3_rect = self.top3.get_rect()
        self.top3_rect.topright = self.top2_rect.topright
        # Moverlo hacia la abajo.
        self.top3_rect.y += self.top3_rect.height * 2

    def _top4(self):
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        texto4 = self.highscore[3]
        self.top4 = self.font.render(
            texto4, True, self.color_texto, self.color_fondo
        )
        self.top4_rect = self.top4.get_rect()
        self.top4_rect.topright = self.top3_rect.topright
        # Moverlo hacia la abajo.
        self.top4_rect.y += self.top4_rect.height * 2

    def _top5(self):
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        texto5 = self.highscore[4]
        self.top5 = self.font.render(
            texto5, True, self.color_texto, self.color_fondo
        )
        self.top5_rect = self.top5.get_rect()
        self.top5_rect.topright = self.top4_rect.topright
        # Moverlo hacia la abajo.
        self.top5_rect.y += self.top5_rect.height * 2

    def _mostrar_puntos(self):
        self.pantalla.blit(self.titulo, self.titulo_rect)
        self.pantalla.blit(self.puntos, self.puntos_rect)
        self.pantalla.blit(self.top1, self.top1_rect)
        self.pantalla.blit(self.top2, self.top2_rect)
        self.pantalla.blit(self.top3, self.top3_rect)
        self.pantalla.blit(self.top4, self.top4_rect)
        self.pantalla.blit(self.top5, self.top5_rect)
