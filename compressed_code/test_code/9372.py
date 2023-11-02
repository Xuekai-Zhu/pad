def solution():
    
    normal_lemon_production = 60
    engineered_lemon_production = normal_lemon_production * 1.5
    num_trees = 50 * 30
    total_lemons_per_year = num_trees * engineered_lemon_production
    total_lemons_in_5_years = total_lemons_per_year * 5
    result = total_lemons_in_5_years
    return result

print(solution())