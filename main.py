import pygame
import sys
from game import Game

def main():
    # Inicializar Pygame
    pygame.init()
    
    # Configuración de la pantalla
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    FPS = 60
    
    # Crear ventana
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("My Space Invaders 🚀")
    
    # Cargar fuentes
    font = pygame.font.Font(None, 36)
    
    # Cargar imágenes
    try:
        bullet_img = pygame.image.load("assets/bullet.png").convert_alpha()
        spaceship_img = pygame.image.load("assets/spaceship.png").convert_alpha()
    except pygame.error as e:
        print(f"No se pudieron cargar las imágenes: {e}")
        print("Asegúrate de que existen los archivos:")
        print("- assets/bullet.png")
        print("- assets/spaceship.png")
        sys.exit()
    
    # Redimensionar imágenes si es necesario
    spaceship_img = pygame.transform.scale(spaceship_img, (50, 40))
    bullet_img = pygame.transform.scale(bullet_img, (5, 15))
    
    # Crear instancia del juego
    game = Game(
        font=font,
        FPS=FPS,
        lives=3,
        window=screen,
        screen_width=SCREEN_WIDTH,
        screen_height=SCREEN_HEIGHT,
        bullets=5,  # Máximo de balas en pantalla
        bullet_img=bullet_img,
        spaceship_img=spaceship_img
    )
    
    # Ejecutar el juego
    game.run()

if __name__ == "__main__":
    main()