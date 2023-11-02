def solution():
    # Calculate the number of green marbles
    red_marbles = 20
    green_marbles = 3 * red_marbles

    # Calculate the number of yellow marbles
    yellow_marbles = 0.2 * green_marbles

    # Calculate the total number of marbles
    total_marbles = 3 * green_marbles

    # Calculate the number of marbles that are not red, green, or yellow
    other_marbles = total_marbles - (red_marbles + green_marbles + yellow_marbles)
    result = other_marbles
    return result

print(solution())