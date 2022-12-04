def get_compartments(rucksack):
    # The first half of the characters represent items in the first compartment
    # The second half of the characters represent items in the second compartment
    half = int(len(rucksack) / 2)
    return rucksack[:half], rucksack[half:]

def get_wrongly_packed(rubstack):
    # The item type that appears in both compartments of the rubstack needs to be rearranged
    first_compartment, second_compartment = get_compartments(rubstack)
    wrong = set(first_compartment) & set(second_compartment)
    return list(wrong)[0]

def get_priority(char: str):
    if char.islower(): # Lowercase item types a through z have priorities 1 through 26
        return ord(char) - 97
    else: # Uppercase item types A through Z have priorities 27 through 52
        return ord(char) - 38

def get_groups(input, n):
	for i in range(0, len(input), n):
		yield input[i : i + n]

def get_badge(group):
    # The one item type that is common between all three Elves in each group
    elf_1, elf_2, elf_3 = group
    badge = set(elf_1) & set(elf_2) & set(elf_3)
    return list(badge)[0]

rucksacks = open("input.txt").read().strip().split("\n")

# Part One
wrongly_packed = [get_wrongly_packed(r) for r in rucksacks]
priorities = sum(get_priority(p) for p in wrongly_packed)
print(f"The sum of the priorities of item types that appear in both compartments of each rucksack is {priorities}")

# Part Two
groups = get_groups(rucksacks, 3)
badges = [get_badge(group) for group in groups]
priorities = sum(get_priority(b) for b in badges)
print(f"The sum of the priorities of badges is {priorities}")
