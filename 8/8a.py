from dataclasses import dataclass
from math import sqrt
from typing import Dict, List, Tuple

TOTAL_JOINS = 1000

@dataclass(frozen=True)
class BoxPosition:
    x: int
    y: int
    z: int

    @staticmethod
    def parse(s: str):
        split = s.split(",")
        x = int(split[0])
        y = int(split[1])
        z = int(split[2])
        return BoxPosition(x, y, z)
    
@dataclass(frozen=True)
class Pair:
    start: BoxPosition
    stop: BoxPosition

    def distance_between(self):
        return sqrt((self.start.x - self.stop.x) ** 2 + (self.start.y - self.stop.y) ** 2 + (self.start.z - self.stop.z) ** 2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
    box_positions = [BoxPosition.parse(line) for line in lines]

    distances: List[Tuple[Pair, float]] = []

    for i in range(len(box_positions)):
        for j in range(i + 1, len(box_positions)):
            pair = Pair(start=box_positions[i], stop=box_positions[j])
            distances.append((pair, pair.distance_between()))

    sorted_distances = sorted(distances, key=lambda x: x[1])

    circuits: List[List[BoxPosition]] = []

    for i in range(1000):
        pair, _ = sorted_distances[i]

        start_index = None
        stop_index = None
        for j, circuit in enumerate(circuits):
            if pair.start in circuit:
                start_index = j
            if pair.stop in circuit:
                stop_index = j
        
        if start_index is None and stop_index is None:
            circuits.append([pair.start, pair.stop])
        elif start_index is None and stop_index is not None:
            circuits[stop_index].append(pair.start)
        elif start_index is not None and stop_index is None:
            circuits[start_index].append(pair.stop)
        elif start_index is not None and stop_index is not None:
            if start_index == stop_index:
                continue
            new_circuits = []
            for j in range(len(circuits)):
                if j == start_index or j == stop_index:
                    continue
                new_circuits.append(circuits[j])
            new_circuits.append(circuits[start_index] + circuits[stop_index])
            circuits = new_circuits

    lengths = [len(circuit) for circuit in circuits]
    sorted_lengths = sorted(lengths)
    total = sorted_lengths[-1] * sorted_lengths[-2] * sorted_lengths[-3]
    print(total)