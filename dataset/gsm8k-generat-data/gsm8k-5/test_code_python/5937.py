def solution():
    total_marbles = 72  # Beth has 72 marbles in total
    num_colors = 3  # Beth has 3 different colors of marbles
    marbles_per_color = total_marbles // num_colors  # Each color has the same amount of marbles initially

    # Calculate the new number of marbles for each color after Beth loses some
    red_marbles = marbles_per_color - 5
    blue_marbles = marbles_per_color - 2 * 5
    yellow_marbles = marbles_per_color - 3 * 5

    # Calculate the total number of marbles Beth has left
    total_left = red_marbles + blue_marbles + yellow_marbles
    result = total_left
    return result

print(solution())