def solution():
    """About 450 000 people lived in Maryville in 2000. In 2005, about 467 000 people lived in Maryville. What is the average number of people added each year?"""
    initial_population = 450000
    final_population = 467000
    years_passed = 5
    average_population_increase_per_year = (final_population - initial_population) / years_passed
    result = average_population_increase_per_year
    return result

print(solution())