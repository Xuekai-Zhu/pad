def solution():
    """John decides to get a new apartment with a roommate.  His former rent was $2 per square foot for a 750 square foot apartment.  His new apartment cost $2800 per month, which he splits evenly with the roommate.  How much money does he save a year?"""
    # Calculate John's former monthly rent
    old_rent = 2 * 750

    # Calculate John's new monthly rent
    new_rent = 2800 / 2

    # Calculate John's monthly savings
    monthly_savings = old_rent - new_rent

    # Calculate John's yearly savings
    yearly_savings = monthly_savings * 12

    # Display John's yearly savings
    result = yearly_savings
    return result

print(solution())