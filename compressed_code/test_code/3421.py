def solution():
    
    trees_per_square_mile = 600
    forest_size = 4 * 6
    total_trees = forest_size * trees_per_square_mile
    days_to_cut_trees = total_trees / (6 * 8)
    months_to_cut_trees = days_to_cut_trees / 30
    result = months_to_cut_trees
    return result

print(solution())