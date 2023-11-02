def solution():
    total_marbles = 19
    yellow_marbles = 5
    blue_red_ratio = 3/4

    # Calculate the number of blue and red marbles combined
    blue_red_marbles = total_marbles - yellow_marbles

    # Calculate the number of red marbles
    red_marbles = blue_red_marbles * (4/7)

    # Calculate the difference between red and yellow marbles
    difference = red_marbles - yellow_marbles
    result = difference
    return result

print(solution())