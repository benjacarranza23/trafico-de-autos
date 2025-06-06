import pygame
import random
import sys

ancho = 800
alto = 600
BLUE = (0, 100, 255)

#para buscar la imagen del auto buscamos de esta forma:
#créame una imagen de un auto de carrera pixeleado que este mirando recto en forma vertical
#iniciamos
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("trafico de autos")
clock = pygame.time.Clock()

SHIP_SIZE = (50, 50)
AUTOJ_SIZE = (40, 40)
BULLET_SIZE = (5, 10)
AUTOJ_START_Y = -40
BULLET_SPEED = -7
SHIP_SPEED = 5
AUTOS_CARRETERA_MIN_SPEED = 2
AUTOS_CARRETERA_MAX_SPEED = 5
AUTOS_CARRETERA_SPAWN_RATE = 30

imagen_de_AutoJ = pygame.image.load("/home/quintob/Descargas/visual studio.py/imagenruta.webp")

class AutoJ:
    """representa al auto que debe usar o mover el jugador"""
    def __init__(self):
        """inicializacion del auto"""
        imagen_de_autoJ = pygame.image.load("/home/quintob/Descargas/visual studio.py/imagenruta.webp")
        self.image = pygame.Surface(SHIP_SIZE)
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))
        self.velocidad = SHIP_SPEED

def mover_autoJ(self, teclas):
        """Mueve el autoJ según las teclas presionadas."""
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.velocidad

def dibujar(self, superficie):
        """Dibuja la nave en la superficie dada."""
        superficie.blit(self.image, self.rect)

class AUTOS_CARRETERA:
    """Clase que representa los asteroides."""
    def __init__(self):
        """Inicializa un asteroide en una posición aleatoria en la parte superior."""
        x = random.randint(0, WIDTH - CARRET_SIZE[0])
        self.rect = pygame.Rect(x, AUTO_CARRETERA_START_Y, *AUTO_CARRETERA_SIZE)
        self.velocidad = random.randint(AUCARRET_MIN_SPEED, AUCARRET_MAX_SPEED)
        
    def mover(self):
        """Mueve el asteroide hacia abajo."""
        self.rect.y += self.velocidad 
        
class Juego:
    """Clase principal que controla la lógica del juego."""
    def __init__(self):
        """Inicializa los elementos del juego."""
        self.auto = Nave()
        self.autos_catterera = []
        self.puntaje = 0
        self.spawn_timer = 0
        self.running = True
        self.fuente = pygame.font.SysFont(None, 30)