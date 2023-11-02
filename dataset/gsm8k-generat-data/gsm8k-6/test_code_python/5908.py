def solution():
    num_trees = 4 * 5  # number of trees in the grove
    cleaning_time = 6  # time it takes to clean one tree in minutes
    total_time = num_trees * cleaning_time / 2  # total time to clean all trees with help
    hours_spent = total_time / 60  # convert minutes to hours
    result = hours_spent
    return result

print(solution())