from dataclasses import dataclass
from typing import List, Tuple

NOTHING = "."
PAPER_ROLL = "@"
MAX_ROLLS = 4

@dataclass
class Map():
    arrays: List[str]

    @staticmethod
    def parse(arrays: List[str]):
        return Map(arrays=arrays)
    
    @staticmethod
    def from_original_with_removals(original: "Map", locations: List[Tuple[int, int]]):
        modified_arrays = original.arrays[:]
        for (remove_row, remove_column) in locations:
            modified_arrays[remove_row] = modified_arrays[remove_row][:remove_column] + NOTHING + modified_arrays[remove_row][remove_column + 1:]
        return Map(arrays=modified_arrays)
    
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
    
    def removable_paper_roll(self, row: int, column: int):
        if self.get(row, column) != PAPER_ROLL:
            return False

        paper_rolls = 0
        shifts = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        for (row_shift, column_shift) in shifts:
            query_row = row + row_shift
            query_column = column + column_shift

            item_at = map.get(query_row, query_column)
            if item_at == PAPER_ROLL:
                paper_rolls += 1

        return paper_rolls < MAX_ROLLS
    
if __name__ == "__main__":
    with open("input.txt") as f:
        map = Map.parse(f.read().split("\n"))

    all_removed = 0
    while True:
        removals = []
        for center_row in range(map.rows()):
            for center_column in range(map.columns()):
                if map.removable_paper_roll(center_row, center_column):
                    removals.append((center_row, center_column))

        if len(removals) == 0:
            break

        all_removed += len(removals)
        map = Map.from_original_with_removals(map, removals)

    print(all_removed)

            
