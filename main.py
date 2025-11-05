<<<<<<< HEAD
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
=======
import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        
        # Game settings
        self.width = 600
        self.height = 400
        self.block_size = 20
        self.speed = 150  
        
        # Colors
        self.bg_color = "#000000"
        self.snake_color = "#00FF00"
        self.food_color = "#FF0000"
        self.text_color = "#FFFFFF"
        
        # Create canvas
        self.canvas = tk.Canvas(
            root, 
            width=self.width, 
            height=self.height, 
            bg=self.bg_color,
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Score label
        self.score_label = tk.Label(
            root, 
            text="Score: 0", 
            font=("Arial", 14),
            bg="#000000",
            fg="#FFFFFF"
        )
        self.score_label.pack()
        
        # Game state
        self.snake = []
        self.direction = None
        self.next_direction = None
        self.food = None
        self.score = 0
        self.game_running = False
        
        # Bind keys
        self.root.bind("<Left>", lambda e: self.change_direction("Left"))
        self.root.bind("<Right>", lambda e: self.change_direction("Right"))
        self.root.bind("<Up>", lambda e: self.change_direction("Up"))
        self.root.bind("<Down>", lambda e: self.change_direction("Down"))
        self.root.bind("<space>", lambda e: self.restart_game())
        
        # Start game
        self.show_start_screen()
    
    def show_start_screen(self):
        """Display start screen"""
        self.canvas.delete("all")
        self.canvas.create_text(
            self.width // 2,
            self.height // 2 - 30,
            text="SNAKE GAME",
            font=("Arial", 30, "bold"),
            fill=self.text_color
        )
        self.canvas.create_text(
            self.width // 2,
            self.height // 2 + 20,
            text="Press SPACE to start",
            font=("Arial", 16),
            fill=self.text_color
        )
        self.canvas.create_text(
            self.width // 2,
            self.height // 2 + 50,
            text="Use Arrow Keys to move",
            font=("Arial", 12),
            fill=self.text_color
        )
    
    def restart_game(self):
        """Start or restart the game"""
        # Reset game state
        self.snake = [[self.width // 2, self.height // 2]]
        self.direction = None
        self.next_direction = None
        self.score = 0
        self.game_running = True
        
        # Update score
        self.score_label.config(text=f"Score: {self.score}")
        
        # Create first food
        self.create_food()
        
        # Clear canvas and start game loop
        self.canvas.delete("all")
        self.game_loop()
    
    def change_direction(self, new_direction):
        """Change snake direction (prevent 180-degree turns)"""
        if not self.game_running:
            return
        
        opposite_directions = {
            "Left": "Right",
            "Right": "Left",
            "Up": "Down",
            "Down": "Up"
        }
        
        if self.direction is None or new_direction != opposite_directions.get(self.direction):
            self.next_direction = new_direction
    
    def create_food(self):
        """Create food at random position"""
        while True:
            x = random.randint(0, (self.width // self.block_size) - 1) * self.block_size
            y = random.randint(0, (self.height // self.block_size) - 1) * self.block_size
            
            # Make sure food doesn't appear on snake
            if [x, y] not in self.snake:
                self.food = [x, y]
                break
    
    def game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return
        
        # Update direction
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None
        
        # Move snake
        if self.direction:
            head = self.snake[0].copy()
            
            if self.direction == "Left":
                head[0] -= self.block_size
            elif self.direction == "Right":
                head[0] += self.block_size
            elif self.direction == "Up":
                head[1] -= self.block_size
            elif self.direction == "Down":
                head[1] += self.block_size
            
            # Check collision with walls
            if (head[0] < 0 or head[0] >= self.width or 
                head[1] < 0 or head[1] >= self.height):
                self.game_over()
                return
            
            # Check collision with self
            if head in self.snake:
                self.game_over()
                return
            
            # Add new head
            self.snake.insert(0, head)
            
            # Check if ate food
            if head == self.food:
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                self.create_food()
            else:
                # Remove tail if didn't eat food
                self.snake.pop()
        
        # Draw everything
        self.draw()
        
        # Schedule next update
        self.root.after(self.speed, self.game_loop)
    
    def draw(self):
        """Draw snake and food"""
        self.canvas.delete("all")
        
        # Draw snake
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1],
                segment[0] + self.block_size, segment[1] + self.block_size,
                fill=self.snake_color,
                outline=self.snake_color
            )
        
        # Draw food
        if self.food:
            self.canvas.create_rectangle(
                self.food[0], self.food[1],
                self.food[0] + self.block_size, self.food[1] + self.block_size,
                fill=self.food_color,
                outline=self.food_color
            )
    
    def game_over(self):
        """Display game over screen"""
        self.game_running = False
        self.canvas.delete("all")
        
        self.canvas.create_text(
            self.width // 2,
            self.height // 2 - 40,
            text="GAME OVER!",
            font=("Arial", 30, "bold"),
            fill=self.food_color
        )
        self.canvas.create_text(
            self.width // 2,
            self.height // 2 + 10,
            text=f"Final Score: {self.score}",
            font=("Arial", 20),
            fill=self.text_color
        )
        self.canvas.create_text(
            self.width // 2,
            self.height // 2 + 50,
            text="Press SPACE to play again",
            font=("Arial", 14),
            fill=self.text_color
        )

# Create and run game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
>>>>>>> 368fb2b4fd234514757fd4df94de48b2b64927c5
