# The "Magic Chord" to toggle Alphabet Mode
# Am7: A, C, E, G (MIDI: 57, 60, 64, 67)
ALPHA_TOGGLE_CHORD = frozenset([57, 60, 64, 67])
NAV_TOGGLE_CHORD = frozenset([53, 57, 60, 64])
# Note 48 (Low C) = 'a', 49 = 'b', etc.
ALPHABET_MAP = {48 + i: chr(97 + i) for i in range(25)}
# This maps:
# 48 -> a
# 49 -> b
# ...
# 72 -> y (We'll use a Pad for 'z')
# Mode 2: Symbols (Starting at Note 48)
SYMBOL_MAP = {
    48: "z",  # c1
    49: "(",  # c#
    50: ")",  # d
    51: "[",  # d#
    52: "]",  # e
    53: "{",  # f
    54: "}",  # f#
    55: ":",  # g
    56: "=",  # g#
    57: "+",  # a
    58: "-",  # a#
    59: "*",  # b
    60: "/",  # c2
    61: ",",  # c#
    62: ".",  # d
    63: "<",  # d#
    64: ">",  # e
    65: "!",  # f
    66: "_",  # f#
    67: '"',  # g
    68: "'",  # g#
    72: "backspace",  # a
}

# Navigation Map (Starting from Low C / 48)
NAV_MAP = {
    48: "left",
    49: "down",
    50: "up",
    51: "right",
    52: "enter",
    53: "space",
    54: "backspace",
    # You can add more like Home/End or Page Up/Down
    55: "home",
    56: "end",
}
CHORD_MAP = {
    frozenset([48, 52, 55]): "def ",  # C
    frozenset([50, 53, 57]): "for ",  # Dm
    frozenset([52, 55, 59]): "if ",  # Em
    frozenset([53, 57, 60]): "return ",  # F
    frozenset([55, 59, 62]): "in enumerate():",  # G
    frozenset([57, 60, 64]): "in ",  # am
}
# --- Settings ---
DEBOUNCE_TIME = 0.08  # Seconds to wait for a chord to complete
INSTRUMENT = 0

# config_rdr2.py

# Map MIDI notes to Game Keys
# Based on your MPK Mini (48-72)
GAME_MAP = {
    48: "a",  # Low C -> Steer Left
    50: "w",  # D -> Move Forward / Gallop
    52: "d",  # E -> Steer Right
    53: "s",  # F -> Slow Down / Reverse
    54: "shift",  # Pad 1 -> Sprint (Hold for Gallop)
    56: "space",  # Pad 2 -> Jump / Rear Horse
    57: "e",  # Pad 3 -> Mount / Interact
    58: "r",  # Pad 4 -> Reload
    60: "mouse_left",  # Middle C -> Shoot
    72: "v",  # High C -> Change Camera
}
a
