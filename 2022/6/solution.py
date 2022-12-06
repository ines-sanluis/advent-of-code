def get_start(datastream, size):
    for i in range(len(datastream)):
        sequence = datastream[i : i + size]
        if len(set(sequence)) == size:
            return i + size

datastream = open("input.txt").read()
# Part One
print(f"Number of characters processed before the first start-of-packet marker: {get_start(datastream, 4)}")
# Part Two
print(f"Number of characters processed before the first start-of-message marker: {get_start(datastream, 14)}")
