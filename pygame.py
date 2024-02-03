import pygame
import sys


pygame.init()


width, height = 400, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Shapes")


blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)


polygon_vertices = [(146, 0), (291, 106), (236, 277), (56, 277), (0, 106)]


line_start = (60, 300)
line_end = (120, 300)
line_thickness = 4


circle_center = (300, 50)
circle_radius = 20


ellipse_rect = pygame.Rect(300, 250, 40, 80)
ellipse_thickness = 1


rectangle_rect = pygame.Rect(150, 300, 100, 50)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    window.fill((255, 255, 255))

    
    pygame.draw.polygon(window, blue, polygon_vertices)
    pygame.draw.line(window, green, line_start, line_end, line_thickness)
    pygame.draw.circle(window, green, circle_center, circle_radius)
    pygame.draw.ellipse(window, black, ellipse_rect, ellipse_thickness)
    pygame.draw.rect(window, black, rectangle_rect)

    
    pygame.display.flip()


pygame.quit()
sys.exit()
