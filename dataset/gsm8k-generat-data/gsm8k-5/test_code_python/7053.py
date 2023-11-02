def solution():
    red_marbles = 20  # The top hat has 20 red marbles
    blue_marbles = 30  # The top hat has 30 blue marbles

    # Take away 3 red marbles and 4 times as many blue marbles as red marbles
    red_marbles -= 3
    blue_marbles -= 4 * 3

    # Calculate the total number of marbles left
    total_marbles = red_marbles + blue_marbles
    result = total_marbles
    return result

print(solution())