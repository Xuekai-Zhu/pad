def solution():
    """John decides to get a new apartment with a roommate. His former rent was $2 per square foot for a 750 square foot apartment. His new apartment cost $2800 per month, which he splits evenly with the roommate. How much money does he save a year?"""
    # Define the details of the old apartment
    old_rent = 2
    old_size = 750

    # Define the details of the new apartment
    new_rent = 2800 / 2
    new_size = old_size

    # Calculate the annual cost of the old apartment
    old_annual_cost = old_rent * old_size * 12

    # Calculate the annual cost of the new apartment
    new_annual_cost = new_rent * new_size * 12

    # Calculate the amount saved per year
    amount_saved = old_annual_cost - new_annual_cost

    result = amount_saved
    return result

print(solution())