from dataclasses import dataclass
from typing import List


@dataclass
class IDRange:
    start: int
    stop: int

    @staticmethod
    def parse(s: str):
        split = s.split("-")
        start = int(split[0])
        stop = int(split[1])
        return IDRange(start=start, stop=stop)
    
    def compute_in_range(self):
        return self.stop - self.start + 1
    
    def in_range(self, ingredient_id: int):
        return ingredient_id >= self.start and ingredient_id <= self.stop


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    space_index = lines.index("")

    id_ranges = [IDRange.parse(line) for line in lines[:space_index]]

    merged_ranges: List[IDRange] = []
    for id_range in id_ranges:
        remove_indices = []
        new_range = IDRange(id_range.start, id_range.stop)
        for i, merged_range in enumerate(merged_ranges):
            if merged_range.in_range(new_range.start):
                new_range = IDRange(merged_range.start, new_range.stop)
                remove_indices.append(i)
            if merged_range.in_range(new_range.stop):
                new_range = IDRange(new_range.start, merged_range.stop)
                remove_indices.append(i)
            if new_range.in_range(merged_range.start) and new_range.in_range(merged_range.stop):
                remove_indices.append(i)

        new_ranges = [new_range]
        for i in range(len(merged_ranges)):
            if i in remove_indices:
                continue
            new_ranges.append(merged_ranges[i])
        merged_ranges = new_ranges
    
    total = 0
    for merged_range in merged_ranges:
        total += merged_range.compute_in_range()
    print(total)