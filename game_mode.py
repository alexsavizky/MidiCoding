import mido
import pydirectinput
import pygame.midi


def handle_gaming():
    # Identify Controller
    port_name = [n for n in mido.get_input_names() if "MPK Mini" in n][0]

    print(f"🤠 RDR2 MIDI-Controller Active on: {port_name}")

    with mido.open_input(port_name) as inport:
        for msg in inport:
            # When you press the key down
            if msg.type == "note_on" and msg.velocity > 0:
                if msg.note in GAME_MAP:
                    key = GAME_MAP[msg.note]
                    if key == "mouse_left":
                        pydirectinput.mouseDown()
                    else:
                        pydirectinput.keyDown(key)

            # When you lift your finger
            elif msg.type == "note_off" or (
                msg.type == "note_on" and msg.velocity == 0
            ):
                if msg.note in GAME_MAP:
                    key = GAME_MAP[msg.note]
                    if key == "mouse_left":
                        pydirectinput.mouseUp()
                    else:
                        pydirectinput.keyUp(key)


if __name__ == "__main__":
    from config import GAME_MAP

    handle_gaming()
