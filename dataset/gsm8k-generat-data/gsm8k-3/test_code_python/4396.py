def solution():
    """One logger can cut down 6 trees per day. The forest is a rectangle measuring 4 miles by 6 miles, and each square mile has 600 trees. If there are 30 days in each month, how many months will it take 8 loggers to cut down all the trees?"""
    # Calculate the total number of trees in the forest
    trees_per_square_mile = 600
    forest_area = 4 * 6 # in square miles
    total_trees = forest_area * trees_per_square_mile

    # Calculate the daily rate of one logger
    logger_rate = 6 # trees per day

    # Calculate the total number of days needed for one logger to cut down all the trees
    total_days = total_trees / logger_rate

    # Calculate the total number of months needed for 8 loggers to cut down all the trees
    months_needed = total_days / 30 / 8

    # Display the result
    result = months_needed
    return result

print(solution())