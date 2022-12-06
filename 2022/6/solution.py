datastream = open("input.txt").read()

def get_start_of_marker(datastream, packet_size):
    for i in range(len(datastream)):
        sequence = datastream[i : i + packet_size]
        if len(set(sequence)) == packet_size:
            return i + packet_size

# Part One
print(f"Number of characters processed before the first start-of-packet marker: {get_start_of_marker(datastream, 4)}")
# Part Two
print(f"Number of characters processed before the first start-of-message marker: {get_start_of_marker(datastream, 14)}")