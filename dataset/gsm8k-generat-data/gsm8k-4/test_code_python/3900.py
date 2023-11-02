def solution():
    """If the wages of 15 workers for 6 days is $9450. What would be the wages for 19 workers for 5 days?"""
    # Define the initial conditions
    workers1 = 15
    days1 = 6
    wage1 = 9450

    # Calculate the daily wage per worker
    daily_wage_per_worker = wage1 / (workers1 * days1)

    # Calculate the wages for the second scenario
    workers2 = 19
    days2 = 5
    wage2 = daily_wage_per_worker * (workers2 * days2)

    # Return the result
    result = wage2
    return result

print(solution())