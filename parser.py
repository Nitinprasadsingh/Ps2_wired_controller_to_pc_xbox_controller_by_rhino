def parse_line(line):
    parts = line.split()

    # Ignore short packets (the duplicate 4-value packets)
    if len(parts) < 5:
        return None

    # Accept only the full packets
    if parts[0] not in ("65", "115"):
        return None

    try:
        return {
            "LX": int(parts[1]),
            "LY": int(parts[2]),
            "RX": int(parts[3]),
            "RY": int(parts[4]),
            "BUTTONS": parts[5:] if len(parts) > 5 else []
        }
    except ValueError:
        return None