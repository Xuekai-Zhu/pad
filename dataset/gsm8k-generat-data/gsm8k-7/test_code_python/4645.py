def solution():
    total_marbles = 50
    num_white = 20
    num_red = num_blue = (total_marbles - num_white) / 2  # equal number of red and blue marbles
    num_removed = 2 * abs(num_white - num_blue)

    # Calculate the number of marbles left in the box
    num_left = total_marbles - num_removed
    result = num_left
    return result

print(solution())