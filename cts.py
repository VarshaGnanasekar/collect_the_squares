import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Collect the Items Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)

# Player properties
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Items
item_size = 30
num_items = 5
items = [[random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)] for _ in range(num_items)]

# Font and score
font = pygame.font.SysFont("comicsansms", 28)
big_font = pygame.font.SysFont("comicsansms", 48)
score = 0
start_ticks = pygame.time.get_ticks()
game_duration = 60  # seconds

# Sounds (optional)
try:
    collect_sound = pygame.mixer.Sound(pygame.mixer.Sound(pygame.mixer.Sound("collect.wav")))
except:
    collect_sound = None

# Clock
clock = pygame.time.Clock()

# Collision check
def check_collision(p_pos, i_pos):
    px, py = p_pos
    ix, iy = i_pos
    return (
        px < ix + item_size and
        px + player_size > ix and
        py < iy + item_size and
        py + player_size > iy
    )

# Game loop
running = True
game_over = False

while running:
    screen.fill(WHITE)

    # Time calculation
    seconds = game_duration - (pygame.time.get_ticks() - start_ticks) // 1000
    if seconds <= 0:
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
            player_pos[1] += player_speed

        # Collision and respawn
        for i in range(len(items)):
            if check_collision(player_pos, items[i]):
                score += 1
                items[i] = [random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)]
                if collect_sound:
                    collect_sound.play()
                if score % 5 == 0:
                    player_speed += 1  # Increase difficulty

        # Draw player
        pygame.draw.rect(screen, BLUE, (*player_pos, player_size, player_size))

        # Draw items
        for item in items:
            pygame.draw.rect(screen, RED, (*item, item_size, item_size))

        # Draw score and timer
        score_text = font.render(f"Score: {score}", True, BLACK)
        timer_text = font.render(f"Time Left: {seconds}s", True, BLACK)
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (10, 50))
    else:
        # Game Over Screen
        over_text = big_font.render("Game Over!", True, RED)
        final_score = font.render(f"Final Score: {score}", True, BLACK)
        restart_text = font.render("Press R to Restart or Q to Quit", True, BLACK)
        screen.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 100))
        screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 60))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Restart the game
            player_pos = [WIDTH // 2, HEIGHT // 2]
            score = 0
            player_speed = 5
            items = [[random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)] for _ in range(num_items)]
            start_ticks = pygame.time.get_ticks()
            game_over = False
        if keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(30)
