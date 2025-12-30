from dataclasses import dataclass

def is_duplicated(s: str, duplicate_size: int):
    duplicates = int(len(s) / duplicate_size) 
    return s == "".join(s[:duplicate_size] * duplicates) 

def is_invalid(id: int):
    as_str = str(id)
    for i in range(1, int(len(as_str) / 2) + 1):
        if is_duplicated(as_str, i):
            return True
    return False

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

def test_duplicate_size():
    assert is_duplicated("111111", 1)
    assert is_duplicated("111111", 2)
    assert is_duplicated("111111", 3)
    assert is_duplicated("121212", 2)
    assert not is_duplicated("121212", 3)

def test_invalid():
    assert is_invalid(11)
    assert is_invalid(22)
    assert is_invalid(12341234)
    assert is_invalid(123123123)
    assert is_invalid(1212121212)
    assert is_invalid(1111111)
