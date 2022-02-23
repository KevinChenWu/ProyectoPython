class TableroPuntos:
    '''
    Hace la impresión de los puntos altos.
    '''

    def __init__(self, ahorcado):
        '''
        Se inicializan la pantalla del tablero.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

    def _titulo(self):
        '''
        Ajustes para imprimir el título de tablero.
        '''
        # Ajustes del título del Tablero a imprimir.
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
        '''
        Ajustes para imprimir el subtítulo de puntos.
        '''

        # Lectura de los puntos altos
        puntos_altos = open('highscore.txt', 'r')
        highscore = puntos_altos.read().split('\n')
        highscore = highscore[:-1]
        puntos_altos.close()
        self.highscore = highscore
        # Ajustes del subtítulo de Puntos a imprimir
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
        # Moverlo hacia abajo.
        self.puntos_rect.x -= self.puntos_rect.width / 2
        self.puntos_rect.y += self.puntos_rect.height

    def _nombres(self):
        '''
        Ajustes para imprimir el subtítulo de nombres.
        '''

        # Lectura de los nombres asociados a los puntos altos
        nombres_altos = open('highscore_nombre.txt', 'r')
        nombre_highscore = nombres_altos.read().split('\n')
        nombre_highscore = nombre_highscore[:-1]
        nombres_altos.close()
        self.highscore_nombre = nombre_highscore
        # Ajustes del subtítulo de Nombres a imprimir
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        nombres = 'Nombres'
        self.nombres = self.font.render(
            nombres, True, self.color_texto, self.color_fondo
        )
        self.nombres_rect = self.nombres.get_rect()
        self.nombres_rect.topleft = self.titulo_rect.bottomleft
        # Moverlo hacia abajo.
        self.nombres_rect.x += self.nombres_rect.width / 2
        self.nombres_rect.y += self.nombres_rect.height

    def _top1(self):
        '''
        Ajustes para imprimir los puntos del primer puesto.
        '''

        # Ajustes de los puntos de top 1 a imprimir
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
        '''
        Ajustes para imprimir los puntos del segundo puesto.
        '''

        # Ajustes de los puntos de top 2 a imprimir
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
        '''
        Ajustes para imprimir los puntos del tercer puesto.
        '''

        # Ajustes de los puntos de top 3 a imprimir
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
        '''
        Ajustes para imprimir los puntos del cuarto puesto.
        '''

        # Ajustes de los puntos de top 4 a imprimir
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
        '''
        Ajustes para imprimir los puntos del quinto puesto.
        '''

        # Ajustes de los puntos de top 5 a imprimir
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

    def _nombre1(self):
        '''
        Ajustes para imprimir el nombre del primer puesto.
        '''

        # Ajustes del nombre de top 1 a imprimir
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        nombre1 = self.highscore_nombre[0]
        self.nombre1 = self.font.render(
            nombre1, True, self.color_texto, self.color_fondo
        )
        self.nombre1_rect = self.nombre1.get_rect()
        self.nombre1_rect.topleft = self.nombres_rect.topleft
        # Moverlo hacia la abajo.
        self.nombre1_rect.y += self.nombre1_rect.height * 2

    def _nombre2(self):
        '''
        Ajustes para imprimir el nombre del segundo puesto.
        '''

        # Ajustes del nombre de top 2 a imprimir
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        nombre2 = self.highscore_nombre[1]
        self.nombre2 = self.font.render(
            nombre2, True, self.color_texto, self.color_fondo
        )
        self.nombre2_rect = self.nombre2.get_rect()
        self.nombre2_rect.topright = self.nombre1_rect.topright
        # Moverlo hacia la abajo.
        self.nombre2_rect.y += self.nombre2_rect.height * 2

    def _nombre3(self):
        '''
        Ajustes para imprimir el nombre del tercer puesto.
        '''

        # Ajustes del nombre de top 3 a imprimir
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        nombre3 = self.highscore_nombre[2]
        self.nombre3 = self.font.render(
            nombre3, True, self.color_texto, self.color_fondo
        )
        self.nombre3_rect = self.nombre3.get_rect()
        self.nombre3_rect.topright = self.nombre2_rect.topright
        # Moverlo hacia la abajo.
        self.nombre3_rect.y += self.nombre3_rect.height * 2

    def _nombre4(self):
        '''
        Ajustes para imprimir el nombre del cuarto puesto.
        '''

        # Ajustes del nombre de top 4 a imprimir
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        nombre4 = self.highscore_nombre[3]
        self.nombre4 = self.font.render(
            nombre4, True, self.color_texto, self.color_fondo
        )
        self.nombre4_rect = self.nombre4.get_rect()
        self.nombre4_rect.topright = self.nombre3_rect.topright
        # Moverlo hacia la abajo.
        self.nombre4_rect.y += self.nombre4_rect.height * 2

    def _nombre5(self):
        '''
        Ajustes para imprimir el nombre del quinto puesto.
        '''

        # Ajustes del nombre de top 5 a imprimir
        self.ancho, self.altura = 100, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (0, 0, 0)
        self.font = self.ajustes.font_score
        nombre5 = self.highscore_nombre[4]
        self.nombre5 = self.font.render(
            nombre5, True, self.color_texto, self.color_fondo
        )
        self.nombre5_rect = self.nombre5.get_rect()
        self.nombre5_rect.topright = self.nombre4_rect.topright
        # Moverlo hacia la abajo.
        self.nombre5_rect.y += self.nombre5_rect.height * 2

    def _mostrar_puntos(self):
        '''
        Dibujar el título, los subtítulos, los puntos y los nombres del tablero
        en pantalla.
        '''
        self._titulo()
        self._puntos()
        self._nombres()
        self._top1()
        self._nombre1()
        self._top2()
        self._nombre2()
        self._top3()
        self._nombre3()
        self._top4()
        self._nombre4()
        self._top5()
        self._nombre5()
        self.pantalla.blit(self.titulo, self.titulo_rect)
        self.pantalla.blit(self.puntos, self.puntos_rect)
        self.pantalla.blit(self.nombres, self.nombres_rect)
        self.pantalla.blit(self.top1, self.top1_rect)
        self.pantalla.blit(self.nombre1, self.nombre1_rect)
        self.pantalla.blit(self.top2, self.top2_rect)
        self.pantalla.blit(self.nombre2, self.nombre2_rect)
        self.pantalla.blit(self.top3, self.top3_rect)
        self.pantalla.blit(self.nombre3, self.nombre3_rect)
        self.pantalla.blit(self.top4, self.top4_rect)
        self.pantalla.blit(self.nombre4, self.nombre4_rect)
        self.pantalla.blit(self.top5, self.top5_rect)
        self.pantalla.blit(self.nombre5, self.nombre5_rect)
