import vgamepad as vg

class XboxController:

    def __init__(self):
        self.gamepad = vg.VX360Gamepad()

    def press(self, button):
        self.gamepad.press_button(button=button)
        self.gamepad.update()

    def release(self, button):
        self.gamepad.release_button(button=button)
        self.gamepad.update()

    def left_stick(self, x, y):
        self.gamepad.left_joystick_float(
            x_value_float=x,
            y_value_float=y
        )
        self.gamepad.update()

    def right_stick(self, x, y):
        self.gamepad.right_joystick_float(
            x_value_float=x,
            y_value_float=y
        )
        self.gamepad.update()