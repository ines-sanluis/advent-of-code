assignments = open("input.txt").read().strip().split("\n")

def create_range(assignment):
    start, end = map(int, assignment.split("-"))
    return set(range(start, end + 1))

fully_contained, overlaps = 0, 0
for pairs in assignments:
    pair = pairs.split(",")
    first_range = create_range(pair[0]) # range of first elf
    second_range = create_range(pair[1]) # range of second elf
    # Part One
    if first_range.issubset(second_range) or second_range.issubset(first_range): # if one of the range is a subset of the other they are fully contained
        fully_contained += 1
    # Part two
    if len(first_range & second_range) > 0: # if the intersection has at least one element is because they overlap
        overlaps += 1

# Answers
print(f"In {fully_contained} assignment pairs does one range fully contain the other")
print(f"The ranges overlap in {overlaps} assignments")