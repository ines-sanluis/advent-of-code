# Part 1
elves_input = open("input.txt").read().strip().split("\n\n")
elves_calories = [sum(map(int, elf.split("\n"))) for elf in elves_input]
sorted_elves_calories = sorted(elves_calories)
most_calories = sorted_elves_calories[-1]
best_elf = elves_calories.index(most_calories) + 1

# Part 2
best_three = sorted_elves_calories[-3:]
second_helf = elves_calories.index(best_three[1]) + 1
third_helf = elves_calories.index(best_three[0]) + 1

# Answers
print(f"Elf number {best_elf} is carrying the most calories with a total of {most_calories} calories")
print(f"Elfs {best_elf}, {second_helf} and {third_helf} are carrying a total of {sum(best_three)} calories")
