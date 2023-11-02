def solution():
    num_white = 12
    num_blue = 6
    num_marbles = 20

    # Calculate the number of green marbles
    num_green = num_marbles - num_white - num_blue
    result = num_green
    return result

print(solution())