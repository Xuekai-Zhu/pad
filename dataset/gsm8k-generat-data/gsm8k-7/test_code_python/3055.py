def solution():
    initial_percent = 100
    rate_of_evaporation = 0.2
    num_years = 2

    # Calculate the percent of vinegar left after one year
    percent_left_after_one_year = (1 - rate_of_evaporation) * initial_percent

    # Calculate the percent of vinegar left after two years
    percent_left_after_two_years = (1 - rate_of_evaporation) * percent_left_after_one_year

    result = percent_left_after_two_years
    return result

print(solution())