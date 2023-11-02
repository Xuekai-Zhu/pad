def solution():
    num_watermelons = 1
    num_peach_trees = 1
    num_plum_trees = 2

    # Calculate the total number of peaches
    num_peaches = num_watermelons + 12

    # Calculate the total number of plums
    num_plums = num_peaches * 3

    # Calculate the total number of pieces of fruit
    total_fruit = num_watermelons + num_peaches + num_plums
    result = total_fruit
    return result

print(solution())