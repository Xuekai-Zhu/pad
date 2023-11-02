def solution():
    initial_population = 450000  # Initial population in 2000
    final_population = 467000  # Final population in 2005
    time_period = 5  # Time period between 2000 and 2005

    # Calculate the average number of people added per year
    people_added_per_year = (final_population - initial_population) / time_period
    result = people_added_per_year
    return result

print(solution())