import pygame
from character import Character

# kelas untuk pemain yang bisa dikendalikan dengan keyboard
class TankPlayer(Character):
    def move(self, keys, enemy, WIDTH, HEIGHT): # pergerakan = berdasarkan input keyboard, dengan deteksi tabrakan dengan musuh, map
        old_x = self.x
        old_y = self.y

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.direction = "LEFT"
        if keys[pygame.K_d]:
            self.x += self.speed
            self.direction = "RIGHT"
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.direction = "UP"
        if keys[pygame.K_s]:
            self.y += self.speed
            self.direction = "DOWN"

        # batasan agar tidak keluar map
        if self.x < 0:
            self.x = 0
        if self.x + self.width > WIDTH:
            self.x = WIDTH - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

        # deteksi tabrakan dengan musuh
        if self.get_rect().colliderect(enemy.get_rect()):
            self.x = old_x
            self.y = old_y