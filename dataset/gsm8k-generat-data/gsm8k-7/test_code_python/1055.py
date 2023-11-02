def solution():
    population_New_England = 2100000
    population_New_York = (2/3) * population_New_England
    
    # Calculate the combined population of New England and New York
    combined_population = population_New_England + population_New_York
    result = combined_population
    return result

print(solution())