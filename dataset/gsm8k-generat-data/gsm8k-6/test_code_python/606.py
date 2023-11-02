def solution():
    # Calculate the number of green marbles
    green_marbles = 3 * 20  # three times more green marbles than red

    # Calculate the number of yellow marbles
    yellow_marbles = 0.2 * green_marbles  # yellow marbles make up 20% of the green marbles

    # Calculate the total number of marbles in the box
    total_marbles = green_marbles + yellow_marbles + 20  # total is three times more than the number of green marbles

    # Calculate the number of marbles of a different color
    diff_color_marbles = total_marbles - (20 + green_marbles + yellow_marbles)  # subtract red, green, and yellow marbles from total

    result = diff_color_marbles
    return result

print(solution())