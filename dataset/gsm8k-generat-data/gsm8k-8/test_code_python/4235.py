def solution():
    # Define the variables
    original_population = x
    new_population = 100
    population_outflow = 400
    current_population = 60

    # Calculate the population after year 1
    year1_population = (original_population + new_population - population_outflow) / 2

    # Calculate the population after year 2
    year2_population = year1_population / 2

    # Calculate the population after year 3
    year3_population = year2_population / 2

    # Calculate the population after year 4
    year4_population = year3_population / 2

    # Solve for the original population
    original_population = ((current_population * 2) + population_outflow - new_population) * 16

    result = original_population
    return result

print(solution())