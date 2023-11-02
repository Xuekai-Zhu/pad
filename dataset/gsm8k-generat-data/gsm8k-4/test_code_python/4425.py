def solution():
    """Mary Anne drinks 1/5 of a bottle of sparkling water every night at dinner. If each bottle costs her $2.00, how much does she spend on sparkling water every year?"""
    # Define the amount of sparkling water consumed per night
    daily_consumption = 1 / 5

    # Define the cost of one bottle of sparkling water
    bottle_cost = 2.0

    # Calculate the amount spent on sparkling water per night
    nightly_spending = daily_consumption * bottle_cost

    # Calculate the amount spent on sparkling water per year
    yearly_spending = nightly_spending * 365

    result = yearly_spending
    return result

print(solution())