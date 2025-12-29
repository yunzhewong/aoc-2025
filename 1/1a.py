from dataclasses import dataclass

INITIAL_DIAL = 50
DIAL_RANGE = 100

@dataclass
class DialPoint:
    number: int

    def rotate(self, rotation: int):
        new_number = (self.number + rotation + DIAL_RANGE) % DIAL_RANGE
        return DialPoint(number=new_number) 
    
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
        dial = dial.rotate(action.rotation)
        if dial.number == 0:
            total += 1
    
    print(total)
