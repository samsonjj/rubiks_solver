import pygame
from typing import List, Self

class Permutation():
    def __init__(self):
        self.state = base()
    
    def t(self, b: List[int]):
        self.state = permute(self.state, b)
        return self

    def t_x(self, b: List[int], x: int):
        for i in range(x):
            self.state = permute(self.state, b)
        return self

    def out(self) -> List[int]:
        return self.state

def base() -> List[int]:
    return [
        0, 1, 2, 3, 4, 5, 6, 7, 8,
        9,10,11,12,13,14,15,16,17,
        18,19,20,21,22,23,24,25,26,
        27,28,29,30,31,32,33,34,35,
        36,37,38,39,40,41,42,43,44,
        45,46,47,48,49,50,51,52,53,
    ]

def permute(a: List[int], b: List[int]) -> List[int]:
    result = [None] * len(a)
    for i in range(len(a)):
        result[i] = a[b[i]]
    return result

def unpermute(a: List[int], b: List[int]) -> List[int]:
    result = [None] * len(a)
    for i in range(len(a)):
        result[b[i]] = a[i]
    return result

TS = [
    18,19,20,21,22,23,24,25,26,
    11,14,17,10,13,16,9,12,15,
    27,28,29,30,31,32,33,34,35,
    45,46,47,48,49,50,51,52,53, 
    42,39,36,43,40,37,44,41,38,
    0, 1, 2, 3, 4, 5, 6, 7, 8,
]

TS2 = [
    36,37,38,39,40,41,42,43,44,
    0, 1, 2, 3, 4, 5, 6, 7, 8,
    20,23,26,19,22,25,18,21,24,
    17,16,15,14,13,12,11,10,9,
    35,34,33,32,31,30,29,28,27,
    51,48,45,52,49,46,53,50,47,
]

TS2I = Permutation().t_x(TS2, 3).out()

TR = [
    0, 1,38, 3, 4,41, 6, 7,44,
    9,10, 2,12,13, 5,15,16, 8,
    18,19,20,21,22,23,24,25,26,
    17,28,29,14,31,32,11,34,35,
    36,37,33,39,40,30,42,43,27,
    45,46,47,48,49,50,51,52,53,
]
TRI = Permutation().t_x(TR, 3).out()
TSI = Permutation().t_x(TS, 3).out()

TF = Permutation().t(TS).t(TR).t(TSI).out()
TFI = Permutation().t_x(TF, 3).out()

TL = Permutation().t_x(TS, 2).t(TR).t_x(TS, 2).out()
TLI = Permutation().t_x(TL, 3).out()

TB = Permutation().t(TSI).t(TR).t(TS).out()
TBI = Permutation().t_x(TB, 3).out()

TD = Permutation().t(TS2).t(TF).t(TS2I).out()
TDI = Permutation().t_x(TD, 3).out()

TT = Permutation().t(TS2I).t(TF).t(TS2).out()
TTI = Permutation().t_x(TT, 3).out()

def as_str(a: List[int]) -> str:
    import json
    return json.dumps(a)

def as_code(a: List[int]) -> str:
    return "[\n  " + "\n  ".join([
        ", ".join([
            "{:>2}".format(a[x+y*9]) for x in range(9)
        ])
        for y in range(6)
    ]) + "\n]"

def get_color(x) -> pygame.Color:
    c = x // 9 + 1
    match c:
        case 1:
            return (255, 255, 255)
        case 2:
            return (255, 0, 0)
        case 3:
            return (0, 0, 255)
        case 4:
            return (255, 255, 0)
        case 5:
            return (0, 255, 0)
        case 6:
            return (255, 128, 20)

W = 50
F = 3 * W

def render(screen, state: List[int]):
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
        pygame.draw.rect(
            screen,
            get_color(val),
            pygame.Rect(offset_x + (i % 3) * W, offset_y + (i // 3) * W, W-2, W-2)
        )
        my_font = pygame.font.SysFont('Comic Sans MS', W // 2, True)
        text_surface = my_font.render(str(val), True, (0, 0, 0))
        screen.blit(text_surface, (offset_x + (i % 3) * W + .15 * W, offset_y + (i // 3) * W + .1 * W))

class Game:
    def __init__(self): 
        self.state = base()
        self.running = True

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello, World!")

    game = Game()
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            if event.type == pygame.KEYDOWN:
                handle_key_event(event, game)

        render(screen, game.state)

def handle_key_event(event, game: Game): 
    if event.key == pygame.K_ESCAPE:
        game.running = False

    key_helper(event, game, pygame.K_RIGHT, TS, TSI)
    key_helper(event, game, pygame.K_LEFT, TSI, TS)

    key_helper(event, game, pygame.K_UP, TS2, TS2I)
    key_helper(event, game, pygame.K_DOWN, TS2I, TS2)

    key_helper(event, game, pygame.K_d, TR, TRI)
    key_helper(event, game, pygame.K_r, TR, TRI)

    key_helper(event, game, pygame.K_f, TF, TFI)
    key_helper(event, game, pygame.K_SPACE, TF, TFI)

    key_helper(event, game, pygame.K_l, TL, TLI)
    key_helper(event, game, pygame.K_a, TL, TLI)

    key_helper(event, game, pygame.K_b, TB, TBI)
    key_helper(event, game, pygame.K_e, TB, TBI)

    key_helper(event, game, pygame.K_w, TT, TTI)
    key_helper(event, game, pygame.K_t, TT, TTI)

    key_helper(event, game, pygame.K_s, TD, TDI)


def key_helper(event, game, k, t1, t2):
    if event.key == k:
        if event.mod & pygame.KMOD_LSHIFT:
            game.state = permute(game.state, t2)
        else:
            game.state = permute(game.state, t1)


if __name__ == "__main__":
    main()
