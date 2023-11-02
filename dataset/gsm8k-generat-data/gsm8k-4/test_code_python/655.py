def solution():
    """Hawkeye is driving to his aunt. He has to charge his battery for $3.5 per charge. If he charged his battery four times, and his battery charging budget was $20, how much money was he left with when he reached his aunt's place?"""
    # Define the cost per battery charge
    CHARGE_COST = 3.5

    # Define the number of battery charges
    num_charges = 4

    # Define the battery charging budget
    budget = 20

    # Calculate the total cost of the battery charges
    total_cost = CHARGE_COST * num_charges

    # Deduct the total cost from the budget to find the remaining amount of money
    remaining_money = budget - total_cost

    # return the result
    result = remaining_money
    return result

print(solution())