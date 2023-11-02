def solution():
    """Los Angeles has 6 million people living in it. If half the population is women and 1/3 of the women work in retail, how many women work in retail in Los Angeles?"""
    # Define the total population of Los Angeles and calculate the number of women
    total_population = 6000000
    women_population = total_population / 2

    # Calculate the number of women who work in retail
    retail_workers = women_population / 3

    # Return the result
    result = retail_workers
    return result

print(solution())