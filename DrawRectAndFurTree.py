import time
import os


# Drawing a rect and a fur tree

def draw_line(n=10, sym='X'):
    i = 0
    while i < n:
        print(sym, end='')
        i += 1


def draw_rect(n=10, sym='H'):
    i = 0
    while i < n:
        draw_line(n, sym)
        print()
        i += 1
        time.sleep(0.3)


def fur_tree(n=10, sym='#'):
    i = 0
    while i < n:
        draw_line(int((n - i) / 2), ' ')
        draw_line(i + 1, sym)
        print()
        i += 1
        time.sleep(0.3)


os.system('cls')
draw_rect(10, 'D')
fur_tree(12, '#')
