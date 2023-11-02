def solution():
    """One logger can cut down 6 trees per day. The forest is a rectangle measuring 4 miles by 6 miles, and each square mile has 600 trees. If there are 30 days in each month, how many months will it take 8 loggers to cut down all the trees?"""
    trees_per_square_mile = 600
    forest_size = 4 * 6
    total_trees = forest_size * trees_per_square_mile
    days_to_cut_trees = total_trees / (6 * 8)
    months_to_cut_trees = days_to_cut_trees / 30
    result = months_to_cut_trees
    return result

print(solution())