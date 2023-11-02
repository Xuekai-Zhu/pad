def solution():
    normal_lemons_per_year = 60
    increase_percent = 0.5  # 50% increase
    num_trees = 50 * 30
    num_years = 5

    # Calculate the number of lemons per year for each engineered lemon tree
    engineered_lemons_per_year = normal_lemons_per_year * (1 + increase_percent)

    # Calculate the total number of lemons produced each year
    total_lemons_per_year = num_trees * engineered_lemons_per_year

    # Calculate the total number of lemons produced over 5 years
    total_lemons = total_lemons_per_year * num_years
    result = total_lemons
    return result

print(solution())