from dataclasses import dataclass
from typing import List

BATTERY_COUNT = 12

def calculate_joltage_from_selected(selected: List[int]):
    joltage = 0
    for battery in selected:
        joltage *= 10        
        joltage += battery
    return joltage


@dataclass
class Bank:
    batteries: List[int]

    @staticmethod
    def parse(s: str):
        return Bank([int(char) for char in s])
    
    def maximum_joltage(self):
        total = 0
        selectables = self.batteries[:]
        for batteries_to_choose in range(BATTERY_COUNT, 0, -1):
            required_afters = batteries_to_choose - 1
            best_next = max(selectables[:len(selectables) -1 * required_afters])

            total *= 10
            total += best_next

            best_next_index = selectables.index(best_next)
            selectables = selectables[best_next_index + 1:]

        return total 
    
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
        banks = [Bank.parse(line) for line in lines]
    
    total = 0
    for bank in banks:
        joltage = bank.maximum_joltage()
        total += joltage
    print(total)

def test_parse():
    assert Bank.parse("987654321111111") == Bank(batteries=[9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1])

def test_joltage_calc():
    assert Bank.parse("987654321111111").maximum_joltage() == 987654321111111