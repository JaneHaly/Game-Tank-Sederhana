import random # untuk memilih arah gerakan secara acak
from character import Character # disini tidak membutuhkan import pygame karena sudah diimport di character.py

# kelas untuk musuh yang bergerak otomatis
class TankBot(Character): 
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.move_timer = 0


    def move(self, player,WIDTH, HEIGHT): # pergerakan = otomatis dengan timer, dengan deteksi tabrakan dengan pemain, map  
        old_x = self.x
        old_y = self.y

        self.move_timer += 1

        if self.move_timer > 60:
            self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
            self.move_timer = 0

        # gerakan berdasarkan arah yang dipilih
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed

        # batasan agar tidak keluar map
        if self.x < 0:
            self.x = 0
        if self.x + self.width > WIDTH:
            self.x = WIDTH - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

        # deteksi tabrakan dengan pemain
        if self.get_rect().colliderect(player.get_rect()):
            self.x = old_x
            self.y = old_y