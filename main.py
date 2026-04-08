import pygame
import sys 
from tankplayer import TankPlayer
from tankbot import TankBot
from bullet import Bullet

pygame.init()

# mengambil gambar tank player dan tank bot dari folder 
player_img = pygame.image.load("C:/Project/PBO/Project Tank/tank_player.png")
enemy_img = pygame.image.load("C:/Project/PBO/Project Tank/tank_enemy.png")

# menyeting ukuran gambar tank yang sesuai
player_img = pygame.transform.scale(player_img, (40, 40))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))

# mengambil backsound dari folder dan menyeting volume serta memainkannya secara loop
pygame.mixer.init()
pygame.mixer.music.load("C:/Project/PBO/Project Tank/backsound.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

# mengambil background dari folder 
background_img = pygame.image.load("C:/Project/PBO/Project Tank/background.png")
background_img = pygame.transform.scale(background_img, (600, 600))

# menyeting ukuran layar, judul, warna, font, dan clock untuk mengatur frame rate
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Tank Sederhana")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# membuat objek player dan enemy, serta variabel untuk mengatur peluru, game over, dan hasil permainan
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# fungsi untuk menentukan posisi awal peluru berdasarkan posisi dan arah tank
def get_bullet_start(x, y, width, height, direction):
    if direction == "UP":
        return x + width // 2, y
    elif direction == "DOWN":
        return x + width // 2, y + height
    elif direction == "LEFT":
        return x, y + height // 2
    elif direction == "RIGHT":
        return x + width, y + height // 2

# membuat objek player dan enemy, serta variabel untuk mengatur peluru, game over, dan hasil permainan
player = TankPlayer(100, 200, player_img)
enemy = TankBot(400, 200, enemy_img)

# mengatur delay tembakan musuh agar tidak terlalu cepat
enemy_last_shot = 0
enemy_shoot_delay = 800

# daftar untuk menyimpan peluru yang ditembakkan oleh player dan enemy
bullets = []
enemy_bullets = []

# variabel untuk mengatur status game over dan hasil permainan
game_over = False
game_result = ""

# mengatur delay tembakan player agar tidak terlalu cepat
last_shot_time = 0
shoot_delay = 700

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # jika permainan sudah selesai maka bisa mengulang dengan menekan tombol space 
    if game_over and keys[pygame.K_SPACE]:
        # dan mereset posisi player dan enemy
        player = TankPlayer(100, 200, player_img)
        enemy = TankBot(400, 200, enemy_img)
        bullets.clear()
        enemy_bullets.clear()
        game_over = False
        game_result = ""

    # jika permainan belum selesai maka player dan enemy bisa bergerak
    if not game_over:
        player.move(keys, enemy, WIDTH, HEIGHT)
        enemy.move(player, WIDTH, HEIGHT)

    current_time = pygame.time.get_ticks()

    # jika tombol enter ditekan dan sudah melewati delay tembakan
    if keys[pygame.K_RETURN] and current_time - last_shot_time > shoot_delay:
        bx, by = get_bullet_start(
            player.x, player.y, player.width, player.height, player.direction
        )
        bullets.append(Bullet(bx, by, player.direction))
        last_shot_time = current_time

    # musuh akan menembak secara otomatis berdasarkan timer dan delay tembakan
    if current_time - enemy_last_shot > enemy_shoot_delay:
        bx, by = get_bullet_start(
            enemy.x, enemy.y, enemy.width, enemy.height, enemy.direction
        )
        enemy_bullets.append(Bullet(bx, by, enemy.direction))
        enemy_last_shot = current_time

    # menggerakkan semua peluru yang ada di layar
    for bullet in bullets:
        bullet.move()

    # menggerakkan semua peluru musuh yang ada di layar
    for bullet in enemy_bullets:
        bullet.move()
        
    # menghapus peluru yang sudah keluar dari layar
    for bullet in bullets:
        if bullet.get_rect().colliderect(enemy.get_rect()):
            game_over = True
            game_result = "MENANG"

    for bullet in enemy_bullets:
        if bullet.get_rect().colliderect(player.get_rect()):
            game_over = True
            game_result = "KALAH"

    screen.blit(background_img, (0, 0))

    player.draw(screen)
    enemy.draw(screen)

    # jika game over maka tampilkan pesan hasil permainan dan instruksi untuk mengulang
    if game_over:
        if game_result == "MENANG":
            text = font.render("KAMU MENANG", True, (0, 0, 200))
        else:
            text = font.render("KAMU KALAH", True, (200, 0, 0))

        screen.blit(text, (WIDTH//2 - 120, HEIGHT//2 - 20))

        info = font.render("Tekan SPACE untuk ulang", True, BLACK)
        screen.blit(info, (WIDTH//2 - 180, HEIGHT//2 + 30))

    for bullet in bullets:
        bullet.draw(screen)

    for bullet in enemy_bullets:
        bullet.draw(screen)

    pygame.display.update()

pygame.quit()
sys.exit()