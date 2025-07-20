import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Click Me Game!")

font=pygame.font.SysFont(None, 40)

card_list =["image1.jpg", "image2.jpg","image3.jpg","image4.png", 'image5.png']
card_images = []
for filename in card_list:
    img = pygame.image.load(filename)
    card_images.append(pygame.transform.scale(img,(150,150)))

card_img = random.choice(card_images)
lst = []

player_x = random.randint(0, SCREEN_WIDTH - 100)
player_y = random.randint(0, SCREEN_HEIGHT - 100)

player_score = 0
miss_score = 0
BLACK = (0,0,0)

#function to display text message to user
def draw_text(text, font, color, x,y):
    img = font.render(text,True, color )
    text_rect = img.get_rect(center=(x,y))
    screen.blit(img,text_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if any(rect.collidepoint(x,y) for rect in lst):
                # print('clicked on image')
                card_img = random.choice(card_images)
                player_x = random.randint(0, SCREEN_WIDTH - 100)
                player_y = random.randint(0, SCREEN_HEIGHT - 100)
                # print(player_x, player_y)
                player_score += 1
            else:
                miss_score += 1

    screen.fill((255,255,255))

    lst = []
    if card_img !=None:   
        lst.extend([
        screen.blit(card_img,[player_x,player_y]) 
        ])

    draw_text(f'Hits:{player_score}', font, BLACK, 100,50)
    draw_text(f'Missed:{miss_score}', font, BLACK, SCREEN_WIDTH-120,50)

    pygame.display.flip()
pygame.quit()
