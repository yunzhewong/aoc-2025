from dataclasses import dataclass

def is_invalid(id: int):
    as_str = str(id)
    if len(as_str) % 2 != 0:
        return False
    half_length = int(len(as_str) / 2)
    return as_str[:half_length] == as_str[half_length:]

@dataclass
class IDRange():
    start: int 
    stop: int

    @staticmethod
    def parse(s: str):
        split = s.split("-")
        start = int(split[0])
        stop = int(split[1])
        return IDRange(start=start, stop=stop)

    def identify_invalids(self):
        invalids = []
        for i in range(self.start, self.stop + 1):
            if is_invalid(i):
                invalids.append(i)
        return invalids

if __name__ == "__main__":
    with open("input.txt") as f:
        strings = f.read().split(",")
        id_ranges = [IDRange.parse(string) for string in strings]

    total = 0
    for id_range in id_ranges:
        invalids = id_range.identify_invalids()
        total += sum(invalids)
    print(total)

def test_parse():
    parsed = IDRange.parse("11-22")
    assert parsed.start == 11
    assert parsed.stop == 22