def solution():
    # Calculate the number of blue marbles in the bowl
    total_non_yellow = 19 - 5  # the remainder of the marbles after the yellow ones are taken
    blue_marbles = total_non_yellow * (3/7)  # blue marbles are 3/7 of the remaining marbles
    red_marbles = total_non_yellow * (4/7)  # red marbles are 4/7 of the remaining marbles
    yellow_to_red_diff = red_marbles - 5  # calculate the difference between the number of red and yellow marbles
    result = yellow_to_red_diff
    return result

print(solution())