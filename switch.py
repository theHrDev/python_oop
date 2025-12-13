
class LightSwitch:
    def __init__(self):
        self._is_on = False  # private internal state

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def toggle(self):
        self._is_on = not self._is_on

    def get_status(self):
        return "ON" if self._is_on else "OFF"


switch = LightSwitch()

print(switch.get_status())   # OFF
switch.turn_on()
print(switch.get_status())   # ON
switch.toggle()
print(switch.get_status())   # OFF
switch.turn_off()
print(switch.get_status())   # OFF

