def solution():
    initial_population = 450000
    final_population = 467000
    num_years = 5

    # Calculate the total increase in population
    total_increase = final_population - initial_population

    # Calculate the average increase in population per year
    average_increase = total_increase / num_years
    result = average_increase
    return result

print(solution())