import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 40
PLAYER_RADIUS = 15
PLAYER_COLOR = "red"
BACKGROUND_COLOR = "white"
MAZE_COLOR = "black"
FPS = 10

# Load sound
sound = pygame.mixer.Sound("sound_keyboard.wav")
congratulations_sound = pygame.mixer.Sound("sound_congratulations.wav")

# Maze layout (1 represents wall, 0 represents path)
MAZE = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

# Player starting position
player_pos = [3 * TILE_SIZE + TILE_SIZE // 2, 0 * TILE_SIZE + TILE_SIZE // 2]

# Exit position
exit_pos = (14, 10)  # Grid position of the exit

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

def draw_maze():
    for y, row in enumerate(MAZE):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, MAZE_COLOR, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def move_player(dx, dy):
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    grid_x = new_x // TILE_SIZE
    grid_y = new_y // TILE_SIZE

    if MAZE[grid_y][grid_x] == 0:
        player_pos[0] = new_x
        player_pos[1] = new_y
        # Play sound
        sound.play()

pygame.key.stop_text_input()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_player(0, -TILE_SIZE)
    if keys[pygame.K_s]:
        move_player(0, TILE_SIZE)
    if keys[pygame.K_a]:
        move_player(-TILE_SIZE, 0)
    if keys[pygame.K_d]:
        move_player(TILE_SIZE, 0)

    # Check if player reached the exit
    if (player_pos[0] // TILE_SIZE, player_pos[1] // TILE_SIZE) == exit_pos:
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont(None, 55)
        text = font.render('Congratulations!', True, (0, 128, 0))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        congratulations_sound.play()
        pygame.display.flip()
        time.sleep(3)
        running = False

    screen.fill(BACKGROUND_COLOR)
    draw_maze()
    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, PLAYER_RADIUS)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()