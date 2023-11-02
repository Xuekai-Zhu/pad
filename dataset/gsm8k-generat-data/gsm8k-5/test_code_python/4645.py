def solution():
    # Calculate the original number of red and blue marbles
    original_white = 20
    original_red = original_blue = (50 - original_white) / 2

    # Calculate the number of marbles Jack removes
    difference = original_white - original_blue
    removed_marbles = 2 * abs(difference)

    # Calculate the number of marbles left in the box
    remaining_marbles = 50 - removed_marbles

    result = remaining_marbles
    return result

print(solution())