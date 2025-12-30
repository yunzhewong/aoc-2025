from dataclasses import dataclass
from typing import List

@dataclass
class Bank:
    batteries: List[int]

    @staticmethod
    def parse(s: str):
        return Bank([int(char) for char in s])

    def maximum_joltage(self):
        best_start = max(self.batteries[:-1])
        best_start_index = self.batteries.index(best_start)
        best_stop = max(self.batteries[best_start_index + 1:])
        return best_start * 10 + best_stop
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

def test_best_joltage():
    assert Bank.parse("987654321111111").maximum_joltage() == 98