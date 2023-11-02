def solution():
    red_marbles = 20
    blue_marbles = 30

    # Remove 3 red marbles
    red_marbles -= 3

    # Remove 4 times as many blue marbles as red marbles
    blue_remove = 4 * 3
    blue_marbles -= blue_remove

    # Calculate the total number of remaining marbles
    total_marbles = red_marbles + blue_marbles
    result = total_marbles
    return result

print(solution())