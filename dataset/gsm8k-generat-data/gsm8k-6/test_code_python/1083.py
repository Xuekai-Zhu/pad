def solution():
    # Calculate the production of televisions in second year
    first_year_production = 10 * 365  # number of days in a year multiplied by daily production
    second_year_production = first_year_production * 0.9  # 10% reduction in production
    result = second_year_production
    return result

print(solution())