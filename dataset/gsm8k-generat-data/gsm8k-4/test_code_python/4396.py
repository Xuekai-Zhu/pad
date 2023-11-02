def solution():
    """One logger can cut down 6 trees per day. The forest is a rectangle measuring 4 miles by 6 miles, and each square mile has 600 trees. If there are 30 days in each month, how many months will it take 8 loggers to cut down all the trees?"""
    # Define the number of trees in each square mile
    TREES_PER_MILE = 600

    # Define the size of the forest
    WIDTH = 4
    LENGTH = 6

    # Calculate the total number of trees in the forest
    total_trees = WIDTH * LENGTH * TREES_PER_MILE

    # Calculate the number of trees one logger can cut down in a month
    logger_trees_per_month = 6 * 30

    # Calculate the number of trees 8 loggers can cut down in a month
    total_logger_trees_per_month = logger_trees_per_month * 8

    # Calculate the number of months it will take to cut down all the trees
    months = total_trees / total_logger_trees_per_month

    result = round(months, 2)
    return result

print(solution())