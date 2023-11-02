def solution():
    """One logger can cut down 6 trees per day. The forest is a rectangle measuring 4 miles by 6 miles, and each square mile has 600 trees. If there are 30 days in each month, how many months will it take 8 loggers to cut down all the trees?"""
    trees_per_mile = 600
    total_area = 4 * 6
    total_trees = total_area * trees_per_mile
    loggers = 8
    trees_cut_per_day = loggers * 6
    days_to_cut_all_trees = total_trees // trees_cut_per_day
    months_to_cut_all_trees = days_to_cut_all_trees / 30
    result = months_to_cut_all_trees
    return result

print(solution())