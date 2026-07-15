import time
from parser import parse_line


def calibrate(ser):
    print("=" * 40)
    print(" Leave the controller untouched ")
    print(" Calibrating for 3 seconds...")
    print("=" * 40)

    samples = []

    start = time.time()

    while time.time() - start < 3:

        line = ser.readline().decode(errors="ignore").strip()

        data = parse_line(line)

        if data:
            samples.append(data)

    lx = sum(s["LX"] for s in samples) / len(samples)
    ly = sum(s["LY"] for s in samples) / len(samples)
    rx = sum(s["RX"] for s in samples) / len(samples)
    ry = sum(s["RY"] for s in samples) / len(samples)

    print()

    print("Calibration Complete")

    print(f"LX = {lx:.1f}")
    print(f"LY = {ly:.1f}")
    print(f"RX = {rx:.1f}")
    print(f"RY = {ry:.1f}")

    return lx, ly, rx, ry