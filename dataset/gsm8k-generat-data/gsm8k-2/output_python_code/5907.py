def solution():
    """Jack has a grove with 4 trees by 5 trees. It takes 6 minutes to clean each tree. He gets help to clean the trees so it only takes half as long. How many hours did he spend cleaning trees?"""
    num_trees = 4 * 5
    time_per_tree = 6 / 2  # half as long with help
    total_time = num_trees * time_per_tree
    hours = total_time / 60
    result = hours
    return result

print(solution())