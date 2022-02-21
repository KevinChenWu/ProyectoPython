class Menu:

    def __init__(self, ahorcado):
        '''
        Se inicializa los ajustes para desplegar la imagen del muñeco.
        '''
        self.pantalla = ahorcado.pantalla
        self.ajustes = ahorcado.ajustes
        self.pantalla_rect = ahorcado.pantalla.get_rect()

        self._titulo()
        self._creadores()
        self._creador1()
        self._creador2()
        self._creador3()

    def _titulo(self):
        self.ancho, self.altura = 200, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (163, 0, 0)
        self.font = self.ajustes.font_titulo

        texto = 'Py Ahorcado'
        self.titulo = self.font.render(
            texto, True, self.color_texto, self.color_fondo
        )
        self.titulo_rect = self.titulo.get_rect()
        self.titulo_rect.midtop = self.pantalla_rect.midtop
        # Moverlo hacia la abajo.
        self.titulo_rect.y += self.titulo_rect.height

    def _creadores(self):
        self.ancho, self.altura = 200, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (163, 0, 0)
        self.font = self.ajustes.font_score

        texto = 'Creadores:'

        self.creadores = self.font.render(
            texto, True, self.color_texto, self.color_fondo
        )
        self.creadores_rect = self.creadores.get_rect()
        self.creadores_rect.bottomright = self.pantalla_rect.bottomright
        # Moverlo hacia la arriba.
        self.creadores_rect.y -= self.creadores_rect.height * 7
        self.creadores_rect.x -= self.creadores_rect.height

    def _creador1(self):
        self.ancho, self.altura = 200, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (163, 0, 0)
        self.font = self.ajustes.font_score

        texto = 'Kevin Chen'

        self.creador1 = self.font.render(
            texto, True, self.color_texto, self.color_fondo
        )
        self.creador1_rect = self.creador1.get_rect()
        self.creador1_rect.bottomright = self.pantalla_rect.bottomright
        # Moverlo hacia la arriba.
        self.creador1_rect.y -= self.creador1_rect.height * 5
        self.creador1_rect.x -= self.creador1_rect.height

    def _creador2(self):
        self.ancho, self.altura = 200, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (163, 0, 0)
        self.font = self.ajustes.font_score

        texto = 'Javier Saca'

        self.creador2 = self.font.render(
            texto, True, self.color_texto, self.color_fondo
        )
        self.creador2_rect = self.creador2.get_rect()
        self.creador2_rect.bottomright = self.pantalla_rect.bottomright
        # Moverlo hacia la arriba.
        self.creador2_rect.y -= self.creador2_rect.height * 3
        self.creador2_rect.x -= self.creador2_rect.height

    def _creador3(self):
        self.ancho, self.altura = 200, 50
        self.color_fondo = (255, 255, 255)
        self.color_texto = (163, 0, 0)
        self.font = self.ajustes.font_score

        texto = 'Jorge Sancho'

        self.creador3 = self.font.render(
            texto, True, self.color_texto, self.color_fondo
        )
        self.creador3_rect = self.creador3.get_rect()
        self.creador3_rect.bottomright = self.pantalla_rect.bottomright
        # Moverlo hacia la arriba.
        self.creador3_rect.y -= self.creador3_rect.height
        self.creador3_rect.x -= self.creador3_rect.height

    def _dibujar_menu(self):
        # Dibujar el botón
        self.pantalla.blit(self.titulo, self.titulo_rect)
        self.pantalla.blit(self.creadores, self.creadores_rect)
        self.pantalla.blit(self.creador1, self.creador1_rect)
        self.pantalla.blit(self.creador2, self.creador2_rect)
        self.pantalla.blit(self.creador3, self.creador3_rect)
