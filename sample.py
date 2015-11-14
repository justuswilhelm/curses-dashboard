#!/usr/bin/env python
from curses import wrapper, newwin, curs_set
from math import sin
from time import sleep, time

from dashboard.bar import (
    symbol_vertical_multiline,
    symbol_horizontal_multiline,
    join_symbol_columns,
)


A_DIM = [10, 20]
B_DIM = [10, 20]


def draw_a(a):
    a.clear()

    a.border()

    signal = [sin(a + 4. * time()) for a in range(1, A_DIM[1] - 2)]

    columns = [
        symbol_vertical_multiline(s, A_DIM[0] - 2)
        for s in signal
    ]
    joined_columns = list(join_symbol_columns(columns))
    for row_no, row in enumerate(joined_columns):
        a.addstr(1 + row_no, 1, row)

    a.refresh()


def draw_b(b):
    b.clear()
    b.border()

    signal = [sin(a + 4. * time()) for a in range(1, A_DIM[0] - 1)]

    rows = [
        symbol_horizontal_multiline(s, A_DIM[1] - 2)
        for s in signal
    ]
    for row_no, row in enumerate(rows):
        b.addstr(row_no + 1, 1, ''.join(row))
    b.refresh()


def main(stdscr):
    curs_set(0)

    a = newwin(*A_DIM, 1, 1)
    b = newwin(*B_DIM, 11, 1)
    while True:
        stdscr.border()
        stdscr.refresh()
        draw_a(a)
        draw_b(b)
        sleep(0.1)


if __name__ == "__main__":
    wrapper(main)
