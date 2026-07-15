from calibrate import calibrate


import serial
import vgamepad as vg

from parser import parse_line
from mapper import button_map

import serial.tools.list_ports

port = None





for p in serial.tools.list_ports.comports():
    if "CH340" in p.description:
        port = p.device
        break

if port is None:
    raise Exception("Rhino controller not found!")

print("Connected to", port)

ser = serial.Serial(port, 57600)
center_lx, center_ly, center_rx, center_ry = calibrate(ser)

gamepad = vg.VX360Gamepad()

print("Controller Running...")

previous_data = None

previous_buttons = set()
previous_l2 = False
previous_r2 = False




def normalize(value, center):

    value = (value - center) / 128

    if abs(value) < 0.08:
        return 0

    return max(-1, min(1, value))




try:
    while True:

        line = ser.readline().decode(errors="ignore").strip()

        data = parse_line(line)

        if data is None:
            continue
        if data == previous_data:
            continue

        previous_data = data

        # #temporary print for debugging
        # print(data)


        # Left stick
        x = normalize(data["LX"], center_lx)
        y = -normalize(data["LY"], center_ly)

        gamepad.left_joystick_float(x, y)

        rx = normalize(data["RX"], center_rx)
        ry = -normalize(data["RY"], center_ry)

        gamepad.right_joystick_float(rx, ry)



        # Buttons
        current_buttons = {b for b in data["BUTTONS"]}

        # Release buttons
        for btn in previous_buttons - current_buttons:
            if btn in button_map:
                gamepad.release_button(button=button_map[btn])

        # Press buttons
        for btn in current_buttons - previous_buttons:
            if btn in button_map:
                gamepad.press_button(button=button_map[btn])

        previous_buttons = current_buttons

        # -------- L2 Trigger --------
        l2 = "L2" in current_buttons

        if l2 != previous_l2:
            gamepad.left_trigger(value=255 if l2 else 0)
            previous_l2 = l2

        # -------- R2 Trigger --------
        r2 = "R2" in current_buttons

        if r2 != previous_r2:
            gamepad.right_trigger(value=255 if r2 else 0)
            previous_r2 = r2

        gamepad.update()
except KeyboardInterrupt:
    print("\nClosing controller...")

    gamepad.reset()
    gamepad.update()

    ser.close()

    print("Done!")