import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Items Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player properties
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 5

# Item properties
item_size = 30
item_pos = [random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)]

# Score
score = 0

# Font for displaying the score
font = pygame.font.SysFont("comicsansms", 30)

# Game clock
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    # Check for collision with the item
    if (player_pos[0] < item_pos[0] < player_pos[0] + player_size or item_pos[0] < player_pos[0] < item_pos[0] + item_size) and \
       (player_pos[1] < item_pos[1] < player_pos[1] + player_size or item_pos[1] < player_pos[1] < item_pos[1] + item_size):
        score += 1
        item_pos = [random.randint(0, WIDTH - item_size), random.randint(0, HEIGHT - item_size)]

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (item_pos[0], item_pos[1], item_size, item_size))

    # Display the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the game speed
    clock.tick(30)

# Quit Pygame
pygame.quit()
