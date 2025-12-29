from dataclasses import dataclass
from math import floor

INITIAL_DIAL = 50
DIAL_RANGE = 100

@dataclass
class DialPoint:
    number: int

    def rotate(self, rotation: int):
        cycles = int(rotation / DIAL_RANGE)
        cycle_clicks = abs(cycles)
        trimmed_rotation = rotation - cycles * DIAL_RANGE
        raw_new_number = self.number + trimmed_rotation
        new_number = (raw_new_number + DIAL_RANGE) % DIAL_RANGE

        # if we are on zero, and we have trimmed the rotation to be less than DIAL_RANGE, there is no way for us to create another click through movement
        # in any other case, it is always possible to trigger a zero click
        if self.number == 0:
            return DialPoint(number=new_number), cycle_clicks
        
        passage_clicks = 0
        positive_pass = raw_new_number > DIAL_RANGE
        negative_pass = raw_new_number < 0
        land_on_zero = raw_new_number % DIAL_RANGE == 0  
        if positive_pass or negative_pass or land_on_zero:
            passage_clicks = 1
        zero_clicks = cycle_clicks + passage_clicks
        return DialPoint(number=new_number), zero_clicks 
    
@dataclass
class DialAction:
    rotation: int

    @staticmethod
    def parse(s: str):
        direction_char = s[0]
        amount = int(s[1:])

        if direction_char == "L":
            return DialAction(-1 * amount)
        return DialAction(amount)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
        actions = [DialAction.parse(line) for line in lines]
    
    dial = DialPoint(INITIAL_DIAL)

    total = 0
    for action in actions:
        dial, clicks = dial.rotate(action.rotation)
        print(dial, clicks)
        total += clicks
        
    print(total)
