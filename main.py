import mido
import pyautogui
import pygame.midi
import config  # Import our new mapping file
from threading import Timer

# Initialize Sound
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(config.INSTRUMENT)


# State Management
current_mode = 0  # 0:CODE, 1:ALPHA, 2:SYMBOLS, 3:NAV
active_notes = set()
buffer_timer = None


def process_input():
    global active_notes, current_mode
    chord = frozenset(active_notes)

    # 1. ALPHA/SYMBOL TOGGLE (Am7)
    if chord == config.ALPHA_TOGGLE_CHORD:
        # Toggle between 0, 1, and 2. If in 3, go to 0.
        if current_mode == 3 or current_mode == 2:
            current_mode = 0
        else:
            current_mode += 1
        print_mode()
        return

    # 2. NAVIGATION TOGGLE (Fmaj7)
    if chord == config.NAV_TOGGLE_CHORD:
        if current_mode == 3:
            current_mode = 0  # Return to CODE mode
        else:
            current_mode = 3  # Jump to NAV mode
        print_mode()
        return

    # 3. HANDLE SINGLE NOTES BASED ON MODE
    if len(active_notes) == 1:
        note = list(active_notes)[0]

        # --- MODE 3: NAVIGATION ---
        if current_mode == 3:
            if note in config.NAV_MAP:
                key = config.NAV_MAP[note]
                pyautogui.press(key)
                return

        # --- MODE 1: ALPHA ---
        elif current_mode == 1:
            if note in config.ALPHABET_MAP:
                pyautogui.write(config.ALPHABET_MAP[note])
                return

        # --- MODE 2: SYMBOLS ---
        elif current_mode == 2:
            if note in config.SYMBOL_MAP:
                pyautogui.write(config.SYMBOL_MAP[note])
                return

    # 4. CHORD LOGIC (Global or Mode 0)
    if chord in config.CHORD_MAP and current_mode == 0:
        text = config.CHORD_MAP[chord]
        pyautogui.write(text)
        if text.endswith("):"):
            pyautogui.press("left", presses=2)
        elif text.endswith("()"):
            pyautogui.press("left")


def print_mode():
    modes = ["CODE", "ALPHA", "SYMBOLS", "NAV"]
    print(f"🔄 Current Mode: {modes[current_mode]}")


def handle_midi():
    global buffer_timer
    try:
        port_name = [n for n in mido.get_input_names() if "MPK Mini" in n][0]
    except IndexError:
        print("❌ MPK Mini not found!")
        return

    print(f"🎹 MidiCoding Engine running...")
    print(
        f"📖 Loaded {len(config.CHORD_MAP)} chords and {len(config.SYMBOL_MAP)} single maps."
    )

    with mido.open_input(port_name) as inport:
        for msg in inport:
            if msg.type == "note_on" and msg.velocity > 0:
                player.note_on(msg.note, msg.velocity)
                active_notes.add(msg.note)

                if buffer_timer:
                    buffer_timer.cancel()
                buffer_timer = Timer(config.DEBOUNCE_TIME, process_input)
                buffer_timer.start()

            elif msg.type == "note_off" or (
                msg.type == "note_on" and msg.velocity == 0
            ):
                player.note_off(msg.note, 0)
                if msg.note in active_notes:
                    active_notes.remove(msg.note)


if __name__ == "__main__":
    try:
        handle_midi()
    finally:
        del player
        pygame.midi.quit()
