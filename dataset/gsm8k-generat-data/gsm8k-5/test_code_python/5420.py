def solution():
    total_marbles = 19  # There are 19 marbles in total
    yellow_marbles = 5  # 5 of the marbles are yellow
    other_marbles = total_marbles - yellow_marbles  # The remainder are other color marbles

    # Calculate the ratio of blue marbles to red marbles
    blue_ratio = 3
    red_ratio = 4
    total_ratio = blue_ratio + red_ratio
    blue_marbles = other_marbles * (blue_ratio / total_ratio)
    red_marbles = other_marbles * (red_ratio / total_ratio)

    # Calculate the difference in the number of red and yellow marbles
    difference = red_marbles - yellow_marbles
    result = difference
    return result

print(solution())