#!/usr/bin/python3

import sys

import pygame

import re

import random

from ajustes import Ajustes

from letra import Letra

from abecedario import Abecedario

from munneco import Munneco

from estadisticas import Stats

from boton_jugar import BotonJugar


class Ahorcado:
    '''
    Clase que maneja las características del juego Ahoracado.
    '''
    def __init__(self):
        '''
        Inicialización del juego y creación de recursos.
        '''
        # Inicialización de la configuración de pygame.
        pygame.init()

        # Importar ajustes.
        self.ajustes = Ajustes()

        # Se crea la pantalla del juego.
        self.pantalla = pygame.display.set_mode(
            (self.ajustes.pantalla_ancho, self.ajustes.pantalla_altura)
        )
        pygame.display.set_caption('Ahorcado')

        self.boton_jugar = BotonJugar(self)

        self.juego_activo = False

        self.score = False

        self.stats = Stats(self)

        self.puntero_palabra = 0

        self.lista_palabras = []
        self._cargar_palabras()

    def _init_juego(self):
        '''
        Se inicia el juego cuando se le da al botón jugar y se pasa de
        palabra al acertar la anterior.
        '''
        # Palabra por adivinar.
        self.palabra = self._asignar_palabra()

        # Listas.
        self.letras = []
        self.eventos_repetidos = []
        self.letras_utilizadas = []
        self.letras_abecedario = []
        self.pos_letras = []

        # Contador de fallos
        self.contador_fallos = 0

        self._crear_palabra()
        self._crear_abecedario()
        self.munneco = Munneco(self)  # Creación del muñeco inicial.

    def _cargar_palabras(self):
        '''
        Se cargan listas de palabras que se pueden utilizar en el juego.
        '''
        palabras_largas = open('palabras-largas.txt', 'r')
        largas = palabras_largas.read().split('\n')
        largas = largas[:-1]
        self.largas = [i.upper() for i in largas]
        palabras_largas.close()

        palabras_medianas = open('palabras-medianas.txt', 'r')
        medianas = palabras_medianas.read().split('\n')
        medianas = medianas[:-1]
        self.medianas = [i.upper() for i in medianas]
        palabras_medianas.close()

        palabras_cortas = open('palabras-cortas.txt', 'r')
        cortas = palabras_cortas.read().split('\n')
        cortas = cortas[:-1]
        self.cortas = [i.upper() for i in cortas]
        palabras_cortas.close()

        biblioteca_palabras = [self.cortas, self.medianas, self.largas]
        for nivel in biblioteca_palabras:
            for i in range(5):
                self.lista_palabras.append(random.choice(nivel))

    def _asignar_palabra(self):
        '''
        Se escoge una de las palabras de manera aleatoria.
        '''
        print(self.lista_palabras)
        palabra = self.lista_palabras[self.puntero_palabra]
        print(palabra)
        return palabra

    def _crear_palabra(self):
        '''
        Creación de la palabra por adivinar (renglones).
        '''
        numero_letras = len(self.palabra)
        for numero_letra in range(numero_letras):
            letra = Letra(self, '_ ')
            letra_ancho = letra.rect.width
            letra.x = letra_ancho + letra_ancho * numero_letra
            letra.rect.x = letra.x
            self.letras.append(letra)

    def _crear_abecedario(self):
        '''
        Se utiliza la clase Abecedario y se crean todas las letras del
        abecedario con una posición específica en la pantalla.
        '''
        # Obtención de características de las letras y el abecedario.
        A = Abecedario(self, 'A')
        letra_ancho = A.rect.width
        letra_largo = A.rect.height
        pantalla_rect = self.pantalla.get_rect()
        abecedario_completo = self.ajustes.abecedario_completo
        numero_letras = len(abecedario_completo)

        # Creación de las letras del abecedario y asignación de la posición.
        for numero_letra in range(numero_letras):
            letra = Abecedario(self, abecedario_completo[numero_letra])
            if numero_letra > 8 and numero_letra <= 17:
                x = letra_ancho + letra_ancho * (numero_letra - 9) * 4.5
                letra.rect.x = x
                y = pantalla_rect.bottom - (letra_largo * 4)
                letra.rect.y = y
            elif numero_letra > 17:
                x = letra_ancho + letra_ancho * (numero_letra - 18) * 4.5
                letra.rect.x = x
                y = pantalla_rect.bottom - (letra_largo * 2)
                letra.rect.y = y
            else:
                x = letra_ancho + letra_ancho * numero_letra * 4.5
                letra.rect.x = x
            self.letras_abecedario.append(letra)

    def run_game(self):
        '''
        Bucle principal del juego.
        '''
        while True:
            self._verificar_eventos()
            self._actualizar_pantalla()

    def _verificar_eventos(self):
        '''
        Eventos en el teclado o mouse.
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (
                event.type == pygame.MOUSEBUTTONDOWN and
                self.juego_activo is False and
                self.score is False
            ):
                mouse_pos = pygame.mouse.get_pos()
                self._revisar_boton_jugar(mouse_pos)
            elif (
                event.type == pygame.KEYDOWN and
                self.juego_activo and
                self.score is False
            ):
                self._revisar_evento_tecla(event)
            elif (
                event.type == pygame.KEYDOWN and
                self.juego_activo is False and
                self.score
            ):
                self._revisar_score(event)

    def _revisar_boton_jugar(self, mouse_pos):
        if self.boton_jugar.rect.collidepoint(mouse_pos):
            self.juego_activo = True
            self._init_juego()

    def _revisar_score(self, event):
        if event.key == pygame.K_ESCAPE:
            self.score = False
        elif event.key == pygame.K_SPACE:
            self.score = False
            self.juego_activo = True
            self._init_juego()

    def _revisar_evento_tecla(self, event):
        '''
        Responde a teclas.
        Pensar en mejor forma de aplicar la lógica.
        '''
        if event.key == pygame.K_a:
            self._evento_repetido('A')
        elif event.key == pygame.K_b:
            self._evento_repetido('B')
        elif event.key == pygame.K_c:
            self._evento_repetido('C')
        elif event.key == pygame.K_d:
            self._evento_repetido('D')
        elif event.key == pygame.K_e:
            self._evento_repetido('E')
        elif event.key == pygame.K_f:
            self._evento_repetido('F')
        elif event.key == pygame.K_g:
            self._evento_repetido('G')
        elif event.key == pygame.K_h:
            self._evento_repetido('H')
        elif event.key == pygame.K_i:
            self._evento_repetido('I')
        elif event.key == pygame.K_j:
            self._evento_repetido('J')
        elif event.key == pygame.K_k:
            self._evento_repetido('K')
        elif event.key == pygame.K_l:
            self._evento_repetido('L')
        elif event.key == pygame.K_m:
            self._evento_repetido('M')
        elif event.key == pygame.K_n:
            self._evento_repetido('N')
        elif event.key == 59:  # Probar en teclado en español.
            self._evento_repetido('Ñ')
        elif event.key == pygame.K_o:
            self._evento_repetido('O')
        elif event.key == pygame.K_p:
            self._evento_repetido('P')
        elif event.key == pygame.K_q:
            self._evento_repetido('Q')
        elif event.key == pygame.K_r:
            self._evento_repetido('R')
        elif event.key == pygame.K_s:
            self._evento_repetido('S')
        elif event.key == pygame.K_t:
            self._evento_repetido('T')
        elif event.key == pygame.K_u:
            self._evento_repetido('U')
        elif event.key == pygame.K_v:
            self._evento_repetido('V')
        elif event.key == pygame.K_w:
            self._evento_repetido('W')
        elif event.key == pygame.K_x:
            self._evento_repetido('X')
        elif event.key == pygame.K_y:
            self._evento_repetido('Y')
        elif event.key == pygame.K_z:
            self._evento_repetido('Z')

    def _evento_repetido(self, letra):
        '''
        Se verifica si la letra presionada se había presionado antes.
        Si no, se comprueba si la letra está dentro de la palabra o no.
        '''
        if letra not in self.eventos_repetidos:
            self.eventos_repetidos.append(letra)
            if letra in self.palabra:
                self._letra_acertada(letra)
            else:
                self._letra_fallida(letra)

    def _letra_acertada(self, letra):
        '''
        Si la letra presionada está dentro de la palabra, se cambia el
        renglón por la letra y modifica la letra del abecedario en verde.
        Verde == acierto.
        '''
        # Cambio de reglón por letra.
        coincidencias = re.finditer(letra, self.palabra)
        posicion = [coincidencia.start() for coincidencia in coincidencias]
        for i in posicion:
            self.letras[i].actualizar(letra)
            self.pos_letras.append(i)
        # Cambio de color a verde.
        letra_abecedario = self.ajustes.abecedario_completo.index(letra)
        self.letras_abecedario[letra_abecedario].acierto(letra)
        # Palabra acertada
        if len(self.letras) == len(self.pos_letras):
            self._palabra_acertada()

    def _letra_fallida(self, letra):
        '''
        Si la letra presionada no está dentro de la palabra, se coloca
        la letra en rojo en el abecedario.
        Rojo == fallo.
        '''
        self.contador_fallos += 1
        letra_abecedario = self.ajustes.abecedario_completo.index(letra)
        self.letras_abecedario[letra_abecedario].fallo(letra)
        self.munneco.actualizar_munneco(self.contador_fallos)
        if self.contador_fallos >= 10:
            # Por el momento se cierra el juego si se llega 10 fallos.
            # Hay que actualizarlo para que se regrese a un menu inicial
            # y muestre el scoreboard.
            self._palabra_fallida()

    def _palabra_acertada(self):
        print('Palabra acertada')
        if self.palabra in self.cortas:
            self.stats._aumentar_puntuacion('cortas')
        elif self.palabra in self.medianas:
            self.stats._aumentar_puntuacion('medianas')
        elif self.palabra in self.largas:
            self.stats._aumentar_puntuacion('largas')
        if self.puntero_palabra < 15:
            self.puntero_palabra += 1
            self._init_juego()
        else:
            print('Se acabó el juego')

    def _palabra_fallida(self):
        print('Palabra fallida')
        print('Juego terminado.')
        self.stats._puntuacion_final()
        self.juego_activo = False
        self.score = True

    def _actualizar_pantalla(self):
        '''
        Actualización de la pantalla por cada bucle.
        '''

        # Colerando el fondo.
        self.pantalla.fill(self.ajustes.bg_color)

        # Menú
        if self.juego_activo is False and self.score is False:
            self.boton_jugar._dibujar_boton()

        # Dentro del juego
        if self.juego_activo is True and self.score is False:
            # Impresión de muñeco.
            self.munneco.blitme()

            # Impresión de los puntos.
            self.stats.blit_puntos()

            # Impresión de palabra a adivinar.
            for letra in self.letras:
                letra.blitme()

            # Impresión del abecedario.
            for letra in self.letras_abecedario:
                letra.blitme()

        if self.juego_activo is False and self.score is True:
            self.stats.blitme()

        # Hace visible la última pantalla dibujada.
        pygame.display.flip()


if __name__ == '__main__':
    # Se ejecuta el juego.
    juego = Ahorcado()
    juego.run_game()
