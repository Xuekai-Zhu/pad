def solution():
    """Jack has a grove with 4 trees by 5 trees. It takes 6 minutes to clean each tree. He gets help to clean the trees so it only takes half as long. How many hours did he spend cleaning trees?"""
    # Define the dimensions of the grove
    ROWS = 4
    COLUMNS = 5

    # Define the time it takes to clean one tree and the time it takes with help
    CLEANING_TIME = 6
    HELPED_CLEANING_TIME = CLEANING_TIME / 2

    # Calculate the total number of trees in the grove
    total_trees = ROWS * COLUMNS

    # Calculate the total cleaning time without help and with help
    time_without_help = total_trees * CLEANING_TIME
    time_with_help = total_trees * HELPED_CLEANING_TIME

    # Convert the cleaning time to hours
    hours_without_help = time_without_help / 60
    hours_with_help = time_with_help / 60

    # Display the hours spent cleaning trees
    result = hours_with_help
    return result

print(solution())