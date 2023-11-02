def solution():
    """Charles is moving from Springfield, which has 482,653 people, to Greenville, which has 119,666 fewer people. What is the total population of Springfield and Greenville?"""
    # Define the population of Springfield and the difference in population with Greenville
    springfield_population = 482653
    greenville_population_diff = -119666

    # Calculate the population of Greenville
    greenville_population = springfield_population + greenville_population_diff

    # Calculate the total population of Springfield and Greenville
    total_population = springfield_population + greenville_population

    result = total_population
    return result

print(solution())