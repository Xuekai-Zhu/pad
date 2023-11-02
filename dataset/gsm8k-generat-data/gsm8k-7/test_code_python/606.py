def solution():
    red_marbles = 20
    green_marbles = 3 * red_marbles
    yellow_marbles = 0.2 * green_marbles

    total_marbles = 3 * green_marbles
    # calculate the number of blue marbles
    blue_marbles = total_marbles - (red_marbles + green_marbles + yellow_marbles)

    # return the total number of marbles of a different color
    result = blue_marbles
    return result

print(solution())