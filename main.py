import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen settings
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 20

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock to control FPS
clock = pygame.time.Clock()

# Font for score
font = pygame.font.SysFont('arial', 25)

def show_score(score):
    """Display score on screen"""
    text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(text, (10, 10))

def draw_snake(block_size, snake_list):
    """Draw the snake on screen"""
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], block_size, block_size])

def game():
    """Main game function"""
    game_over = False
    
    # Initial snake position
    x = WIDTH // 2
    y = HEIGHT // 2
    
    # Initial movement
    dx = 0
    dy = 0
    
    # List that stores snake segments
    snake_list = []
    snake_length = 1
    
    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            # Keyboard controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = BLOCK_SIZE
                    dx = 0
        
        # Update position
        x += dx
        y += dy
        
        # Check collision with borders
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw food
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        # Add new head position
        snake_head = [x, y]
        snake_list.append(snake_head)
        
        # Remove old segments
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        # Check collision with own body
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True
        
        # Draw snake
        draw_snake(BLOCK_SIZE, snake_list)
        
        # Show score
        show_score(snake_length - 1)
        
        # Update screen
        pygame.display.update()
        
        # Check if ate food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            snake_length += 1
        
        # Control game speed
        clock.tick(10)
    
    # Game over message
    screen.fill(BLACK)
    message = font.render(f'Game Over! Score: {snake_length - 1}', True, RED)
    screen.blit(message, (WIDTH // 2 - 150, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)
    
    pygame.quit()
    sys.exit()

# Start game
if __name__ == '__main__':
    game()