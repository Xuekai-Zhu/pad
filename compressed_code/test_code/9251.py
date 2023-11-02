def solution():
    
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