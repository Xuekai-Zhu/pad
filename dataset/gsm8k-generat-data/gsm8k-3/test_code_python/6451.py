def solution():
    """John drives 1000 miles a month.  He needs to get an oil change every 3000 miles.  He gets 1 free oil change a year.  If an oil change costs $50, how much does he pay a year?"""
    # Define relevant values
    MILES_PER_MONTH = 1000
    MILES_PER_OIL_CHANGE = 3000
    OIL_CHANGE_COST = 50
    FREE_OIL_CHANGES = 1

    # Calculate the number of oil changes John needs per year
    oil_changes_per_year = (MILES_PER_MONTH * 12) / MILES_PER_OIL_CHANGE

    # Subtract the number of free oil changes from the total
    oil_changes_paid = oil_changes_per_year - FREE_OIL_CHANGES

    # Calculate the total cost of oil changes paid for
    oil_change_cost_paid = oil_changes_paid * OIL_CHANGE_COST

    # Display the total cost paid for oil changes
    result = oil_change_cost_paid
    return result

print(solution())