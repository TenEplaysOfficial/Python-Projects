import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Box")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_SPEED = 5
PIPE_GAP = 150

# Fonts
FONT = pygame.font.Font(None, 36)

# Game states
MAIN_MENU = 0
PLAY_STATE = 1
PAUSE_MENU = 2
GAME_OVER = 3

# Load high score
if os.path.exists("high_score.txt"):
    with open("high_score.txt", "r") as f:
        high_score = int(f.read())
else:
    high_score = 0

class Bird:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2, self.width, self.height)
        self.velocity = 0
        self.alive = True

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        # Check if the bird is out of the screen
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.alive = False

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)

class Pipe:
    def __init__(self):
        self.width = 70
        self.height = random.randint(100, SCREEN_HEIGHT - 200)
        self.pipe_top = pygame.Rect(SCREEN_WIDTH, 0, self.width, self.height)
        self.pipe_bottom = pygame.Rect(SCREEN_WIDTH, self.height + PIPE_GAP, self.width, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.pipe_top.x -= PIPE_SPEED
        self.pipe_bottom.x -= PIPE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.pipe_top)
        pygame.draw.rect(screen, GREEN, self.pipe_bottom)

    def off_screen(self):
        return self.pipe_top.right < 0

    def collides_with(self, bird):
        return bird.rect.colliderect(self.pipe_top) or bird.rect.colliderect(self.pipe_bottom)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main():
    global high_score
    clock = pygame.time.Clock()

    # Game state
    game_state = MAIN_MENU

    # Bird instance
    bird = Bird()

    # Pipe list
    pipes = []

    # Score variables
    score = 0
    pipe_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(pipe_timer, 1200)

    while True:
        SCREEN.fill(WHITE)

        if game_state == MAIN_MENU:
            draw_text("Flappy Bird", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text("Press SPACE to Play", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_state = PLAY_STATE
                        bird = Bird()
                        pipes = []
                        score = 0
                        pygame.time.set_timer(pipe_timer, 1200)

        elif game_state == PLAY_STATE:
            bird.update()
            bird.draw(SCREEN)

            if bird.alive:
                for pipe in pipes:
                    pipe.update()
                    pipe.draw(SCREEN)
                    if pipe.collides_with(bird):
                        bird.alive = False  # End the game if bird collides with a pipe

                pipes = [pipe for pipe in pipes if not pipe.off_screen()]

                # Scoring
                for pipe in pipes:
                    if pipe.pipe_top.right < bird.rect.left and not pipe.collides_with(bird):
                        score += 1
                        pipes.remove(pipe)

                draw_text(f"Score: {score}", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, 50)
                draw_text(f"High Score: {high_score}", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()
                    if event.key == pygame.K_p:
                        game_state = PAUSE_MENU
                if event.type == pipe_timer:
                    pipes.append(Pipe())

            # Check if the bird is dead
            if not bird.alive:
                game_state = GAME_OVER

        elif game_state == PAUSE_MENU:
            draw_text("Game Paused", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text("Press P to Resume", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text("Press Q to Quit", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        game_state = PLAY_STATE

        elif game_state == GAME_OVER:
            draw_text("Game Over", FONT, RED, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            draw_text(f"Score: {score}", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            draw_text(f"High Score: {high_score}", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5)
            draw_text("Press SPACE to Restart", FONT, BLACK, SCREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.25)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if score > high_score:
                            high_score = score
                            with open("high_score.txt", "w") as f:
                                f.write(str(high_score))
                        game_state = MAIN_MENU

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
