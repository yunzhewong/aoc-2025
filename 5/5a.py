from dataclasses import dataclass


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
    
    def in_range(self, ingredient_id: int):
        return ingredient_id >= self.start and ingredient_id <= self.stop

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    space_index = lines.index("")

    id_ranges = [IDRange.parse(line) for line in lines[:space_index]]
    ingredients = [int(line) for line in lines[space_index + 1:]]

    fresh_count = 0
    for ingredient in ingredients:
        fresh = False
        for id_range in id_ranges:
            if id_range.in_range(ingredient):
                fresh = True
                break
        if fresh:
            fresh_count += 1
    print(fresh_count)