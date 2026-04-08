import pygame

# membuat kelas karakter sebagai dasar untuk TankPlayer dan TankBot
class Character:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 2
        self.direction = "UP"
        self.image = image

    # metode untuk menggambar karakter dengan rotasi sesuai arahnya
    def draw(self, surface):
        rotated = self.image

        if self.direction == "UP":
            rotated = pygame.transform.rotate(self.image, 0) # atas

        elif self.direction == "DOWN":
            rotated = pygame.transform.rotate(self.image, 180) # bawah

        elif self.direction == "LEFT":
            rotated = pygame.transform.rotate(self.image, 90) # kiri

        elif self.direction == "RIGHT":
            rotated = pygame.transform.rotate(self.image, -90) # kanan

        surface.blit(rotated, (self.x, self.y)) # menggambar karakter pada posisi (x, y) dengan gambar yang sudah diputar sesuai arah

    # metode untuk mendapatkan persegi panjang karakter untuk deteksi tabrakan
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)