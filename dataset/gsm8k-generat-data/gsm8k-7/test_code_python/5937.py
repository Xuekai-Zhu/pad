def solution():
    total_marbles = 72
    num_colors = 3

    # Calculate the number of marbles per color
    marbles_per_color = total_marbles / num_colors

    # Calculate the new number of each color after losing some
    red_marbles = marbles_per_color - 5
    blue_marbles = marbles_per_color - (2*5)
    yellow_marbles = marbles_per_color - (3*5)

    # Calculate the total number of marbles left
    total_left = red_marbles + blue_marbles + yellow_marbles
    result = total_left
    return result

print(solution())