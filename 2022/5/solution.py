def transpose(array):
    return [[array[j][i] for j in range(len(array))] for i in range(len(array[0]))]

def parse_stack_row(row: str):
    return [row[i:i+4].replace("[", "").replace("]", "").strip() for i in range(0, len(row), 4)]

def remove_uneeded(stacks):
    return [[e for e in stack if e != ''] for stack in stacks]

def get_move(move: str):
    numbers = move.replace("move", "").replace(" from ", ",").replace(" to ", ",")
    return list(map(int, numbers.split(",")))

def parse_input(file: str):
    stacks, moves = open(file).read().split("\n\n")
    stacks, moves = stacks.split("\n"), moves.strip().split("\n")

    number_of_stacks = len(stacks)
    stacks = remove_uneeded(transpose([parse_stack_row(stack) for stack in stacks[:number_of_stacks - 1]]))
    moves = [get_move(move) for move in moves]
    return stacks, moves

def move_stacks(stacks, moves, ordered = True):
    for move in moves:
        quantity, origin, dest = move
        origin_stack = stacks[origin - 1]
        dest_stack = stacks[dest - 1]
        for q in range(quantity):
            if len(origin_stack) > 0:
                element = origin_stack.pop(0) # pop from stack
                dest_stack.insert(q if ordered else 0, element) # insert
    return stacks

def get_top_cranes(stacks):
    crates = []
    for stack in stacks:
        size = len(stack)
        if size > 0:
            crates.append(stack[0])
    return crates

stacks_1, moves_1 = parse_input("input.txt")
stacks_2 = [stack[:] for stack in stacks_1]
moves_2 = [move[:] for move in moves_1]
# Part One
final_stacks_1 = move_stacks(stacks_1, moves_1, False)
# Part Two
final_stacks_2 = move_stacks(stacks_2, moves_2)

# Answers
print(f"In part one crates {''.join(get_top_cranes(final_stacks_1))} end up on top of the stacks")
print(f"In part one crates {''.join(get_top_cranes(final_stacks_2))} end up on top of the stacks")