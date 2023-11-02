def solution():
    """Jack has a grove with 4 trees by 5 trees. It takes 6 minutes to clean each tree. He gets help to clean the trees so it only takes half as long. How many hours did he spend cleaning trees?"""
    num_trees = 4 * 5
    time_per_tree = 6 # in minutes
    total_time = num_trees * time_per_tree # in minutes
    total_time_with_help = total_time / 2 # in minutes
    hours_spent_cleaning = total_time_with_help / 60 # in hours
    result = hours_spent_cleaning
    return result

print(solution())