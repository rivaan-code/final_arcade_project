import pygame


pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("welcome to the arcade")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)  # None = default font, 36 = size
text = font.render("Welcome to my arcade\n1 for menu sandwich game\n2 for turtle race\n3 for click me", True, BLACK)
# for event in pygame.event.get():
#     if event.type == 1:
#         burger.main_loop()
            
#     elif event.type ==2: pass
#     elif event.type == 3: pass
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    # Draw text
    screen.blit(text, (100, 50))
    pygame.display.flip()
    pygame.display.update
pygame.quit()

