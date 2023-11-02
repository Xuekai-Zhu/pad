def solution():
    initial_trees = 8
    years_since_initial = 5
    annual_trees = 1
    total_trees = initial_trees + (years_since_initial * annual_trees)
    result = total_trees
    return result

print(solution())