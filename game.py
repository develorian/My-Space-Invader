import pygame
import random
import os

class Game:
    def __init__(self, font, FPS, lives, window, screen_width, screen_height, bullets=0, clock=None, bullet_img=None, spaceship_img=None):
        self.font = font
        self.HEIGHT = screen_height
        self.WIDTH = screen_width
        self.FPS = FPS
        self.lives = lives
        self.level = 1
        self.count = 0
        self.window = window
        self.clock = clock if clock else pygame.time.Clock()
        self.bullets = bullets
        self.bullet_img = bullet_img
        self.spaceship_img = spaceship_img
        
        # Inicializar listas para enemigos, balas del jugador y balas enemigas
        self.enemies = []
        self.player_bullets = []
        self.enemy_bullets = []
        
        # Posición del jugador
        self.player_x = self.WIDTH // 2
        self.player_y = self.HEIGHT - 80
        self.player_speed = 8
        self.player_width = 50
        self.player_height = 40
        
        # Configuración de enemigos
        self.enemy_rows = 5
        self.enemy_cols = 10
        self.enemy_speed = 1
        self.enemy_direction = 1
        self.enemy_width = 40
        self.enemy_height = 40
        
        # Puntuación
        self.score = 0
        self.game_over = False
        self.victory = False
        
        # Sonidos (opcional)
        self.sounds = {}
        self.load_sounds()
        
        # Inicializar enemigos
        self.create_enemies()
    
    def load_sounds(self):
        """Cargar efectos de sonido (opcional)"""
        try:
            # Puedes agregar sonidos aquí si los tienes
            # self.sounds['shoot'] = pygame.mixer.Sound('assets/shoot.wav')
            pass
        except:
            print("No se pudieron cargar los sonidos")
    
    def create_enemies(self):
        """Crear la formación de enemigos"""
        self.enemies = []
        spacing_x = 10
        spacing_y = 10
        
        for row in range(self.enemy_rows):
            for col in range(self.enemy_cols):
                x = col * (self.enemy_width + spacing_x) + 50
                y = row * (self.enemy_height + spacing_y) + 50
                enemy_rect = pygame.Rect(x, y, self.enemy_width, self.enemy_height)
                self.enemies.append({
                    'rect': enemy_rect,
                    'color': (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
                })
    
    def handle_events(self):
        """Manejar eventos del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_over and not self.victory:
                    self.shoot_bullet()
                elif event.key == pygame.K_r and (self.game_over or self.victory):
                    self.reset_game()
                elif event.key == pygame.K_ESCAPE:
                    return False
        
        return True
    
    def update(self):
        """Actualizar el estado del juego"""
        if self.game_over or self.victory:
            return
        
        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player_x > 0:
            self.player_x -= self.player_speed
        if keys[pygame.K_RIGHT] and self.player_x < self.WIDTH - self.player_width:
            self.player_x += self.player_speed
        
        # Actualizar enemigos
        self.update_enemies()
        
        # Actualizar balas del jugador
        self.update_player_bullets()
        
        # Actualizar balas enemigas
        self.update_enemy_bullets()
        
        # Disparo aleatorio de enemigos
        if random.random() < 0.005 + (self.level * 0.001):  # Aumenta probabilidad por nivel
            self.enemy_shoot()
        
        # Verificar colisiones
        self.check_collisions()
        
        # Verificar condiciones de fin de juego
        self.check_game_conditions()
    
    def update_enemies(self):
        """Actualizar posición de enemigos"""
        move_down = False
        edge_hit = False
    
        # PRIMERO: Solo verificar si hay enemigos en el borde (sin mover todavía)
        for enemy in self.enemies:
            if enemy['rect'].right >= self.WIDTH or enemy['rect'].left <= 0:
                edge_hit = True
                break
    
        # SEGUNDO: Si hay enemigo en el borde, preparar movimiento hacia abajo
        if edge_hit:
            self.enemy_direction *= -1
            move_down = True
    
        # TERCERO: Ahora mover todos los enemigos
        for enemy in self.enemies:
            # Mover horizontalmente
            enemy['rect'].x += self.enemy_speed * self.enemy_direction
        
            # Mover verticalmente SOLO si es necesario
            if move_down:
                # Ajuste más conservador para la caída
                drop_amount = max(8, 20 - (self.level * 1.3))
                enemy['rect'].y += drop_amount
    

    def update_player_bullets(self):
        """Actualizar posición de balas del jugador"""
        for bullet in self.player_bullets[:]:
            bullet.y -= 12
            if bullet.bottom < 0:
                self.player_bullets.remove(bullet)
    
    def update_enemy_bullets(self):
        """Actualizar posición de balas enemigas"""
        for bullet in self.enemy_bullets[:]:
            bullet.y += 7
            if bullet.top > self.HEIGHT:
                self.enemy_bullets.remove(bullet)
    
    def shoot_bullet(self):
        """Disparar una bala del jugador"""
        if len(self.player_bullets) < self.bullets:
            bullet_rect = self.bullet_img.get_rect()
            bullet_rect.centerx = self.player_x + self.player_width // 2
            bullet_rect.bottom = self.player_y
            self.player_bullets.append(bullet_rect)
            
            # Reproducir sonido si existe
            if 'shoot' in self.sounds:
                self.sounds['shoot'].play()
    
    def enemy_shoot(self):
        """Disparo aleatorio de enemigos"""
        if self.enemies:
            shooter = random.choice(self.enemies)
            bullet_rect = self.bullet_img.get_rect()
            bullet_rect.centerx = shooter['rect'].centerx
            bullet_rect.top = shooter['rect'].bottom
            self.enemy_bullets.append(bullet_rect)
    
    def check_collisions(self):
        """Verificar colisiones entre balas y enemigos/jugador"""
        player_rect = pygame.Rect(self.player_x, self.player_y, self.player_width, self.player_height)
    
        # Colisiones balas del jugador con enemigos
        bullets_to_remove = []
        enemies_to_remove = []
    
        for bullet in self.player_bullets:
            for enemy in self.enemies:
                if bullet.colliderect(enemy['rect']):
                    bullets_to_remove.append(bullet)
                    enemies_to_remove.append(enemy)
                    self.score += 10 + (self.level * 2)
                    break
    
        # Remover elementos después de iterar
        for bullet in bullets_to_remove:
            if bullet in self.player_bullets:
                self.player_bullets.remove(bullet)
    
        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)
    
        # Colisiones balas enemigas con jugador
        for bullet in self.enemy_bullets[:]:
            if bullet.colliderect(player_rect):
                self.enemy_bullets.remove(bullet)
                self.lives -= 1
    
    def check_game_conditions(self):
        """Verificar condiciones de victoria o derrota"""
        # Verificar si el jugador perdió
        if self.lives <= 0:
            self.game_over = True
            return
        
        # Verificar si los enemigos llegaron cerca del jugador
        player_rect = pygame.Rect(self.player_x, self.player_y, self.player_width, self.player_height)
        safety_margin = 50  # Aumentar margen de seguridad
    
        for enemy in self.enemies:
            # Verificar colisión real con el jugador, no solo posición Y
            if enemy['rect'].colliderect(player_rect) or enemy['rect'].bottom >= self.HEIGHT - 60:
                self.game_over = True
                return
    
        # Verificar si pasó de nivel
        if len(self.enemies) == 0:
            self.level_up()
    
    def level_up(self):
        """Avanzar al siguiente nivel"""
        self.level += 1
        # Limitar la velocidad máxima para que no sea imposible
        self.enemy_speed = min(2.5, 0.8 + (self.level * 0.2))  # Máximo 2.5 de velocidad
        self.enemy_direction = 1 # Reseteamos la direccion
        
        # Máximo 10 niveles // AGREGAR UN JEFE DESPUÉS DE CADA 10 NIVELES!!!
        if self.level <= 10:
            self.create_enemies()
        else:
            self.victory = True
    

    def reset_game(self):
        """Reiniciar el juego"""
        self.lives = 3
        self.level = 1
        self.score = 0
        self.game_over = False
        self.victory = False
        self.enemy_speed = 1
        self.player_bullets = []
        self.enemy_bullets = []
        self.create_enemies()
        self.player_x = self.WIDTH // 2
    
    def draw(self):
        """Dibujar todos los elementos del juego"""
        # Fondo con estrellas (efecto simple)
        self.window.fill((0, 0, 20))  # Azul oscuro
        
        # Dibujar estrellas de fondo
        for i in range(50):
            x = random.randint(0, self.WIDTH)
            y = random.randint(0, self.HEIGHT)
            pygame.draw.circle(self.window, (255, 255, 255), (x, y), 1)
        
        if not self.game_over and not self.victory:
            # Dibujar jugador (nave espacial)
            self.window.blit(self.spaceship_img, (self.player_x, self.player_y))
            
            # Dibujar enemigos
            for enemy in self.enemies:
                pygame.draw.rect(self.window, enemy['color'], enemy['rect'])
                # Ojos del enemigo (detalles)
                pygame.draw.circle(self.window, (0, 0, 0), (enemy['rect'].left + 10, enemy['rect'].top + 15), 5)
                pygame.draw.circle(self.window, (0, 0, 0), (enemy['rect'].right - 10, enemy['rect'].top + 15), 5)
            
            # Dibujar balas del jugador
            for bullet in self.player_bullets:
                self.window.blit(self.bullet_img, bullet)
            
            # Dibujar balas enemigas
            for bullet in self.enemy_bullets:
                # Rotar la bala enemiga para que apunte hacia abajo
                rotated_bullet = pygame.transform.rotate(self.bullet_img, 180)
                self.window.blit(rotated_bullet, bullet)
        
        # Dibujar HUD
        self.draw_hud()
        
        # Dibujar pantallas de fin de juego
        if self.game_over:
            self.draw_game_over()
        elif self.victory:
            self.draw_victory()
    
    def draw_hud(self):
        """Dibujar interfaz de usuario"""
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        level_text = self.font.render(f"Level: {self.level}", True, (255, 255, 255))
        bullets_text = self.font.render(f"Bullets: {self.bullets - len(self.player_bullets)}/{self.bullets}", True, (255, 255, 255))
        
        self.window.blit(score_text, (10, 10))
        self.window.blit(lives_text, (10, 40))
        self.window.blit(level_text, (10, 70))
        self.window.blit(bullets_text, (10, 100))
    
    def draw_game_over(self):
        """Dibujar pantalla de Game Over"""
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.window.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_text = self.font.render("Press R to restart or ESC to quit", True, (255, 255, 255))
        
        self.window.blit(game_over_text, 
                        (self.WIDTH//2 - game_over_text.get_width()//2, self.HEIGHT//2 - 60))
        self.window.blit(score_text, 
                        (self.WIDTH//2 - score_text.get_width()//2, self.HEIGHT//2 - 20))
        self.window.blit(restart_text, 
                        (self.WIDTH//2 - restart_text.get_width()//2, self.HEIGHT//2 + 20))
    
    def draw_victory(self):
        """Dibujar pantalla de Victoria"""
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 50, 0, 200))
        self.window.blit(overlay, (0, 0))
        
        victory_text = self.font.render("VICTORY!", True, (0, 255, 0))
        score_text = self.font.render(f"Final Score: {self.score}", True, (255, 255, 255))
        restart_text = self.font.render("Press R to restart or ESC to quit", True, (255, 255, 255))
        
        self.window.blit(victory_text, 
                        (self.WIDTH//2 - victory_text.get_width()//2, self.HEIGHT//2 - 60))
        self.window.blit(score_text, 
                        (self.WIDTH//2 - score_text.get_width()//2, self.HEIGHT//2 - 20))
        self.window.blit(restart_text, 
                        (self.WIDTH//2 - restart_text.get_width()//2, self.HEIGHT//2 + 20))
    
    def run(self):
        """Bucle principal del juego"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            
            pygame.display.flip()
            self.clock.tick(self.FPS)