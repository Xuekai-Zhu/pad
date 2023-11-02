def solution():
    # Count the number of yellow marbles
    yellow_marbles = 5

    # Calculate the total number of blue and red marbles
    total_marbles = 19 - yellow_marbles

    # Calculate the ratio of blue marbles to red marbles
    blue_to_red_ratio = 3/4

    # Calculate the number of red marbles
    red_marbles = total_marbles * (4/7)

    # Calculate the difference between red and yellow marbles
    difference = red_marbles - yellow_marbles
    result = difference
    return result

print(solution())