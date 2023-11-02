def solution():
    current_production = 100  # The company currently produces 100 cars per month
    target_production = 1800  # The company wants to produce 1800 cars per year
    months_per_year = 12  # There are 12 months in a year

    # Calculate the additional cars needed per month to reach the target
    additional_cars_needed = (target_production / months_per_year) - current_production

    result = additional_cars_needed
    return result

print(solution())