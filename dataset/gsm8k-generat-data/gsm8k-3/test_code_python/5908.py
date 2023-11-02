def solution():
    """Jack has a grove with 4 trees by 5 trees.  It takes 6 minutes to clean each tree.  He gets help to clean the trees so it only takes half as long.  How many hours did he spend cleaning trees?"""
    # Define the number of trees in Jack's grove
    rows = 4
    columns = 5
    total_trees = rows * columns

    # Define the time it takes to clean each tree and the time it takes with help
    time_per_tree = 6
    time_with_help = time_per_tree / 2

    # Calculate the total time it takes to clean all the trees
    total_time = total_trees * time_with_help

    # Convert total time to hours
    hours = total_time / 60

    # Display the total time spent cleaning trees in hours
    result = hours
    return result

print(solution())