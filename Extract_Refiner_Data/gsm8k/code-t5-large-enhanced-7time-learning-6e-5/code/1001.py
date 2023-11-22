def solution():
    
    # Define the total population of porcupines
    total_population = 50

    # Calculate the number of female porcupines
    female_population = total_population * (3/5)

    # Calculate the total number of porcupines after a year
    total_population_after_year = total_population + (female_population * 4)

    # Display the total number of porcupines after a year
    result = total_population_after_year
    return result

print(solution())