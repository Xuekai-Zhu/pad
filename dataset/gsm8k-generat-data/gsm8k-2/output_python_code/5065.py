def solution():
    """About 450 000 people lived in Maryville in 2000. In 2005, about 467 000 people lived in Maryville. What is the average number of people added each year?"""
    start_population = 450000
    end_population = 467000
    duration_years = 5
    average_growth_per_year = (end_population - start_population) / duration_years
    result = average_growth_per_year
    return result

print(solution())