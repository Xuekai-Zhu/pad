def solution():
    total_marbles = 63
    dark_blue_marbles = total_marbles / 3
    green_marbles = 4

    # Calculate the total number of red marbles
    red_marbles = total_marbles - dark_blue_marbles - green_marbles
    result = red_marbles
    return result

print(solution())