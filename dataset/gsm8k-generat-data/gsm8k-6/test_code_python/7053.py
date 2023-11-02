def solution():
    # Calculate the remaining red and blue marbles
    remaining_red = 20 - 3  # take away 3 red marbles
    remaining_blue = 30 - (4 * 3)  # take away 4 times as many blue marbles as red marbles

    # Calculate the total marbles remaining
    total_marbles = remaining_red + remaining_blue
    result = total_marbles
    return result

print(solution())