def solution():
    total_marbles = 72
    each_color = total_marbles // 3
    red_marbles = each_color
    blue_marbles = each_color
    yellow_marbles = each_color

    # Subtract the lost marbles from each color
    red_marbles = red_marbles - 5
    blue_marbles = blue_marbles - (2 * 5)
    yellow_marbles = yellow_marbles - (3 * 5)

    # Calculate the total remaining marbles
    remaining_marbles = red_marbles + blue_marbles + yellow_marbles

    result = remaining_marbles
    return result

print(solution())