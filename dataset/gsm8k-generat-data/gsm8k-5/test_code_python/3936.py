def solution():
    total_population = 6000000  # Los Angeles has a total population of 6 million people
    women_population = total_population / 2  # Half of the population are women
    women_working_retail = (1 / 3) * women_population  # 1/3 of the women work in retail

    result = women_working_retail
    return result

print(solution())