def solution():
    num_green_houses = 90
    ratio_green_yellow = 3  # Isabella has 3 times as many green houses as yellow houses
    num_yellow_houses = num_green_houses / ratio_green_yellow

    # Isabella has 40 fewer yellow houses than red houses
    num_red_houses = num_yellow_houses + 40

    # Calculate the total number of houses
    total_houses = num_red_houses + num_yellow_houses + num_green_houses

    # Calculate the number of houses that are not yellow
    num_not_yellow = total_houses - num_yellow_houses
    result = num_not_yellow
    return result

print(solution())