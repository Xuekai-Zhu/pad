def solution():
    # Calculate the total mileage driven in a week
    weekly_mileage = (50 * 3) + (100 * 4)

    # Calculate the total cost per week
    weekly_cost = (0.1 * weekly_mileage) + 100

    # Calculate the total cost per year
    yearly_cost = weekly_cost * 52
    result = yearly_cost
    return result

print(solution())