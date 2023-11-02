def solution():
    total_marbles = 85
    num_red = 14
    num_blue = 3 * num_red

    # Calculate the total number of yellow marbles
    num_yellow = total_marbles - num_red - num_blue
    result = num_yellow
    return result

print(solution())