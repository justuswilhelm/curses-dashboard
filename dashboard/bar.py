#  GRAPH_SYMBOLS_VERTICAL = " ▁▂▃▄▅▆▇█" these are utterly useless
# GRAPH_SYMBOLS_HORIZONTAL = " ▏▎▍▌▋▊▉█"
# GRAPH_SYMBOLS_VERTICAL = "░▒▓█" these are ok
# GRAPH_SYMBOLS_VERTICAL = "⠀⠤⠶⠿"
GRAPH_SYMBOLS_VERTICAL = "⠀⣀⣤⣶⣿"
GRAPH_SYMBOLS_HORIZONTAL = "░▒▓█"


def scale(value, old_min, old_max, new_min=0, new_max=1):
    """
    >>> scale(1, -1, 1)
    1.0
    >>> scale(0, -1, 1)
    0.5
    >>> scale(-1, -1, 1)
    0.0
    """
    return (((value - old_min) * (new_max - new_min)) / (
        old_max - old_min)) + new_min


def symbol_vertical_oneline(signal, min=-1, max=1):
    """
    >>> symbol_vertical_oneline(1, -1, 1)
    '█'
    >>> symbol_vertical_oneline(-1, -1, 1)
    ' '
    """
    signal = int(scale(signal, min, max, 0, len(GRAPH_SYMBOLS_VERTICAL) - 1))
    return GRAPH_SYMBOLS_VERTICAL[signal]


def line_decomposition(signal, lines=2):
    """
    Expects a signal in [0, 1]

    >>> list(line_decomposition(1, 1))
    [1.0]
    >>> list(line_decomposition(1, 2))
    [1.0, 1.0]
    >>> list(line_decomposition(0, 2))
    [0.0, 0.0]
    >>> list(line_decomposition(0.5, 2))
    [1.0, 0.0]
    >>> list(line_decomposition(0.75, 2))
    [1.0, 0.5]
    >>> list(line_decomposition(1.0, 4))
    [1.0, 1.0, 1.0, 1.0]
    """
    signal = float(signal)
    line_max = 1 / lines
    for line_no in range(lines):
        yield max(min(line_max, signal) / line_max, 0.0)
        signal -= line_max


def symbol_horizontal_multiline(signal, lines, min=-1, max=1):
    r"""
    >>> symbol_vertical_multiline(1, 2)
    '██'
    >>> symbol_vertical_multiline(0, 2)
    ' █'
    >>> symbol_vertical_multiline(-1, 2)
    '  '
    """
    signal = scale(signal, min, max)
    line_values = line_decomposition(signal, lines)
    return (GRAPH_SYMBOLS_HORIZONTAL[
            int(value * (len(GRAPH_SYMBOLS_HORIZONTAL) - 1))]
            for value in line_values)


def symbol_vertical_multiline(signal, lines, min=-1, max=1):
    r"""
    >>> symbol_vertical_multiline(1, 2)
    '█\n█'
    >>> symbol_vertical_multiline(0, 2)
    ' \n█'
    >>> symbol_vertical_multiline(-1, 2)
    ' \n '
    """
    signal = scale(signal, min, max)
    line_values = line_decomposition(signal, lines)
    return reversed(list(
        GRAPH_SYMBOLS_VERTICAL[
            int(value * (len(GRAPH_SYMBOLS_VERTICAL) - 1))
        ]
        for value in line_values))


def join_symbol_columns(symbol_columns):
    """
    >>> list(join_symbol_columns(["123", "456"]))
    ['14', '25', '36']
    """
    for row in zip(*symbol_columns):
        yield ''.join(row)
