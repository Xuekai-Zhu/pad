def solution():
    # Calculate the current production rate per year
    current_production = 100 * 12

    # Calculate the additional cars needed per year to reach the target
    additional_cars = 1800 - current_production

    # Calculate the additional cars needed per month to reach the target
    additional_cars_per_month = additional_cars / 12

    result = additional_cars_per_month
    return result

print(solution())