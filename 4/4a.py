from dataclasses import dataclass
from typing import List

PAPER_ROLL = "@"
MAX_ROLLS = 4

@dataclass
class Map():
    arrays: List[str]

    @staticmethod
    def parse(arrays: List[str]):
        return Map(arrays=arrays)
    
    def rows(self):
        return len(self.arrays)

    def columns(self):
        return len(self.arrays[0])

    def get(self, row: int, column: int):
        if row < 0 or row >= self.rows():
            return None
        if column < 0 or column >= self.columns():
            return None
        return self.arrays[row][column]
    
if __name__ == "__main__":
    with open("input.txt") as f:
        map = Map.parse(f.read().split("\n"))

    total = 0
    for center_row in range(map.rows()):
        for center_column in range(map.columns()):
            if map.get(center_row, center_column) != PAPER_ROLL:
                continue

            paper_rolls = 0
            shifts = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

            for (row_shift, column_shift) in shifts:
                query_row = center_row + row_shift
                query_column = center_column + column_shift

                item_at = map.get(query_row, query_column)
                if item_at == PAPER_ROLL:
                    paper_rolls += 1

            if paper_rolls < MAX_ROLLS:
                total += 1

    print(total)

            
