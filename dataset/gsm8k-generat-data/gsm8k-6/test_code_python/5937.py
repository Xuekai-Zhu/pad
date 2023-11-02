def solution():
    # Calculate the total number of marbles per color
    total_marbles = 72
    marbles_per_color = total_marbles / 3

    # Calculate the number of lost marbles
    red_lost = 5
    blue_lost = 2 * red_lost
    yellow_lost = 3 * red_lost

    # Calculate the remaining number of marbles per color
    red_remaining = marbles_per_color - red_lost
    blue_remaining = marbles_per_color - blue_lost
    yellow_remaining = marbles_per_color - yellow_lost

    # Calculate the total number of remaining marbles
    total_remaining = red_remaining + blue_remaining + yellow_remaining
    result = total_remaining
    return result

print(solution())