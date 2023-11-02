def solution():
    blue_ratio = 1/2  # Half of the marbles are blue
    red_ratio = 1/4  # A quarter of the marbles are red
    green_count = 27  # 27 of the marbles are green
    yellow_count = 14  # 14 of the marbles are yellow

    # calculate the combined ratio of blue and red marbles
    blue_red_ratio = blue_ratio + red_ratio

    # calculate the total ratio of marbles that are not green or yellow
    other_ratio = 1 - blue_red_ratio - (green_count/(blue_ratio+red_ratio)) - (yellow_count/blue_ratio)

    # calculate the number of marbles in the jar
    total_marbles = int((green_count+yellow_count)/other_ratio)

    result = total_marbles
    return result

print(solution())