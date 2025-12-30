from dataclasses import dataclass
from typing import List

@dataclass
class Section:
    start: int
    stop: int

@dataclass
class NumberRow:
    text: str

    def get(self, section: Section):
        return self.text[section.start:section.stop]

@dataclass
class OperationRow:
    text: str

    def find_sections(self):
        sections: List[Section] = []

        start = 0
        for i, char in enumerate(self.text[1:]):
            if char == " ":
                continue

            sections.append(Section(start, i))
            start = i + 1

        sections.append(Section(start, len(self.text)))
        return sections
    
    def get(self, section: Section):
        return self.text[section.start]
             
if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().split("\n")
    number_rows = [NumberRow(line) for line in lines[:-1]]
    operation_row = OperationRow(lines[-1])
    
    sections = operation_row.find_sections()

    total = 0 
    for section in sections:
        strings = [number_row.get(section) for number_row in number_rows]
        numbers: List[int] = []
        for i in range(len(strings[0])):
            number_str = "".join([string[i] for string in strings])
            numbers.append(int(number_str))
        operation = operation_row.get(section)
        calculation = f" {operation} ".join([str(number) for number in numbers])
        output = eval(calculation)
        total += output
    print(total)
