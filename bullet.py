import pygame

BLACK = (0, 0, 0)

# kelas untuk peluru yang ditembakkan oleh pemain dan musuh
class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.size = 6
        self.speed = 6
        self.direction = direction

    # mengeluarkan peluru berdasarkan arah tank
    def move(self):
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed

    # menggambar peluru sebagai kotak kecil
    def draw(self, surface):
        pygame.draw.rect(surface, BLACK,
                         (self.x, self.y, self.size, self.size))

    # metode untuk mendapatkan persegi panjang peluru untuk deteksi tabrakan dengan tank lain
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)