import mido


def list_inputs():
    inputs = mido.get_input_names()
    if not inputs:
        print("❌ No MIDI controllers found. Check your USB connection!")
        return None
    print("✅ Available MIDI Inputs:")
    for i, name in enumerate(inputs):
        print(f"  [{i}] {name}")
    return inputs


def monitor_midi(input_name):
    print(f"\n--- Monitoring {input_name} ---")
    print("Press keys on your controller to see their MIDI Note Numbers.")
    print("Press Ctrl+C to stop.\n")

    try:
        with mido.open_input(input_name) as inport:
            for msg in inport:
                if msg.type == "note_on" and msg.velocity > 0:
                    print(f"🎵 Note: {msg.note} | Velocity: {msg.velocity}")
    except KeyboardInterrupt:
        print("\nStopping discovery...")


if __name__ == "__main__":
    devices = list_inputs()
    if devices:
        # Usually, your controller is the first one in the list [0]
        monitor_midi(devices[0])
