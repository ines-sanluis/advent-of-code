
raw_input = open("input.txt").read()
replacements = {
    "A": "0",
    "B": "1",
    "C": "2",
    "X": "0",
    "Y": "1",
    "Z": "2"
}
games = raw_input.translate(raw_input.maketrans(replacements)).split("\n")
games = [map(int, game.split()) for game in games]

score_1 = 0
score_2 = 0
for game in games:
    [their_move, my_move] = list(game)
    # Part 1
    if my_move == their_move: score_1 += 3 # draw
    elif my_move == (their_move + 1) % 3: score_1 += 6 # win
    score_1 += my_move + 1 # lose
    # Part 2 -> second column is not my move but the match result
    if my_move == 0: score_2 += (their_move - 1) % 3 # lose
    elif my_move == 2: score_2 += 6 + (their_move + 1) % 3 # win
    else: score_2 += 3 + their_move # draw
    score_2 += 1

# Answers
print(f"In part one my total score would be {score_1}")
print(f"In part two my total score would be {score_2}")
