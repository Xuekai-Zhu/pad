def solution():
    """About 450 000 people lived in Maryville in 2000. In 2005, about 467 000 people lived in Maryville. What is the average number of people added each year?"""
    # Define the starting population and the final population
    start_population = 450000
    final_population = 467000

    # Calculate the total number of people added over the 5-year period
    total_population_added = final_population - start_population

    # Calculate the average number of people added per year
    average_population_added = total_population_added / 5

    # Return the result
    result = average_population_added
    return result

print(solution())