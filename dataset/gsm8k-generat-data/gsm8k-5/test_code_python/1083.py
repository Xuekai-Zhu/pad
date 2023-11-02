def solution():
    production_per_day = 10  # The factory produces 10 televisions per day
    days_per_year = 365  # There are 365 days in a year

    # Calculate the total production in the first year
    total_production_first_year = production_per_day * days_per_year

    # Calculate the reduced production in the second year
    reduced_production_second_year = total_production_first_year * 0.9

    # Calculate the total production in the second year
    total_production_second_year = reduced_production_second_year * days_per_year
    result = total_production_second_year
    return result

print(solution())