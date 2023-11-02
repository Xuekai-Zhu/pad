def solution():
    
    tree_height = 52
    years_passed = 8
    growth_per_year = 5
    total_growth = growth_per_year * years_passed
    height_in_inches = (tree_height + total_growth) * 12
    result = height_in_inches
    return result

print(solution())