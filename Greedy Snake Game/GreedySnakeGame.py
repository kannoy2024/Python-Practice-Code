import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# 游戏窗口尺寸
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# 蛇和食物尺寸
CELL_SIZE = 20

# 初始化窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("黄祖振的贪吃蛇小游戏：52202042015")

clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.body = [[WINDOW_WIDTH//2, WINDOW_HEIGHT//2]]
        self.direction = "RIGHT"
        self.speed = 6

    def move(self):
        head = self.body[0].copy()
        
        if self.direction == "RIGHT":
            head[0] += CELL_SIZE
        elif self.direction == "LEFT":
            head[0] -= CELL_SIZE
        elif self.direction == "UP":
            head[1] -= CELL_SIZE
        elif self.direction == "DOWN":
            head[1] += CELL_SIZE
            
        self.body.insert(0, head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1].copy()
        self.body.append(tail)

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        return [x, y]

def draw_button(surface, color, x, y, width, height, text, text_color):
    pygame.draw.rect(surface, color, (x, y, width, height))
    pygame.draw.rect(surface, BLACK, (x, y, width, height), 2)
    
    try:
        font = pygame.font.Font("simhei.ttf", 35)
    except:
        font = pygame.font.SysFont("simhei", 35)
    
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width/2, y + height/2))
    surface.blit(text_surface, text_rect)
    
    return pygame.Rect(x, y, width, height)


def show_game_over_screen(score):
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    # 使用支持中文的字体
    try:
        font_large = pygame.font.Font("simhei.ttf", 72)
        font_medium = pygame.font.Font("simhei.ttf", 48)
    except:
        font_large = pygame.font.SysFont("simhei", 72)
        font_medium = pygame.font.SysFont("simhei", 48)
    
    game_over_text = font_large.render("游戏结束!", True, WHITE)
    score_text = font_medium.render(f"最终得分: {score}", True, WHITE)
    
    screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2 - 100))
    screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, WINDOW_HEIGHT//2 - 20))
    
    restart_button = draw_button(screen, GREEN, WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 50, 200, 50, "再来一局", WHITE)
    quit_button = draw_button(screen, RED, WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 120, 200, 50, "退出游戏", WHITE)
    
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    return True
                elif quit_button.collidepoint(mouse_pos):
                    return False
        clock.tick(30)

def game_loop():
    while True:
        snake = Snake()
        food = Food()
        score = 0
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                    elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                        snake.direction = "RIGHT"
                    elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                        snake.direction = "LEFT"
                    elif event.key == pygame.K_UP and snake.direction != "DOWN":
                        snake.direction = "UP"
                    elif event.key == pygame.K_DOWN and snake.direction != "UP":
                        snake.direction = "DOWN"

            snake.move()

            # 碰撞检测
            if snake.body[0][0] < 0 or snake.body[0][0] >= WINDOW_WIDTH \
                or snake.body[0][1] < 0 or snake.body[0][1] >= WINDOW_HEIGHT:
                game_over = True

            for segment in snake.body[1:]:
                if snake.body[0] == segment:
                    game_over = True

            # 吃食物检测
            if snake.body[0] == food.position:
                snake.grow()
                food.position = food.random_position()
                score += 100
                snake.speed += 0.5

            # 绘制界面
            screen.fill(BLACK)
            
            # 绘制蛇
            for segment in snake.body:
                pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            
            # 绘制食物
            pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))
            
            # 显示分数
            font = pygame.font.SysFont(None, 35)
            text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(text, (10, 10))

            pygame.display.update()
            clock.tick(snake.speed)

        # 游戏结束，显示结束界面
        if not show_game_over_screen(score):
            pygame.quit()
            return

if __name__ == "__main__":
    game_loop()