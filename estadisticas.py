class Stats:
    '''
    Hace rastreo de las estadísticas del juego.
    '''

    def __init__(self, ahorcado):
        '''
        Se inicializan las estadísticas.
        '''
        self.ajustes = ahorcado.ajustes
        self.juego_activo = True

    def _aumentar_puntuacion(self, tamanno):
        '''
        Se aumenta la puntuación de acuerdo al tamaño de la palabra.
        '''
        if tamanno == 'cortas':
            print('Dificultad: fácil')
        elif tamanno == 'medianas':
            print('Dificultad: media')
        elif tamanno == 'largas':
            print('Dificultad: difícil')
