def solution():
    """John drives 1000 miles a month. He needs to get an oil change every 3000 miles. He gets 1 free oil change a year. If an oil change costs $50, how much does he pay a year?"""
    # Calculate the number of oil changes required in a year
    miles_per_year = 1000 * 12
    oil_changes_per_year = miles_per_year / 3000
    total_oil_changes_per_year = oil_changes_per_year + 1

    # Calculate the total cost of oil changes per year
    oil_change_cost = total_oil_changes_per_year * 50

    # return the result
    result = oil_change_cost
    return result

print(solution())