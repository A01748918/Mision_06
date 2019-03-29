#Autor: César Guzmán Guadarrama
#Mision 06 dibujando con ecuasiones

import random
import math
import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

def generarColorAzar():
    rojo = random.randint(0, 255)
    azul =random.randint(0, 255)
    verde= random.randint(0,255)
    colorX = (rojo,azul,verde)
    return colorX


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r, R, l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        k = r / R
        colorAzar = generarColorAzar()

        periodo = r // math.gcd(r, R)
        for angulo in range(0, (360+1)*periodo*2, 1):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(R * (((1 - k) * math.cos(a)) + ((l * k) * math.cos(((l - k) / k) * a))))
            y = int(R * (((1 - k) * math.sin(a)) - ((l * k) * math.sin(((l - k) / k) * a))))
            pygame.draw.circle(ventana, colorAzar, (x + ANCHO // 2, ALTO // 2 - y), 1)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = int(input("Teclea un valor para r: "))
    R = int(input("Teclea un valor para R: "))
    l = float(input("Teclea un valor para l: "))
    dibujar(r, R, l)

# Llamas a la función principal
main()