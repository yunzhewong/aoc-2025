from dataclasses import dataclass
from typing import List, Set

START = "S"
SPLITTER = "^"

@dataclass
class Map:
    rows: List[str]

    def find_start(self):
        return self.rows[0].index(START)
    
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
    beam_locations = set([start])
    for i in range(len(map.rows)):
        occupied: Set[int] = set([])
        splitter_indexes = map.find_splitter_indexes(i)
        for beam_location in beam_locations:
            if beam_location in splitter_indexes:
                occupied.add(beam_location - 1)
                occupied.add(beam_location + 1)
                total += 1
            else:
                occupied.add(beam_location)
        beam_locations = occupied
    print(total)