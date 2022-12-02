raw_input = open("input.txt").read()
replacements = {
    "A": "0",
    "B": "1",
    "C": "2",
    "X": "0",
    "Y": "1",
    "Z": "2"
}
draw_points = 3
win_points = 6
games = raw_input.translate(raw_input.maketrans(replacements)).split("\n")
games = [map(int, game.split()) for game in games]

number_of_games = len(games)
scores = [number_of_games, number_of_games] # compensates mapping to a zero-based indexing
for game in games:
    their_move, my_move = game
    winning_move = (their_move + 1) % 3
    losing_move = (their_move - 1) % 3
    # Part 1
    if my_move == their_move: scores[0] += draw_points # draw
    elif my_move == winning_move: scores[0] += win_points # win
    scores[0] += my_move
    # Part 2 -> second column is not my move but the match result
    if my_move == 0: scores[1] += losing_move # lose
    elif my_move == 2: scores[1] += win_points + winning_move # win
    else: scores[1] += draw_points + their_move # draw

# Answers
print(f"In part one my total score would be {scores[0]}")
print(f"In part two my total score would be {scores[1]}")
