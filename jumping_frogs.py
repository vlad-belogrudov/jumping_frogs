#!/usr/bin/env python3

"""
Jumping frogs and lamps - we have a number of either.
All lamps are off at the beginning and have buttons in a row.
Frogs jump one after another. The first frog jumps on each button
starting with the first button, the second frog on button number 2,
4, 6... the third on button number 3, 6, 9...
This program emulates state of lamps (on, off)
"""


class Lamps:
    """This class represents state of lamps"""
    def __init__(self, num) -> None:
        """Initialize state of all lamps - all off"""
        self.state = [False for _ in range(0, num)]

    def __str__(self) -> str:
        """To string"""
        return "".join((str(int(s)) for s in self.state))

    def __int__(self) -> int:
        """To int"""
        return int(str(self), 2)

    def press(self, num) -> None:
        """Press button"""
        self.state[num] = not self.state[num]

if __name__ == "__main__":

    NUM_LAMPS = 10
    NUM_FROGS = 10

    lamps_state = Lamps(NUM_LAMPS) 

    for iteration in range(1, NUM_LAMPS + 1):
        for frog in range(1, NUM_LAMPS + 1):
            lamp_num = frog * iteration -1
            if lamp_num < NUM_LAMPS:
                lamps_state.press(lamp_num)
            else:
                break
        print(lamps_state)

    print(hex(int(lamps_state)))
