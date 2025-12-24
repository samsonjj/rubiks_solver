import pygame
from typing import List

class SquareColor:
    WHI = 1
    RED = 2
    BLU = 3
    YEL = 4
    ORA = 5
    GRE = 6

    @staticmethod
    def get_color(c) -> pygame.Color:
        match c:
            case SquareColor.WHI:
                return (255, 255, 255)
            case SquareColor.RED:
                return (255, 0, 0)
            case SquareColor.BLU:
                return (0, 0, 255)
            case SquareColor.YEL:
                return (255, 255, 0)
            case SquareColor.GRE:
                return (0, 255, 0)
            case SquareColor.ORA:
                return (255, 128, 20)

WHI = SquareColor.WHI
RED = SquareColor.RED
BLU = SquareColor.BLU
YEL = SquareColor.YEL
ORA = SquareColor.ORA
GRE = SquareColor.GRE

W = 15
F = 45

def render(screen):
    cube = [
        1, 1, 1, 1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3, 3, 3,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 
        5, 5, 5, 5, 5, 5, 5, 5, 5,
        6, 6, 6, 6, 6, 6, 6, 6, 6, 
    ]

    draw_face(screen, cube[  : 9], F, F) # W
    draw_face(screen, cube[9 :18], F, 0) # R
    draw_face(screen, cube[18:27], 0, F) # B
    draw_face(screen, cube[27:36], 3*F, F) # Y
    draw_face(screen, cube[36:45], F, 2*F) # O 
    draw_face(screen, cube[45:54], 2*F, F) # G

    pygame.display.update()

def draw_face(screen, face: List[int], offset_x: float, offset_y: float):
    for i in range(9):
        val = face[i]
        W = 15
        pygame.draw.rect(
            screen,
            SquareColor.get_color(val),
            pygame.Rect(offset_x + (i % 3) * W, offset_y + (i // 3) * W, W-2, W-2)
        )

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello, World!")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                running = False
        render(screen)


if __name__ == "__main__":
    main()


