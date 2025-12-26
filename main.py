import pygame
from typing import List, Self

class Permutation:
    @staticmethod
    def base_of_54() -> Self:
        return Permutation(list(range(54)))

    def __init__(self, data: List[int]):
        self.data = data
    
    def permute(self, p: Self) -> Self: 
        data = [None] * 54
        for i in range(len(p.data)):
            data[i] = self.data[p[i]]
        return Permutation(data)
    
    def unpermute(self, p: Self) -> Self:
        data = [None] * 54
        for i in range(len(p.data)):
            data[p[i]] = self.data[i]
        return Permutation(data)
    
    def as_str(self) -> str:
        import json
        return json.dumps(self.data)
    
    def as_code(self) -> str:
        return "[\n  " + "\n  ".join([
            ", ".join([
                "{:>2}".format(self.data[x+y*9]) for x in range(9)
            ])
            for y in range(6)
        ]) + "\n]"



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

class Cube:
    def __init__(self):
        self.state = [
            1, 1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2, 2, 2, 2, 2, 2,
            3, 3, 3, 3, 3, 3, 3, 3, 3,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 
            5, 5, 5, 5, 5, 5, 5, 5, 5,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 
        ]
        self.stateb = [
            1, 1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2, 2, 2, 2, 2, 2,
            3, 3, 3, 3, 3, 3, 3, 3, 3,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 
            5, 5, 5, 5, 5, 5, 5, 5, 5,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 
        ]

    def t_None():
        return [
             0, 1, 2, 3, 4, 5, 6, 7, 8,
             9,10,11,12,13,14,15,16,17,
            18,19,20,21,22,23,24,25,26,
            27,28,29,30,31,32,33,34,35,
            36,37,38,39,40,41,42,43,44,
            45,46,47,48,49,50,51,52,53,
        ]
    
    def t_ROTATE(self):
        t = [
            18,19,20,21,22,23,24,25,26,
             9,10,11,12,13,14,15,16,17,
            27,28,29,30,31,32,33,34,35,
            45,46,47,48,49,50,51,52,53, 
            36,37,38,39,40,41,42,43,44,
             0, 1, 2, 3, 4, 5, 6, 7, 8,
        ]
        self.apply_t(t)
    
    def t_R(self):
        t = [
             0, 1,38, 3, 4,39, 6, 7,44,
             9,10, 2,12,13, 5,15,16, 8,
            18,19,20,21,22,23,24,25,26,
            27,28,29,30,31,32,33,34,35,
            36,37,38,39,40,48,42,43,44,
            45,46,47,48,49,50,51,52,53,
        ]

        self.apply_t(t)
    
    def t_print(t):
        pass

    
    def apply_t(self, t):
        for i in range(len(self.state)):
            self.stateb[i] = self.state[t[i]]

        (self.state, self.stateb) = (self.stateb, self.state)


def render(screen):
    cube = Cube()
    cube.t_ROTATE()
    state = cube.state

    draw_face(screen, state[  : 9],   F,   F, 0) # W
    draw_face(screen, state[9 :18],   F,   0, 9) # R
    draw_face(screen, state[18:27],   0,   F, 18) # B
    draw_face(screen, state[27:36], 3*F,   F, 27) # Y
    draw_face(screen, state[36:45],   F, 2*F, 36) # O 
    draw_face(screen, state[45:54], 2*F,   F, 45) # G

    pygame.display.update()

def draw_face(screen: pygame.Surface, face: List[int], offset_x: float, offset_y: float, n = 0):
    for i in range(9):
        val = face[i]
        W = 15
        pygame.draw.rect(
            screen,
            SquareColor.get_color(val),
            pygame.Rect(offset_x + (i % 3) * W, offset_y + (i // 3) * W, W-2, W-2)
        )
        my_font = pygame.font.SysFont('Comic Sans MS', 8)
        text_surface = my_font.render(str(n + i), False, (0, 0, 0))
        screen.blit(text_surface, (offset_x + (i % 3) * W, offset_y + (i // 3) * W))


def main():
    pygame.init()
    pygame.font.init()
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


