from dataclasses import dataclass
from typing import List, Set

START = "S"
SPLITTER = "^"

@dataclass
class Map:
    rows: List[str]

    def find_start(self):
        return self.rows[0].index(START)
    
    def width(self):
        return len(self.rows[0])
    
    def find_splitter_indexes(self, index: int):
        row = self.rows[index]
        splitter_indices: Set[int] = set([])
        for i, char in enumerate(row):
            if char == SPLITTER:
                splitter_indices.add(i)
        return splitter_indices

if __name__ == "__main__":
    with open("input.txt") as f:
        map = Map(f.read().split("\n"))

    start = map.find_start()

    total = 0
    beam_counts: List[int] = [0 for _ in range(map.width())]
    beam_counts[start] = 1
    for i in range(len(map.rows)):
        occupied: List[int] = [0 for _ in range(map.width())]
        splitter_indexes = map.find_splitter_indexes(i)
        for j, count in enumerate(beam_counts):
            if count != 0:
                if j in splitter_indexes:
                    occupied[j - 1] += count
                    occupied[j + 1] += count
                else:
                    occupied[j] += count
        beam_counts = occupied[:]
    print(sum(beam_counts))